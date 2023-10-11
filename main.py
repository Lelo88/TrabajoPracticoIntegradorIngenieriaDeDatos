from Importar_Datos.importar_datos import Importar_desde_json
from Conexion_BD.conexion_base_de_datos import Conectar_base_de_datos
from Creacion_Tablas.creacion_tablas import Crear_tablas
from Insercion_Datos.insercion_datos import Insertar_datos
from Registro_Actividades.registro_actividades import Registrar_actividades
import logging

# Función principal del programa
def main():
    archivo_json = "empresa.json"
    tienda = "empresa.db"
    archivo_log = "registro.txt'"

    datos = Importar_desde_json(archivo_json)
    if datos:
        conexion, cursor = Conectar_base_de_datos(tienda)
        if conexion and cursor:
            try:
                Crear_tablas(conexion, cursor)
                Insertar_datos(conexion, cursor, datos)
                conexion.commit()  # Realiza un commit final
                Registrar_actividades('Proceso completado: Datos importados y almacenados en la base de datos.', archivo_log)
            except Exception as e:
                conexion.rollback()  # Revierte los cambios en caso de error
                logging.error(f'Error durante la operación: {str(e)}')
            finally:
                cursor.close()  # Cierra el cursor
                conexion.close()  # Cierra la conexión
        else:
            Registrar_actividades('No se pudo conectar a la base de datos.', archivo_log)
    else:
        Registrar_actividades('No se pudieron importar los datos desde el archivo JSON.', archivo_log)


if __name__ == '__main__':
    main()