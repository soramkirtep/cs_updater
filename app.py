import db_update
import shutil
import os
import datetime


this_date = datetime.date.today()
# version = 487
# mypath = '.\\db_updates'    
# source_dir = '/path/to/source_folder'
# target_dir = '/path/to/dest_folder'
folders = ['Clubspire.ear', 'ovladani.sar', 'ovladaniVstupu.sar']

jboss_home = os.environ['JBOSS_HOME']
path_to_folders = jboss_home + '\\server\\default\\deploy\\'
update_path = '..\\update\\data\\jboss\\'

def move_to_backup():
    try:
        if not os.path.exists(jboss_home +'\\..\\Updates'):
            os.mkdir(jboss_home +'\\..\\Updates')
        if not os.path.exists(jboss_home +'\\..\\Updates' + '\\' + str(this_date)):
            backup_folder = os.mkdir(jboss_home +'\\..\\Updates' + '\\' + str(this_date))


        folders_location = [path_to_folders+folder for folder in folders] 
            
        for item in folders_location:
            shutil.move(item, backup_folder)

    except(Exception) as error:
        print(error)  

# def move_from_update():
#     try:
#          folders_location = [update_path+folder for folder in folders] 
            
#         for item in folders_location:
#             shutil.move(item, path_to_folders)

#     except(Exception) as error:
#         print(error)



move_to_backup()

# if __name__ == '__main__':
    # 
    # result = update_db('kaplicka', 'postgres', 'postgres')
    # print(result)