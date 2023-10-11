from sqlite3 import Error
from logging import error
def Insertar_datos(conexion, cursor, datos):
    datos_empleados = [(item["nombre"], item["apellido"], item["cargo"], item["edad"], item["departamento_id"]) for item in datos["empleados"]]
    datos_departamento = [(item["nombre"],) for item in datos["departamento"]]
    datos_proyectos = [(item["nombre"],) for item in datos["proyectos"]]
    datos_tareas = [(item["descripcion"], item["proyecto_id"], item["empleado_id"]) for item in datos["tareas"]]
    try:
        cursor.executemany('INSERT INTO empleados (nombre, apellido, cargo, edad, departamento_id) VALUES (?, ?, ?, ?, ?)', datos_empleados)
        cursor.executemany('INSERT INTO departamento (nombre) VALUES (?)', datos_departamento)
        cursor.executemany('INSERT INTO proyectos (nombre) VALUES (?)', datos_proyectos)
        cursor.executemany('INSERT INTO tareas (descripcion, proyecto_id, empleado_id) VALUES (?, ?, ?)', datos_tareas)
        # Inserta datos en las otras dos tablas aquí
        conexion.commit()
    except Error as e:
        conexion.rollback()  # Revierte los cambios en caso de error
        error(f'Error al insertar datos en la base de datos: {str(e)}')