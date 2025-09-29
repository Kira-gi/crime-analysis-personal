import requests
from app.ml.data_cleaning import pd
from app.models import db, User, Crime
from werkzeug.security import generate_password_hash

def import_api_data():
    api_url = 'https://data.lacity.org/resource/2nrs-mtv8.json?$limit=1300000'
    response = requests.get(api_url)

    if response.status_code == 200:
        djson = response.json()
        data = pd.DataFrame(djson)

        for _, row in data.iterrows():
            try:
                age_str = str(row.get('vict_age', '')).strip()
                vict_age = int(age_str) if age_str.isdigit() else None

                crime = Crime(
                    date_occ=row.get('date_occ'),
                    vict_age=vict_age,
                    vict_sex=row.get('vict_sex'),
                    vict_descent=row.get('vict_descent'),
                    area_name=row.get('area_name'),
                    crm_cd_desc=row.get('crm_cd_desc'),
                    weapon_type=row.get('weapon_desc'),
                    status=row.get('status'),
                    lat=float(row.get('lat', 0)) if row.get('lat') else None,
                    lon=float(row.get('lon', 0)) if row.get('lon') else None
                )

                db.session.add(crime)
            except Exception as e:
                print(f'Error adding row: {e}')
        
        try:
            db.session.commit()
            print("API data imported successfully.")
        except Exception as e:
            print(f"Commit failed: {e}")
            db.session.rollback()
    else:
        print(f"Failed to retrieve data: {response.status_code}")


def create_user():
    if not User.query.filter_by(username='admin').first():
        hashed_pw = generate_password_hash('admin123')
        user = User(username='admin', password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        print("Default user created.")
