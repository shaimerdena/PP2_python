import psycopg2
import csv
from config import load_config

def inserting(file_path):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(file_path, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader)  #skipping the first row
                    for row in reader:
                        cur.execute(
                            "INSERT INTO phonebook(first_name, last_name, phone_number) VALUES(%s, %s, %s)",
                            (row[0], row[1], int(row[2]))
                        )
                    conn.commit()
                    print("Data inserted from CSV successfully!")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__=='__main__':
    file_path = r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab10\phonebook\data.csv'
    inserting(file_path)      
