import psycopg2

def conectar():
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='admin',
            database='db-tareas'
         
        )
    
    except psycopg2.Error as ex:  
        print('Error al conectar:', ex)

