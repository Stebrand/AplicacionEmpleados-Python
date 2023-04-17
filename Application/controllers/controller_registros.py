from Application import app
from flask import Flask
from flask import render_template, request, redirect
from Application.models import model_registros
from datetime import datetime, time

@app.route("/")
def inicio():
    return render_template('index.html')

@app.route("/salida")
def salida():
    return render_template('salida.html')

@app.route('/nuevo')
def nuevo():
    return render_template('nuevo.html')

@app.route('/modificar')
def modificar():
    return render_template('modificar.html')

@app.route('/borrar')
def borrar():
    return render_template('borrar.html')

@app.route('/salidamotivo')
def salidamotivo():
    return render_template('salidamotivo.html')

#######################
@app.route('/nuevo/crearempleado', methods=['POST'])
def crearempleado():
    _nombre = (request.form['Nombre_Empleado'])
    _documento = (request.form['Documento_Empleado'])
    _area = (request.form['Area_Empleado'])
    objecto = model_registros.BaseDatos()
    objecto.Crear(_documento,_nombre,_area,"empleados")
    return redirect('/nuevo')
    
@app.route('/nuevo/crearvisitante', methods=['POST'])
def crearvisitante():
    _nombre = (request.form['Nombre_Visitante'])
    _documento = (request.form['Documento_Visitante'])
    _tipo = (request.form['Tipo_Visitante'])
    crear = model_registros.BaseDatos()
    crear.Crear(_documento,_nombre,_tipo,"visitante")
    return redirect('/nuevo')

@app.route('/modificar/modempleado', methods=['POST'])
def modificarempleado():
    _documento = (request.form['Documento_Empleado'])
    _nombre = (request.form['Nombre_Empleado'])
    _area = (request.form['Area_Empleado'])
    modificar=model_registros.BaseDatos()
    empleado=modificar.Leer(_documento,"empleados")
    if(empleado):
        modificar.Modificar(_documento,_nombre,_area,"empleados")
        return redirect("/modificar", mensaje="Actualizacion Satisfactoria")
    else:
        return redirect("/modificar")
        
@app.route('/modificar/modvisitante', methods=['POST'])
def modificarvisitante():
    _documento = (request.form['Documento_Visitante'])
    _nombre = (request.form['Nombre_Visitante'])
    _tipo = (request.form['Tipo_Visitante'])
    modificar=model_registros.BaseDatos()
    visitante=modificar.Leer(_documento,"visitante")
    if(visitante):
        modificar.Modificar(_documento,_nombre,_tipo,"visitante")
        return redirect("/modificar", mensaje="Actualizacion Satisfactoria")
    else:
        return redirect("/modificar")

@app.route('/borrar/boempleado', methods=['POST'])
def borrarempleado():
    _documento = (request.form['Documento_Empleado'])
    borrar=model_registros.BaseDatos()
    borrar.Borrar(_documento,"empleados")
    return redirect("/borrar")

@app.route('/borrar/bovisitante', methods=['POST'])
def borrarvisitante():
    _documento = (request.form['Documento_Visitante'])
    borrar=model_registros.BaseDatos()
    borrar.Borrar(_documento,"visitante")
    return redirect("/borrar")

@app.route('/inempleado', methods=['POST'])
def ingresoempleado():
    _documento=(request.form['Documento_Empleado'])
    ingreso=model_registros.BaseDatos()
    empleado=ingreso.Leer(_documento,"empleados")
    print(empleado)
    if(empleado):
        _time=datetime.now()
        fechaActual=_time.strftime("%Y-%m-%d")
        horaActual=_time.strftime("%H:%M")
        ingreso.Registro(_documento,fechaActual,horaActual,"registro_empleado")
        return redirect("/")
    else:
        return redirect("/")

@app.route('/salida/saempleado', methods=['POST'])
def salidaempleado():
    _documento=(request.form['Documento_Empleado'])
    salida=model_registros.BaseDatos()
    empleado=salida.Leer(_documento,"empleados")
    if(empleado):
        if(datetime.now().time()>=time(16,00)):
            _time=datetime.now()
            fechaActual=_time.strftime("%Y-%m-%d")
            horaActual=_time.strftime("%H:%M")
            salida.RegistroSalida(_documento,fechaActual,horaActual,"registro_empleado")
            return redirect("/salida")
        else:
            print("Motivo de retiro")
            return redirect("/salidamotivo")
    else:
        return redirect("/salida")

@app.route('/salidamotivo/motivo', methods=['POST']) 
def motivosalida():
    _documento=(request.form['Documento_Empleado'])
    _motivo=(request.form['Motivo_Salida'])
    salida=model_registros.BaseDatos()
    empleado=salida.Leer(_documento,"empleados")
    if(empleado):
        _time=datetime.now()
        fechaActual=_time.strftime("%Y-%m-%d")
        horaActual=_time.strftime("%H:%M")
        salida.RegistroMotivo(_documento,fechaActual,horaActual,_motivo)
        return redirect("/salida") 
    else:
        return redirect("/salida")

@app.route('/invisitante', methods=['POST'])    
def ingresovisitante():
    _documento=(request.form['Documento_Visitante'])
    ingreso=model_registros.BaseDatos()
    visitante=ingreso.Leer(_documento,"visitante")
    if(visitante):
        _time=datetime.now()
        fechaActual=_time.strftime("%Y-%m-%d")
        horaActual=_time.strftime("%H:%M")
        ingreso.Registro(_documento,fechaActual,horaActual,"registro_visitante")
        return redirect("/")
    else:
        return redirect("/")
    
@app.route('/salida/savisitante', methods=['POST'])
def salidavisitante():
    _documento=(request.form['Documento_visitante'])
    salida=model_registros.BaseDatos()
    visitante=salida.Leer(_documento,"visitante")
    if(visitante):
        _time=datetime.now()
        fechaActual=_time.strftime("%Y-%m-%d")
        horaActual=_time.strftime("%H:%M")
        salida.RegistroSalida(_documento,fechaActual,horaActual,"registro_visitante")        
        return redirect("/salida")
    else:
        return redirect("/salida")    