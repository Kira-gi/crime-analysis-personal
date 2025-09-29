from app import create_app
from app.services.admin_functions import import_api_data, create_user
from app.ml.data_cleaning import fetch_db_data, clean_data, clear_crime_table, insert_cleaned_data
from app.models import db
app = create_app()

with app.app_context():
    db.create_all()
    create_user()
    import_api_data()
    df= fetch_db_data()
    df = clean_data(df)
    clear_crime_table()
    insert_cleaned_data(df)
    
