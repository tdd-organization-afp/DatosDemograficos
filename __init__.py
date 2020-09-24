def configure_logging(app):
    # Eliminamos los handlers que puedan existir por defecto
    del app.logger.handlers[:]
    
    # Añadimos el logger por defecto 
    logger = app.logger
    handlers = []
    
    # Creamos un manejador para escribir los mensajes por consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(verbose_formatter())
    handlers.append(console_handler)
    
    # Asociamos cada uno de los handlers a cada uno de los loggers
    for handler in handlers:
        logger.addHandler(handler)
    l.propagate = False
    l.setLevel(logging.DEBUG)
        
def verbose_formatter():
    return logging.Formatter(
        '[%(asctime)s.%(msecs)d]\t %(levelname)s \t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )
    
def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
    # Load the config file specified by the APP environment variable
    app.config.from_object(settings_module)
    # Load the configuration from the instance folder
    if app.config.get('TESTING', False):
        app.config.from_pyfile('config-testing.py', silent=True)
    else:
        app.config.from_pyfile('config.py', silent=True)
    configure_logging(app)
