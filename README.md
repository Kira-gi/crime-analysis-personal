Crime Analysis and Prediction System
====================================

Author: Kirubel Gebreyohanis 
Affiliation: Southeast Missouri State University  
Course: CS499 - Capstone 

Project Description:
--------------------
This project leverages data mining, machine learning, and web technologies to analyze and forecast crime rates in Los Angeles. It includes time-series forecasting using SARIMA and LSTM, geospatial clustering via DBSCAN, and an interactive web dashboard built with Flask.

Key Features:
-------------
- Predict monthly crime trends using SARIMA and LSTM models
- Visualize crime hotspots on an interactive heatmap (Folium)
- Filter/search crime data by age, race, date, area, weapon, and status
- Secure login/logout functionality with role-based session handling
- Clean, responsive web UI with HTML/CSS templating

Technologies Used:
------------------
- Python (Flask, SQLAlchemy, TensorFlow, scikit-learn, Pandas, Folium)
- SQLite (for local data storage)
- HTML/CSS (Jinja templating)
- Bootstrap-style responsive forms (custom `style.css`)
- LAPD Open Data API for source data

File Structure:
---------------
- /app/
  - __init__.py           → App factory and route registration
  - models.py             → SQLAlchemy models for Users and Crimes
  - auth_route.py         → User login/logout and session handling
  - search_route.py       → Crime data filtering and pagination
  - heat_route.py         → Heatmap visualization based on filtered crimes
- /templates/
  - base.html             → Shared layout with nav/footer
  - login.html            → Login page
  - search.html           → Search filters + paginated crime results
  - heatmap.html          → Embedded Folium map
- /static/
  - style.css             → CSS for layout and form styling
- run.py                  → Entry point for running the Flask app
- setup_db.py             → Initializes the SQLite database and tables
- LA_Crime_Data_from_2020_to_Present.csv → Source dataset

How to Run:
-----------
1. Clone or download this repository.
2. Ensure you have Python 3.8+ and pip installed.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Initialize the database:
   ```
   python setup_db.py
   ```
5. Launch the web application:
   ```
   python run.py
   ```
6. Open your browser and go to `http://127.0.0.1:5000`

User Credentials:
-----------------
You can create users manually via the database or implement a registration system.

Default roles:
- User: View search and heatmap
- Admin (if enabled): Can access restricted panels

Future Enhancements:
--------------------
- Real-time data updates via LAPD API
- Admin dashboard for managing users and data
- Role-based access control with more granular permissions
- More robust model retraining pipelines
- Enhanced visualizations with dynamic filters

License:
--------
Open-source for academic purposes only. Do not deploy in production with real data without additional security, legal, and ethical safeguards.

References:
-----------
- LAPD Crime Data: https://data.lacity.org/
- SARIMA documentation: https://www.statsmodels.org/
- LSTM Forecasting: https://www.tensorflow.org/
