import psycopg2
from os import listdir
import subprocess
import datetime
import error_log

db_updates_path = '.\\db_updates'
db_updates_func = '.\\db_updates_func'

def backup(db, user, date, backup_path):
    try:
        subprocess.run("pg_dump -Fc -b --host=127.0.0.1 -U " + user + " bs  > " + backup_path + "\\" + str(date) + "\\" + str(date) + ".backup",shell=True)
        return
    except (Exception)as error:
        error_log.error_logger('Error in db backup: ' + sys.exc_info()[0])



def update_by_query(db, username, password, version):
    conn = None
    updated_rows = 0
    try:
        conn = psycopg2.connect(database=db,user=username,password=password)
        for filename in listdir(db_updates_path):
            if int(filename) > version:
                with open('.\\db_updates\\'+filename, encoding='utf-8') as f:
                    list_values = list(f.read().split('\n'))
                    for values in list_values:
                        # print(values)
                        cur = conn.cursor()
                        cur.execute(values)
                        updated_rows = cur.rowcount
                        conn.commit()
                        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        with open('.\\error.log', mode='a', encoding='utf-8') as e:
            e.write(values)
            e.write(str(error))
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
    return updated_rows

def update_db_func(db,username, password):
    conn = None
    updated_rows = 0
    try:
        conn = psycopg2.connect(database=db,user=username,password=password)
        for filename in listdir(db_updates_func):
            with open('.\\db_updates\\'+filename, encoding='utf-8') as f:
                list_values = f.read()
                print(list_values)
                cur = conn.cursor()
                cur.execute(list_values)
                updated_rows = cur.rowcount
                conn.commit()
                cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        with open('.\\error.log', mode='a', encoding='utf-8') as e:
            e.write(str(error))
            print(error)
    finally:
        if conn is not None:
            conn.close()
    