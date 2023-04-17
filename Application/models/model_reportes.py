from Application.Config.ConfigBD import ConfigBaseDatos

class reporteBD(ConfigBaseDatos):

    def __init__(self):
        super().__init__()
        pass

    def ConsultaEmpleados(self,completar):
        consulta="""SELECT empleados.documento, empleados.nombre, empleados.area, registro_empleado.fecha_ingreso, registro_empleado.hora_ingreso, registro_empleado.fecha_salida, registro_empleado.hora_salida, registro_empleado.motivo_salida
                                    FROM empleados 
                                    INNER JOIN registro_empleado 
                                    ON empleados.documento = registro_empleado.documento """+completar                         
        try:
            self.cursor.execute(consulta)
            dato=self.cursor.fetchall()
            self.conexion.commit()
            self.conexion.close()
            return dato           
        except:
            print("Error")

    def ConsultaVisitante(self,completar):
        consulta="""SELECT visitante.documento, visitante.nombre, visitante.tipo, registro_visitante.fecha_ingreso, registro_visitante.hora_ingreso, registro_visitante.fecha_salida, registro_visitante.hora_salida
                                    FROM visitante 
                                    INNER JOIN registro_visitante 
                                    ON visitante.documento = registro_visitante.documento """+completar
        try:
            self.cursor.execute(consulta)
            dato=self.cursor.fetchall()
            self.conexion.commit()
            self.conexion.close()
            return dato           
        except:
            print("Error")                                               