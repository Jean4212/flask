from flask_wtf import FlaskForm
from wtforms import Form, IntegerField, SelectField, SubmitField, StringField, validators, DateField
from wtforms.validators import DataRequired, Length, number_range

class formcalculadora(FlaskForm):
	dni = StringField("Dni",  validators=[validators.input_required(), Length(min=8, max=8)])	     
	paterno = StringField("Dni",  validators=[validators.input_required(), Length(min=3, max=20)])     
	materno = StringField("Dni",  validators=[validators.input_required(), Length(min=3, max=20)])   
	nombre = StringField("Dni",  validators=[validators.input_required(), Length(min=3, max=30)])         
	nacimiento = DateField("Dni",  validators=[validators.input_required(),  number_range(min="1900-01-01", max="2050-01-01")])     
    #nacimiento=SelectField("Operador",choices=[("+","Sumar"),("-","Resta"),
							#("*","Multiplicar"),("/","Dividir")])
	submit = SubmitField('Submit')