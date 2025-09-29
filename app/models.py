from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
class Crime(db.Model):
    __bind_key__ = 'crimes'
    id = db.Column(db.Integer, primary_key=True)
    date_occ = db.Column(db.String(100))
    vict_age = db.Column(db.Integer)
    vict_sex = db.Column(db.String(10))
    vict_descent = db.Column(db.String(100))
    area_name = db.Column(db.String(100))
    crm_cd_desc = db.Column(db.String(100))
    weapon_type = db.Column(db.String(100))
    status = db.Column(db.String(2))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)