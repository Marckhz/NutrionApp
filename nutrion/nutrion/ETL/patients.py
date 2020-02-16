import psycopg2
import csv
import sys

def populate(csvfile,table_name):
    try:
        conn = psycopg2.connect("dbname=nutrionapp user=marck")
        cur = conn.cursor()

        cur.copy_from(csvfile, table_name,sep=',')

    except ValueError:
        print("Error al insertar archivo")
    finally:
        conn.commit()
        cur.close()
        conn.close()

def reader_csv(data, table_name):
    with open(data) as csvfile:
        #reader = csvfile.readlines()
        populate(csvfile, table_name )

if __name__ == '__main__':
    reader_csv( sys.argv[1], sys.argv[2] )
