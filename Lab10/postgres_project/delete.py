import psycopg2
from config import load_config


def delete_part(vendor_id):
    """ Delete part by vendor id """

    rows_deleted  = 0
    sql = 'DELETE FROM vendors WHERE vendor_id = %s'
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (vendor_id,))
                rows_deleted = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return rows_deleted

num = int(input('Input an id of a vendor that you wanna delete: '))
if __name__ == '__main__':
    deleted_rows = delete_part(num)
    print('The number of deleted rows: ', deleted_rows)