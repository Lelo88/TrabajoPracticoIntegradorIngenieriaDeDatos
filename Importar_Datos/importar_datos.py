from json import load, JSONDecodeError
from logging import error
def Importar_desde_json(archivo_json):
    try:
        with open(archivo_json, 'r') as archivo_json:
            datos = load(archivo_json)
        return datos
    except FileNotFoundError:
        error(f'El archivo {archivo_json} no se encuentra.')
        return None
    except JSONDecodeError:
        error(f'Error al decodificar el archivo JSON: {archivo_json}')
        return None