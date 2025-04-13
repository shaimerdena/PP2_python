import psycopg2
from config import load_config

def deleting(name):

    config = load_config()
    rows_deleted = 0
    sql = 'DELETE FROM phonebook WHERE first_name = %s'

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name,))
                rows_deleted = cur.rowcount

            conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return rows_deleted
    
name = input("Enter a name of the user that you wanna delete: ")
if __name__ == "__main__":
    deleted_rows = deleting(name)
    print('The number of deleted rows: ', deleted_rows)