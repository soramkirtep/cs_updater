import db_update
import move_cs_folders


move_cs_folders.move_to_backup()
move_cs_folders.move_from_update()

# if __name__ == '__main__':
    # 
    # result = update_db('kaplicka', 'postgres', 'postgres')
    # print(result)