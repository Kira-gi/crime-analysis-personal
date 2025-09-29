from app.models import db, Crime
import pandas as pd

def fetch_db_data():
    query = Crime.query.all()
    crime_data = [{
        'date_occ': row.date_occ,
        'vict_age': row.vict_age,
        'vict_sex': row.vict_sex,
        'vict_descent': row.vict_descent,
        'area_name': row.area_name,
        'crm_cd_desc': row.crm_cd_desc,
        'weapon_type': row.weapon_type,
        'status': row.status,
        'lat': row.lat,
        'lon': row.lon
    } for row in query]
    return pd.DataFrame(crime_data)

def clean_data(df):
    df = df.dropna(subset=['lat', 'lon', 'vict_sex','vict_descent'])  # Remove records with missing geolocation
    df = df[df['vict_age'].between(0, 120, inclusive='both')]  # Keep plausible ages
    df = df[df['status'].isin(['IC', 'CC', 'AO'])]  # Example: filter valid statuses
    return df

def clear_crime_table():
    db.session.query(Crime).delete()
    db.session.commit()
    print("All original records deleted.")

def insert_cleaned_data(df):
    for _, row in df.iterrows():
        crime = Crime(
            date_occ=row['date_occ'],
            vict_age=row['vict_age'],
            vict_sex=row['vict_sex'],
            vict_descent=row['vict_descent'],
            area_name=row['area_name'],
            crm_cd_desc=row['crm_cd_desc'],
            weapon_type=row['weapon_type'],
            status=row['status'],
            lat=row['lat'],
            lon=row['lon']
        )
        db.session.add(crime)
    db.session.commit()
    print("Cleaned data inserted into the Crime table.")