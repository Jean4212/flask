from flask import render_template

data = [{"paterno": "Oropeza", "materno": "Inca", "nombre": "Jeancarlos Alberto",
         "dni": "48555618", "cargo": "Asistente", "distrito": "Chorrillos",
         "licencia": "A48555618", "categoria": "AIIIC", "revalidacion":"01/01/2022",
         "nacimiento": "01/01/2000", "ingreso": "01/01/2022"}, 
         {"paterno": "Garcia", "materno": "Guivin", "nombre": "Claret Magna",
          "dni": "40137921", "cargo": "Empleada", "distrito": "Surco",
          "licencia": "A40137921", "categoria": "AIIB", "revalidacion":"10/11/2022",
          "nacimiento": "05/04/1990", "ingreso": "31/12/2019"},
          {"paterno": "Oropeza", "materno": "Inca", "nombre": "Jeancarlos Alberto",
         "dni": "48555618", "cargo": "Asistente", "distrito": "Chorrillos",
         "licencia": "A48555618", "categoria": "AIIIC", "revalidacion":"01/01/2022",
         "nacimiento": "01/01/2000", "ingreso": "01/01/2022"}, 
         {"paterno": "Garcia", "materno": "Guivin", "nombre": "Claret Magna",
          "dni": "40137921", "cargo": "Empleada", "distrito": "Surco",
          "licencia": "A40137921", "categoria": "AIIB", "revalidacion":"10/11/2022",
          "nacimiento": "05/04/1990", "ingreso": "31/12/2019"},
          {"paterno": "Oropeza", "materno": "Inca", "nombre": "Jeancarlos Alberto",
         "dni": "48555618", "cargo": "Asistente", "distrito": "Chorrillos",
         "licencia": "A48555618", "categoria": "AIIIC", "revalidacion":"01/01/2022",
         "nacimiento": "01/01/2000", "ingreso": "01/01/2022"}, 
         {"paterno": "Garcia", "materno": "Guivin", "nombre": "Claret Magna",
          "dni": "40137921", "cargo": "Empleada", "distrito": "Surco",
          "licencia": "A40137921", "categoria": "AIIB", "revalidacion":"10/11/2022",
          "nacimiento": "05/04/1990", "ingreso": "31/12/2019"},
          {"paterno": "Oropeza", "materno": "Inca", "nombre": "Jeancarlos Alberto",
         "dni": "48555618", "cargo": "Asistente", "distrito": "Chorrillos",
         "licencia": "A48555618", "categoria": "AIIIC", "revalidacion":"01/01/2022",
         "nacimiento": "01/01/2000", "ingreso": "01/01/2022"}, 
         {"paterno": "Garcia", "materno": "Guivin", "nombre": "Claret Magna",
          "dni": "40137921", "cargo": "Empleada", "distrito": "Surco",
          "licencia": "A40137921", "categoria": "AIIB", "revalidacion":"10/11/2022",
          "nacimiento": "05/04/1990", "ingreso": "31/12/2019"},
          {"paterno": "Oropeza", "materno": "Inca", "nombre": "Jeancarlos Alberto",
         "dni": "48555618", "cargo": "Asistente", "distrito": "Chorrillos",
         "licencia": "A48555618", "categoria": "AIIIC", "revalidacion":"01/01/2022",
         "nacimiento": "01/01/2000", "ingreso": "01/01/2022"}, 
         {"paterno": "Garcia", "materno": "Guivin", "nombre": "Claret Magna",
          "dni": "40137921", "cargo": "Empleada", "distrito": "Surco",
          "licencia": "A40137921", "categoria": "AIIB", "revalidacion":"10/11/2022",
          "nacimiento": "05/04/1990", "ingreso": "31/12/2019"}]


def index():    
    return render_template("index.html")

def trabajadores():    
    return render_template("trabajadores.html", data=data)

def planilla():    
    return render_template("planilla.html")

def asistencia():    
    return render_template("asistencia.html")

def login():
    return render_template("login.html")