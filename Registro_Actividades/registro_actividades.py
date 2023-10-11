from logging import basicConfig, StreamHandler, INFO, Formatter, getLogger, error
def Registrar_actividades(actividad, archivo_log):
    try:
        # Configurar el registro de eventos en un archivo y en la consola
        basicConfig(filename=archivo_log, level=INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        # Configurar un manejador adicional para mostrar los registros en la consola
        console_handler = StreamHandler()
        console_handler.setLevel(INFO)
        console_formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)

        logger = getLogger()
        logger.addHandler(console_handler)

        logger.info(actividad)  # Registrar la actividad
    except IOError as e:
        error(f'Error al escribir en el archivo de registro: {str(e)}')