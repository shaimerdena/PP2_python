import psycopg2
from config import load_config

def connect(config):
    """ Connect to the book database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect("dbname=book user=postgres password=G0lden_wings222") as conn:
            print('Connected to the book server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    config = load_config()
    connect(config)