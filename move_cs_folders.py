import db_update
import shutil
import os
import datetime

this_date = datetime.date.today()
folders = ['Clubspire.ear', 'ovladani.sar', 'ovladaniVstupu.sar']

jboss_home = os.environ['JBOSS_HOME']
cs_server_old = jboss_home + '\\server\\default\\deploy\\'
cs_server_new = '..\\update\\data\\jboss\\'
old_files_path = [cs_server_old+folder for folder in folders]

def move_to_backup():
    try:
        if not os.path.exists(jboss_home +'\\..\\Updates'):
            os.mkdir(jboss_home +'\\..\\Updates')
        if not os.path.exists(jboss_home +'\\..\\Updates' + '\\' + str(this_date)):
            os.mkdir(jboss_home +'\\..\\Updates' + '\\' + str(this_date))    
        for item in old_files_path:
            shutil.move(item, jboss_home +'\\..\\Updates' + '\\' + str(this_date))
    except(Exception) as error:
        print(error) 

def move_from_update():
    try:
        folders_location = [cs_server_new+folder for folder in folders]   
        for item in folders_location:
            shutil.move(item, cs_server_old)
    except(Exception) as error:
        print(error)