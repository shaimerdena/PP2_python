import psycopg2
from config import load_config

def inserting(first_name, last_name, phone_number):
    sql = '''INSERT INTO phonebook(first_name, last_name, phone_number)
            VALUES(%s, %s, %s) RETURNING user_id;
    '''
    user_id = None
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (first_name, last_name, phone_number,))
                rows = cur.fetchone()
                if rows:
                    user_id = rows[0]
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return user_id
    
first_name = input("First name: ")
last_name = input("Last name: ")
phone_number = int(input("Phone number: "))
if __name__ == '__main__':
    inserting(first_name, last_name, phone_number)