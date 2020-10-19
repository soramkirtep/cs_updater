import db_update
import move_cs_folders

if __name__ == '__main__':
    # move_cs_folders.move_to_backup()
    # move_cs_folders.move_from_update() 
    # result = update_db('kaplicka', 'postgres', 'postgres')
    db_update.db_add_func('kaplicka', 'postgres', 'postgres')