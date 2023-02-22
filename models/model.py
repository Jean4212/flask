from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Persons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(8))
    paterno = db.Column(db.String(30))
    materno = db.Column(db.String(30))
    nombre = db.Column(db.String(30))
    nacimiento = db.Column(db.String(10))
   