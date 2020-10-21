import psycopg2
from os import listdir
import subprocess
import logging

db_updates = '.\\db_updates'
db_updates_func = '.\\db_updates_func'

def backup(db, user, date, backup_path):
    try:
        subprocess.run("pg_dump -Fc -b --host=127.0.0.1 -U " + user + " bs  > " + backup_path + "\\" + str(date) + "\\" + str(date) + ".backup",shell=True)
        return
    except (Exception)as error:
        logging.exception('Postgres error: ')
        print(error)



def update_by_query(db, username, password, version):
    conn = None
    updated_rows = 0
    try:
        conn = psycopg2.connect(database=db,user=username,password=password)
        for filename in listdir(db_updates):
            if int(filename) > int(version):
                with open(db_updates + '\\' + filename, encoding='utf-8') as f:
                    list_values = list(f.read().split('\n'))
                    # print(list_values)
                    for values in list_values:
                        print(values)
                        # cur = conn.cursor()
                        # cur.execute(values)
                        # updated_rows = cur.rowcount
                        # conn.commit()
                        # cur.close()         
    except (Exception, psycopg2.DatabaseError) as error:
        logging.exception('Postgres error: ')
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return updated_rows

def update_by_file(db,username, password, version):
    conn = None
    updated_rows = 0
    try:
        conn = psycopg2.connect(database=db,user=username,password=password)
        for filename in listdir(db_updates_func):
            if int(filename) > int(version):
                with open(db_updates_func + '\\' + filename, encoding='utf-8') as f:
                    values = f.read()
                    print(values)
                    # cur = conn.cursor()
                    # cur.execute(values)
                    # updated_rows = cur.rowcount
                    # conn.commit()
                    # cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        logging.exception('Postgres error: ')
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return updated_rows