from config import config
import psycopg2

def connect():
    connection = None
    try:
        params = config()
        print('\nConnecting to postgreSQL Database...\n')
        connection = psycopg2.connect(**params)

        #Create a cursor
        crsr = connection.cursor()
        print('PostSQL database version: ')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connect is not None:
            connection.close()
            print('\nDatabase Connection terminated.\n')
if __name__ == "__main__":
    connect()
