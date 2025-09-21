Crime-analysis-personal 

==================================== 

Author: Kirubel Gebreyohanis  

Affiliation: Southeast Missouri State University  

Course: CS499 - Capstone  

Sponsor: Rich Flotron 

 

Project Description: 

------------------------- 

This project was developed as part of my Capstone course at Southeast Missouri State University. It applies data mining, machine learning, and web technologies to analyze and forecast crime rates in Los Angeles. The system includes time-series forecasting using SARIMA and LSTM, geospatial clustering via DBSCAN, and an interactive web dashboard built with Flask. 

This repository is my personal version of the group project, showcasing my contributions and learnings. 

My Contributions: 

----------------------- 

Implemented search filters for crime data (age, race, date, area, weapon, status). 

Helped design SQLAlchemy models for Users and Crimes. 

Assisted in building Flask routes and Jinja-based templates. 

Worked with teammates on SARIMA and LSTM forecasting. 

Contributed to testing and debugging across multiple modules. 

Key Features: 

----------------- 

Predict monthly crime trends using SARIMA and LSTM models. 

Visualize crime hotspots on an interactive heatmap (Folium). 

Filter/search crime data by multiple attributes. 

Secure login/logout functionality with role-based session handling. 

Responsive web UI with HTML/CSS templating. 

Technologies Used: 

------------------------- 

Python (Flask, SQLAlchemy, TensorFlow, scikit-learn, Pandas, Folium) 

SQLite (local data storage) 

HTML/CSS (Jinja templating + custom CSS) 

Bootstrap-style responsive forms 

LAPD Open Data API (source data) 

File Structure: 

------------------ 

/app/ 

init.py → App factory and route registration 

models.py → SQLAlchemy models for Users and Crimes 

auth_route.py → User login/logout and session handling 

search_route.py → Crime data filtering and pagination 

heat_route.py → Heatmap visualization based on filtered crimes 

/templates/ 

base.html → Shared layout with nav/footer 

login.html → Login page 

search.html → Search filters + paginated crime results 

heatmap.html → Embedded Folium map 

/static/ 

style.css → CSS for layout and form styling 

run.py → Entry point for running the Flask app 

setup_db.py → Initializes the SQLite database and tables 

LA_Crime_Data_from_2020_to_Present.csv → Source dataset 

How to run: 

-------------- 

1. Clone or download this repository. 

2. Ensure you have Python 3.8+ and pip installed. 

3. Install dependencies: 

   ``` 

  pip install -r requirements.txt 
   ```  

4. Initialize the database:python setup_db.py 

  ``` 
   python setup_db.py 
   ``` 
  

5. Launch the web application:python run.py 

     ``` 
     python run.py 
     ``` 
  

6. Open your browser and go to http://127.0.0.1:5000  

 

User Credentials: 

---------------------- 

You can create users manually via the database or implement a registration system. 

 

Default roles: 

----------------- 

User: View search and heatmap 

Admin (if enabled): Can access restricted panels 

 

Future Enhancement: 

--------------------------- 

 

Real-time data updates via LAPD API 

Admin dashboard for managing users and data 

Role-based access control with more granular permissions 

More robust model retraining pipelines 

Enhanced visualizations with dynamic filters 

License: 

---------- 

Open source for academic purposes only. Do not deploy in production with real data without additional security, legal, and ethical safeguards. 

Reference:  

-------------- 

LAPD Crime Data: https://data.lacity.org/ 

SARIMA documentation: https://www.statsmodels.org/ 

LSTM Forecasting: https://www.tensorflow.org/ 

 
