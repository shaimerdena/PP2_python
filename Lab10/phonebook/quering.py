import psycopg2
from config import load_config

def order_by_column(column, order):
    if column not in ['first_name', 'last_name', 'phone_number']:
        print("Invalid column name. Try again.")
        return

    if order == 'a':
        direction = 'ASC'
    elif order == 'd':
        direction = 'DESC'
    else:
        print("Invalid sort order. Try again.")
        return

    query = f'''SELECT * FROM phonebook ORDER BY {column} {direction}'''

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    ordering = input("By which column should the table be sorted? Type 'first_name' or 'last_name' or 'phone_number': ")
    ans = input('In ascending or descending order? Type "a" for ASC or "d" for DESC: ')
    order_by_column(ordering, ans)
