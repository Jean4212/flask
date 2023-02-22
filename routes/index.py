from flask import render_template, redirect, request, flash
from models.model import Persons

def index():
    if request.method == 'POST':

        content = request.json

        print(content)
        print(content["dni"])


        dni = content["dni"]
        #paterno = request.form.get('paterno')
        #materno = request.form.get('materno')
        #nombre = request.form.get('nombre')
#
        person = Persons.query.filter_by(dni=dni).first()
    #
        if person:                    
            return {"person": True}
#
#
        #print(f"Tu dni es: {dni} y tu nombre es: {nombre}")       
        return {"person": False}

    
    return render_template("prueba.html")
	