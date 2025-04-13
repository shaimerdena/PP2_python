import psycopg2
from config import load_config

#updating a first name
def updating_first_name(user_id):
    name = input("Enter a new name: ")
    updated_row_count = 0

    sql = '''UPDATE phonebook
             SET first_name = %s
             WHERE user_id = %s'''
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, user_id))
                updated_row_count = cur.rowcount
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count


#updating a last name
def updating_last_name(user_id):
    last_name = input("Enter a new last name: ")
    updated_row_count = 0

    sql = '''UPDATE phonebook
             SET last_name = %s
             WHERE user_id = %s'''
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (last_name, user_id))
                updated_row_count = cur.rowcount
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count

    
#updating a phone number
def updating_phone(user_id):
    phone = input("Enter a new phone number: ")
    updated_row_count = 0

    sql = '''UPDATE phonebook
             SET phone_number = %s
             WHERE user_id = %s'''
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (phone, user_id))
                updated_row_count = cur.rowcount
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count

    
update = input("What do you wanna update? type 'first_name', 'last_name' or 'phone_number': ")
id = int(input("Enter a user id you wanna change: "))
if __name__ == "__main__":
    if update == 'first_name':
        updating_first_name(id)
    if update == 'last_name':
        updating_last_name(id)
    if update == 'phone_number':
        updating_phone(id)
    else:
        print("Invalid option. Try again.")