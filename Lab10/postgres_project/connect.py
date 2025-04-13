import psycopg2
from config import load_config

def connect(config):
    """ Connect to the labten database server """
    try:
        conn = psycopg2.connect("dbname=labten user=postgres password=G0lden_wings222")
        print('Connected to the PostgreSQL server.')
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    config = load_config()
    connect(config)