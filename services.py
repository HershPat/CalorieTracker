from config import config
import psycopg2
from psycopg2 import pool

connection_pool = None

"""Initialize connection pool to PostgreSQL database"""
def init_pool():
    global connection_pool
    try:
        params = config()
        print('\nInitializing PostgreSQL connection pool...\n')
        minPool = 5
        maxPool = 20
        connection_pool = pool.SimpleConnectionPool(minPool, maxPool, **params)
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error creating connection pool: {error}")
        
"""Get connection from pool"""
def connect():
    global connection_pool
    if connection_pool is None:
        connection_pool = init_pool()
    try:
        return connection_pool.getconn()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error getting connection from pool: {error}")
        return None

"""Return connection to pool"""
def disconnect(connection):
    global connection_pool
    if connection is not None:
        connection_pool.putconn(connection)
        print('\nConnection returned to pool.\n')

"""Close the connection pool"""
def close_pool():
    global connection_pool
    if connection_pool is not None:
        connection_pool.closeall()
        print('\nConnection pool closed.\n')

"""Insert a row into specified table"""
def insert_row(table, columns, values):
    connection = connect()
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO {table} ({','.join(columns)}) VALUES ({','.join(['%s']*len(values))})"
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        print(f"Successfully inserted row into {table}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error inserting row: {error}")
        connection.rollback()
    disconnect(connection)
    
"""Delete row(s) from specified table based on condition"""
def delete_row(table, conditions):
    connection = connect()
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM {table} WHERE {' AND '.join(f"{column} = %s" for column in conditions.keys())}"
        cursor.execute(query, list(conditions.values()))
        connection.commit()
        cursor.close()
        print(f"Successfully deleted row(s) from {table}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error deleting row: {error}")
        connection.rollback()
    disconnect(connection)

"""Read row(s) from specified table based on condition OR all rows"""
def read_row(table, columns=None, conditions=None):
    connection = connect()
    try:
        cursor = connection.cursor()
        if columns and conditions:
            query = f"SELECT {','.join(columns)} FROM {table} WHERE {' AND '.join(f"{column} = %s" for column in conditions.keys())}"
        elif columns:
            query = f"SELECT {','.join(columns)} FROM {table}"
        else:
            query = f"SELECT * FROM {table}"
        cursor.execute(query)
        result = cursor.fetchone()
        print(result)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error reading row: {error}")
        connection.rollback()
    disconnect(connection)

"""Update row(s) in specified table based on condition"""
def update_row(table, updates, conditions):
    connection = connect()
    try:
        cursor = connection.cursor()
        query = f"UPDATE {table} SET {', '.join(f'{column} = %s' for column in updates.keys())} WHERE {' AND '.join(f'{column} = %s' for column in conditions.keys())}"
        cursor.execute(query, list(updates.values()) + list(conditions.values()))
        connection.commit()
        cursor.close()
        print(f"Successfully updated row(s) in {table}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error updating row: {error}")
        connection.rollback()
    disconnect(connection)

"""Main function to test the services"""
if __name__ == "__main__":
    init_pool()
    # insert_row('client', ['first_name', 'last_name', 'client_age', 'client_weight', 'email', 'phone_number'], ['John', 'Doe', 30, 170, 'john@example.com', '1234567890'])
    read_row('client')
    delete_row('client', {'first_name': 'John'})
    read_row('client')
    close_pool()

