import psycopg2
from os import listdir

version = 490
mypath = '.\\db_updates'



def update_db(db,username, password ):
    conn = None
    updated_rows = 0
    try:
        conn = psycopg2.connect(database=db,user=username,password=password)
        for filename in listdir(mypath):
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


if __name__ == '__main__':
    # 
    result = update_db('kaplicka', 'postgres', 'postgres')
    print(result)