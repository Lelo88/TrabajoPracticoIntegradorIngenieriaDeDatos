from sqlite3 import Error
from logging import error
def Crear_tablas(conexion, cursor):
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT,
                            apellido TEXT,
                            cargo TEXT,
                            edad INTEGER,
                            departamento_id INTEGER
                        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS departamento (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT
                        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS proyectos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT
                        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS tareas (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            descripcion TEXT,
                            proyecto_id INTEGER,
                            empleado_id INTEGER
                        )''')
        # Define las otras dos tablas aquí
        conexion.commit()
    except Error as e:
        error(f'Error al crear tablas en la base de datos: {str(e)}')