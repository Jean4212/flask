from flask import Flask, render_template, url_for

app = Flask(__name__)

data = [{"paterno": "Oropeza", "materno": "Inca", "nombre": "Jeancarlos Alberto",
         "dni": "48555618", "cargo": "Asistente", "distrito": "Chorrillos",
         "licencia": "A48555618", "categoria": "AIIIC", "revalidacion":"01/01/2022",
         "nacimiento": "01/01/2000", "ingreso": "01/01/2022"}, 
         {"paterno": "Garcia", "materno": "Guivin", "nombre": "Claret Magna",
           "dni": "40137921", "cargo": "Empleada", "distrito": "Surco",
           "licencia": "A40137921", "categoria": "AIIB", "revalidacion":"10/11/2022",
            "nacimiento": "05/04/1990", "ingreso": "31/12/2019"}]

@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/trabajadores")
def trabajadores():    
    return render_template("trabajadores.html", data=data)

@app.route("/planilla")
def planilla():    
    return render_template("planilla.html")

@app.route("/asistencia")
def asistencia():    
    return render_template("asistencia.html")


if __name__ == "__main__":
    app.run(debug=True)