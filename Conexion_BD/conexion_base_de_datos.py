from sqlite3 import connect, Error
from logging import error

def Conectar_base_de_datos(empresa):
    try:
        conexion = connect(empresa)
        cursor = conexion.cursor()
        return conexion, cursor
    except Error as e:
        error(f'Error al conectar a la base de datos: {str(e)}')
        return None, None
