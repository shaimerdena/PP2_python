import psycopg2
from config import load_config

def creating_table():
    '''Create tables in the book database'''
    command = (
    '''
    CREATE TABLE phonebook(
        user_id SERIAL PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL, 
        last_name VARCHAR(255),
        phone_number BIGINT NOT NULL)
    '''
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    creating_table()