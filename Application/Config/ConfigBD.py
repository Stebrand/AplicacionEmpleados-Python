import sqlite3 as sql

db_path = "Application/Config/DataBase.db" 

class ConfigBaseDatos:

    def __init__(self):
        self.conexion = sql.connect(db_path)
        self.cursor = self.conexion.cursor()
      