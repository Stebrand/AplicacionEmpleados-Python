from Application.Config.ConfigBD import ConfigBaseDatos

class BaseDatos(ConfigBaseDatos):
    def __init__(self):
        super().__init__()
        pass    

    def Crear(self,documento,nombre,dato,tabla):                             
        try:            
            self.cursor.execute("INSERT INTO " + tabla + " VALUES (?,?,?)",(documento,nombre,dato))
            self.conexion.commit()
            self.conexion.close()
        except:
            print("No se pudo crear en base de datos")
            self.conexion.close()
    
    def Leer(self,documento,tabla):
        try:
            self.cursor.execute("SELECT documento FROM " + tabla + " WHERE documento = '" + documento + "'")
            self.consulta = self.cursor.fetchall()
            return self.consulta
        except:
            print("No se encuentra el archivo en base de datos")

    def Modificar(self,documento,nombre,dato,tabla):
        campo = "area" if tabla == "empleados" else "tipo"
        try:
            self.cursor.execute("UPDATE " + tabla + " SET nombre='"+ nombre +"', "+ campo +"='"+ dato +"' WHERE documento = '" + documento + "'")      
            self.conexion.commit()
            self.conexion.close()
        except:
            print("No se puede modificar no existe en base de datos")

    def Borrar(self,documento,tabla):        
        try:
            self.cursor.execute("DELETE FROM "+ tabla +" WHERE documento = '" + documento + "'")
            self.conexion.commit()
            self.conexion.close()            
        except:
            print("No se pudo borrar no exite en base de datos")        

    def Registro(self,documento,fecha,hora,tabla):                                  
        try:
            self.cursor.execute("INSERT INTO "+tabla+" (documento,fecha_ingreso,hora_ingreso) VALUES (?,?,?)",(documento,fecha,hora))
            self.conexion.commit()
            self.conexion.close()            
        except:
            print("Empleado no existe en base de datos registro") 

    def RegistroSalida(self,documento,fecha,hora,tabla):                                
        try:
            self.cursor.execute("SELECT MAX(ID) FROM "+tabla+" WHERE documento = '"+documento+"'")
            id=self.cursor.fetchall()
            self.cursor.execute("UPDATE "+tabla+" SET fecha_salida= '"+fecha+"', hora_salida= '"+hora+"' WHERE documento = '"+documento+"' AND id ='"+str(id[0][0])+"'")
            self.conexion.commit()
            self.conexion.close()            
        except:
            print("Empleado no existe en base de datos registro salida")                       

    def RegistroMotivo(self,documento,fecha,hora,motivo):                        
        try:
            self.cursor.execute("SELECT MAX(ID) FROM registro_empleado WHERE documento = '"+documento+"'")
            id=self.cursor.fetchall()
            self.cursor.execute("UPDATE registro_empleado SET fecha_salida= '"+fecha+"', hora_salida= '"+hora+"',motivo_salida= '"+motivo+"' WHERE documento = '"+documento+"' AND id ='"+str(id[0][0])+"'")
            self.conexion.commit()
            self.conexion.close()            
        except:
            print("Empleado no existe en base de datos ")            

  
