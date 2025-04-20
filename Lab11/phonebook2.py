import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="book",
    user="postgres",
    password="G0lden_wings222"
)

def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def create_table():
    command =     '''
    CREATE TABLE IF NOT EXISTS phonebook2(
        user_id SERIAL PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL, 
        last_name VARCHAR(255),
        phone_number VARCHAR(20) NOT NULL )
    '''
    try:
        with conn.cursor() as cur:
            cur.execute(command)
            conn.commit()
    except(psycopg2.DatabaseError, Exception) as error:
        print(error)

def get_all_users():
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook2")
            rows = cur.fetchall()
            for row in rows:
                print(row)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def csv_to_table(filepath):
    command = '''
    INSERT INTO phonebook2(first_name, last_name, phone_number) VALUES(%s, %s, %s)
'''
    try:
        with conn.cursor() as cur:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    first_name, last_name, phone_number = row
                    cur.execute(command, (first_name, last_name, phone_number))
                conn.commit()
                print("Data inserted from CSV successfully!")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

# 1st task: function that returns all records based on a pattern
def create_function_find_by_pattern():  
    command = '''
    CREATE OR REPLACE FUNCTION find_by_pattern(pattern TEXT)
    RETURNS TABLE(user_id INTEGER, first_name VARCHAR, last_name VARCHAR, phone_number VARCHAR) AS $$
    BEGIN
    RETURN QUERY 
    SELECT p.user_id, p.first_name, p.last_name, p.phone_number
    FROM phonebook2 p
    WHERE p.first_name ILIKE '%' || pattern || '%'
       OR p.last_name ILIKE '%' || pattern || '%'
       OR p.phone_number ILIKE '%' || pattern || '%';
    END;
    $$
    LANGUAGE plpgsql;
'''
    try:
        with conn.cursor() as cur:
            cur.execute(command)
            conn.commit()
            print("Function created successfully.")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)


def call_find_by_pattern():
    pattern = input("Enter a pattern to search: ")
    query = "SELECT * FROM find_by_pattern(%s);"
    try:
        with conn.cursor() as cur:
            cur.execute(query, (pattern,))
            for row in cur.fetchall():
                print(row)
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


#2nd task: procedure to insert new user by name and phone, update phone if user already exists
create_or_update_procedure = '''   
    CREATE OR REPLACE PROCEDURE add_new(
        new_first_name VARCHAR,
        new_last_name VARCHAR,
        new_phone_number VARCHAR
    ) AS $$
    BEGIN
        IF EXISTS(
            SELECT 1 FROM phonebook2
            WHERE first_name = new_first_name AND last_name = new_last_name
        ) THEN 
            UPDATE phonebook2
            SET phone_number = new_phone_number
            WHERE first_name = new_first_name AND last_name = new_last_name;
        ELSE
            INSERT INTO phonebook2(first_name, last_name, phone_number)
            VALUES(new_first_name, new_last_name, new_phone_number);
        END IF;
    END;
    $$
    LANGUAGE plpgsql;
'''

def call_insert_or_update_user():
    first_name = input("New user's first name: ")
    last_name = input("The user's last name: ")
    phone_number = input("The user's phone number: ")

    try:
        with conn.cursor() as cur:
            cur.execute("CALL add_new(%s, %s, %s)", (first_name, last_name, phone_number))
            conn.commit()
        print("Procedure executed successfully!")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

#3th task: procedure to insert many new users by list of name and phone
inserting_list_of_names_procedure =''' 
    CREATE OR REPLACE PROCEDURE insert_many_users( IN user_list TEXT[][] )
    LANGUAGE plpgsql
    AS $$
    DECLARE
        row TEXT[];
        fname TEXT;
        lname TEXT;
        phone TEXT;
        incorrect_data TEXT[] := ARRAY[]::TEXT[];
    BEGIN
        FOREACH row SLICE 1 IN ARRAY user_list LOOP
        fname := row[1];
        lname := row[2];
        phone := row[3];

        IF phone ~ '^\+?[0-9\-\s]{7,15}$' THEN
            INSERT INTO phonebook2(first_name, last_name, phone_number)
            VALUES (fname, lname, phone);
        ELSE
            incorrect_data := array_append(incorrect_data, fname || ' ' || lname || ' (' || phone || ')');
        END IF;
    END LOOP;

    RAISE NOTICE 'Incorrect data: %', incorrect_data;
END;
$$;
'''

def call_inserting(list_of_users):
    # converting massive into formatted(PostgreSQL list)
    formatted_list = "ARRAY[" + ", ".join(
        ["ARRAY[" + ", ".join(f"'{item}'" for item in user) + "]" for user in list_of_users]
    ) + "]::text[][]"

    # ARRAY[
    # ARRAY['Ali', 'Mukhammed', '+123456789'],
    # ARRAY['Bob', 'Brown', 'wrongnumber'],
    # ARRAY['Bruh', 'Sigma', '88005553535']
    # ]::TEXT[][]

    command = f"CALL insert_many_users({formatted_list})"
    try:
        with conn.cursor() as cur:
            cur.execute(command)
            conn.commit()
            print("Users inserted (or partially skipped) successfully.")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

list_of_users = [
    ['Ali', 'Mukhammed', '+123456789'],
    ['Bob', 'Brown', 'wrongnumber'],
    ['Bruh', 'Sigma', '88005553535']
]

#4th task: function to querying data from the tables with pagination (by limit and offset)
query_with_pagination = '''
        CREATE OR REPLACE FUNCTION quering(li_mit INT, off_set INT)
        RETURNS TABLE(user_id INTEGER, first_name VARCHAR, last_name VARCHAR, phone_number VARCHAR) AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM phonebook2 
            LIMIT li_mit OFFSET off_set;
        END;
        $$
        LANGUAGE plpgsql;
'''

def quering_with_pagination():
    limit = int(input("How many records to show? (limit): "))
    offset = int(input("From which record to start? (offset): "))
    query = '''SELECT * FROM quering(%s, %s)'''
    try:
        with conn.cursor() as cur:
            cur.execute(query, (limit, offset))
            rows = cur.fetchall()
            for row in rows:
                print(row)
            conn.commit()
    except ValueError:
        print("Enter valid numbers.")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

#5th task: procedure to deleting data from tables by username or phone
create_procedure_delete = '''
    CREATE OR REPLACE PROCEDURE deleting(f_name varchar) AS $$
    BEGIN
        DELETE FROM phonebook2 WHERE first_name = f_name;
    END;
    $$
    LANGUAGE plpgsql;
'''
def call_delete_procedure():
    f_name = input("Enter the user's first name to delete: ")
    command = "CALL deleting(%s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (f_name,))
            conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

# create_table()
# csv_to_table(r"C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab11\data.csv")


# get_all_users()

# create_function_find_by_pattern()
# call_find_by_pattern()

# execute_query(create_or_update_procedure)
# call_insert_or_update_user()

# execute_query(inserting_list_of_names_procedure)
# call_inserting(list_of_users)

# execute_query(query_with_pagination)
# quering_with_pagination()

# execute_query(create_procedure_delete)
# call_delete_procedure()

conn.close()