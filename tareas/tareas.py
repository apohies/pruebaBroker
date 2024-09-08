from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task(name="registrar_log")
def registrar_log(usuario):
    try:
        with open('log_signin.txt', 'a') as file:
            file.write(' Inicio de sesió')
    except Exception as e:
        # Registrar el error en un archivo de log o en algún sistema de monitoreo
        with open('error_log.txt', 'a') as error_file:
            error_file.write('Error: {}\n'.format(e))
        raise e