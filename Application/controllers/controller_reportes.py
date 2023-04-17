from Application import app
from flask import Flask
from flask import render_template, request, redirect
from Application.models import model_reportes
from datetime import datetime

theadEmpleado=("Documento","Nombre","Area","Fecha Ingreso","Hora Ingreso","Fecha Salida","Hora Salida","Motivo Salida")
theadVisitante=("Documento","Nombre","Tipo","Fecha Ingreso","Hora Ingreso","Fecha Salida","Hora Salida")

@app.route('/reportes')
def reportes():
    return render_template('reportes.html')

@app.route('/reportes/consulta', methods=['POST'])
def consulta():
    _fechaInicio=(request.form['Fecha_Inicio'])
    _fechaFin=(request.form['Fecha_Fin'])
    _visitante=(request.form['Visitante'])
    _documento=(request.form['Documento'])
    _area=(request.form['Area_Empleado'])
    datos=model_reportes.reporteBD()
    
    if(_visitante =="Empleado"):        
        if(_documento):
            if(_area):
                if(_fechaInicio or _fechaFin):
                    if(_fechaInicio and _fechaFin):
                        completar=f"WHERE empleados.documento = '{_documento}' AND empleados.area ='{_area}' AND date(fecha_ingreso)>='{_fechaInicio}' AND date(fecha_salida)<='{_fechaFin}'"
                        datos=datos.ConsultaEmpleados(completar)
                    elif(_fechaInicio):
                        completar=f"WHERE empleados.documento = '{_documento}' AND empleados.area ='{_area}' AND date(fecha_ingreso)>='{_fechaInicio}'"
                        datos=datos.ConsultaEmpleados(completar)
                    else:
                        completar=f"WHERE empleados.documento = '{_documento}' AND empleados.area ='{_area}' AND date(fecha_ingreso)>='{_fechaFin}'"
                        datos=datos.ConsultaEmpleados(completar)
                else:
                    completar=f"WHERE empleados.documento = '{_documento}' AND empleados.area ='{_area}'"
                    datos=datos.ConsultaEmpleados(completar)
            else:
                completar=f"WHERE empleados.documento = '{_documento}'"
                datos=datos.ConsultaEmpleados(completar)
        elif(_area):
            if(_fechaInicio or _fechaFin):
                    if(_fechaInicio and _fechaFin):
                        completar=f"WHERE empleados.area ='{_area}' AND date(fecha_ingreso)>='{_fechaInicio}' AND date(fecha_salida)<='{_fechaFin}'"
                        datos=datos.ConsultaEmpleados(completar)
                    elif(_fechaInicio):
                        completar=f"WHERE empleados.area ='{_area}' AND date(fecha_ingreso)>='{_fechaInicio}'"
                        datos=datos.ConsultaEmpleados(completar)
                    else:
                        completar=f"WHERE empleados.area ='{_area}' AND date(fecha_ingreso)>='{_fechaFin}'"
                        datos=datos.ConsultaEmpleados(completar)
            else:
                completar=f"WHERE empleados.area ='{_area}'"
                datos=datos.ConsultaEmpleados(completar)
        elif(_fechaInicio or _fechaFin):
                    if(_fechaInicio and _fechaFin):
                        completar=f"WHERE date(fecha_ingreso)>='{_fechaInicio}' AND date(fecha_salida)<='{_fechaFin}'"
                        datos=datos.ConsultaEmpleados(completar)
                    elif(_fechaInicio):
                        completar=f"WHERE date(fecha_ingreso)>='{_fechaInicio}'"
                        datos=datos.ConsultaEmpleados(completar)
                    else:
                        completar=f"WHERE date(fecha_ingreso)>='{_fechaFin}'"
                        datos=datos.ConsultaEmpleados(completar)
        else:
            completar=""
            datos=datos.ConsultaEmpleados(completar)
    else:
        if(_documento):
            if(_area):
                if(_fechaInicio or _fechaFin):
                    if(_fechaInicio and _fechaFin):
                        completar=f"WHERE visitante.documento = '{_documento}' AND visitante.area ='{_area}' AND date(fecha_ingreso)>='{_fechaInicio}' AND date(fecha_salida)<='{_fechaFin}'"
                        datos=datos.ConsultaVisitante(completar)
                    elif(_fechaInicio):
                        completar=f"WHERE visitante.documento = '{_documento}' AND visitante.area ='{_area}' AND date(fecha_ingreso)>='{_fechaInicio}'"
                        datos=datos.ConsultaVisitante(completar)
                    else:
                        completar=f"WHERE visitante.documento = '{_documento}' AND visitante.area ='{_area}' AND date(fecha_ingreso)>='{_fechaFin}'"
                        datos=datos.ConsultaVisitante(completar)
                else:
                    completar=f"WHERE visitante.documento = '{_documento}' AND visitante.area ='{_area}'"
                    datos=datos.ConsultaVisitante(completar)
            else:
                completar=f"WHERE visitante.documento = '{_documento}'"
                datos=datos.ConsultaVisitante(completar)                
        elif(_area):
            if(_fechaInicio or _fechaFin):
                    if(_fechaInicio and _fechaFin):
                        completar=f"WHERE visitante.area ='{_area}' AND date(fecha_ingreso)>='{_fechaInicio}' AND date(fecha_salida)<='{_fechaFin}'"
                        datos=datos.ConsultaVisitante(completar)
                    elif(_fechaInicio):
                        completar=f"WHERE visitante.area ='{_area}' AND date(fecha_ingreso)>='{_fechaInicio}'"
                        datos=datos.ConsultaVisitante(completar)
                    else:
                        completar=f"WHERE visitante.area ='{_area}' AND date(fecha_ingreso)>='{_fechaFin}'"
                        datos=datos.ConsultaVisitante(completar)
            else:
                completar=f"WHERE visitante.area ='{_area}'"
                datos=datos.ConsultaVisitante(completar)
        elif(_fechaInicio or _fechaFin):
                    if(_fechaInicio and _fechaFin):
                        completar=f"WHERE date(fecha_ingreso)>='{_fechaInicio}' AND date(fecha_salida)<='{_fechaFin}'"
                        datos=datos.ConsultaVisitante(completar)
                    elif(_fechaInicio):
                        completar=f"WHERE date(fecha_ingreso)>='{_fechaInicio}'"
                        datos=datos.ConsultaVisitante(completar)
                    else:
                        completar=f"WHERE date(fecha_ingreso)>='{_fechaFin}'"
                        datos=datos.ConsultaVisitante(completar)
        else:
            completar=""
            datos=datos.ConsultaVisitante(completar)    

    thead= theadVisitante if _visitante =="Visitante" else theadEmpleado
    datos.insert(0,thead)
    return render_template('reportes.html',datos=datos)