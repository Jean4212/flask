from os import path, getcwd
from flask import render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from models.model import db, Persons
from models.person import formcalculadora



data = []
for num in range(100):
    line = {"paterno": "Oropeza", "materno": "Inca", "nombre": "Jeancarlos Alberto",
         "dni": num, "cargo": "Asistente", "distrito": "Chorrillos",
         "licencia": "A48555618", "categoria": "AIIIC", "revalidacion":"01/01/2022",
         "nacimiento": "01/01/2000", "ingreso": "01/01/2022"}
    data.append(line)

def api():   
    dni = request.form.get("dni")
    person = Persons.query.filter_by(dni=dni).first()
    
    if person:   

        return f"Usuario Registrado"
    
    return f"tu dni es: {dni}" #render_template("trabajadores.html", data=data)

def index():

    form = formcalculadora(request.form)        

    if form.validate_on_submit():
        dni = form.dni.data
        paterno = form.paterno.data      
        materno = form.materno.data
        nombre = form.nombre.data      
        nacimiento = form.nacimiento.data      

        dni = request.form.get("dni")
        person = Persons.query.filter_by(dni=dni).first()

        if person:
            print('La persona se encuentra registrada')   
            return redirect(request.url)    
            
       
        print('persona registrada correctamente')   
        newPerson = Persons(dni, paterno, materno, nombre, nacimiento)
        db.session.add(newPerson)
        db.session.commit()    
        return redirect(request.url)    

        #try:
        #    resultado = eval(str(num1) + operador + str(num2))
        #except:
        #    return render_template("index.html", error="No puedo realizar la operación")
        #
        #return render_template("planilla.html", num1=num1, num2=num2, operador=operador, resultado=resultado)	
        

    return render_template("index.html", form=form)
    
    

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
        person = Persons.query.filter_by(dni=dni).first()

        if person:
            flash('La persona se encuentra registrada', "danger")            
            return redirect(request.url)

        paterno = request.form.get("paterno")
        materno = request.form.get("materno")
        nombre = request.form.get("nombre")
        nacimiento = request.form.get("nacimiento")
        ingreso = request.form.get("ingreso") 
        licencia = request.form.get("licencia")
        categoria = request.form.get("categoria")
        revalidacion = request.form.get("revalidacion")
        distrito = request.form.get("distrito")   

        newPerson = Persons(dni=dni, paterno=paterno, materno=materno, nombre=nombre, nacimiento=nacimiento)
        db.session.add(newPerson)
        db.session.commit()

        file = request.files['file']
        if file.filename != '':              
            filename = secure_filename(file.filename)            
            new_filename = dni + "." + filename.rsplit(".")[1]         
            file.save(path.join(getcwd() + "/static/uploads", new_filename))

        flash('Usuario Registrado Correctamente', "message")                
        return redirect(request.url)

    return render_template("admin.html")