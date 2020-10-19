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

backup_folder = jboss_home +'\\..\\Updates' + '\\' + str(this_date)
if not os.path.exists(backup_folder):
    os.mkdir(backup_folder)


folders_location = [path_to_folders+folder for folder in folders] 
    
# for item in folders_location:
#     shutil.move(item, backup_folder)   

print(backup_folder)
print(folders_location)


# if __name__ == '__main__':
    # 
    # result = update_db('kaplicka', 'postgres', 'postgres')
    # print(result)