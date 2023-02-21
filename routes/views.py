import os
from flask import render_template, request, redirect
from werkzeug.utils import secure_filename
from models.model import db, User


data = []
for num in range(100):
    line = {"paterno": "Oropeza", "materno": "Inca", "nombre": "Jeancarlos Alberto",
         "dni": num, "cargo": "Asistente", "distrito": "Chorrillos",
         "licencia": "A48555618", "categoria": "AIIIC", "revalidacion":"01/01/2022",
         "nacimiento": "01/01/2000", "ingreso": "01/01/2022"}
    data.append(line)

def index():       
    
    usuario = User(username="dsds", email="ddfsfd")
    db.session.add(usuario)
    db.session.commit()

    return render_template("index.html")

def trabajadores():   
    return render_template("trabajadores.html", data=data)

def asistencia():    
    return render_template("asistencia.html", data=data)

def desarrollo():    
    return render_template("desarrollo.html")

def planilla():    
    return render_template("planilla.html")

def login():
    return render_template("login.html")

def admin():

    if request.method == "POST":
        dni = request.form.get("dni")
        paterno = request.form.get("paterno")
        materno = request.form.get("materno")
        nombre = request.form.get("nombre")
        nacimiento = request.form.get("nacimiento")
        ingreso = request.form.get("ingreso") 
        licencia = request.form.get("licencia")
        categoria = request.form.get("categoria")
        revalidacion = request.form.get("revalidacion")
        distrito = request.form.get("distrito") 

        file = request.files['file']
        if file.filename != '':            
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(os.getcwd() + "/static/uploads", filename))
      
        return redirect(request.url)

    return render_template("admin.html")