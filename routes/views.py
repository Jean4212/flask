from flask import render_template

data = []
for num in range(100):
    line = {"paterno": "Oropeza", "materno": "Inca", "nombre": "Jeancarlos Alberto",
         "dni": num, "cargo": "Asistente", "distrito": "Chorrillos",
         "licencia": "A48555618", "categoria": "AIIIC", "revalidacion":"01/01/2022",
         "nacimiento": "01/01/2000", "ingreso": "01/01/2022"}
    data.append(line)

def index():
    a = 1
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