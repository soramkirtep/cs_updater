import shutil
import os
import logging

def move_to_backup(backup, date, old_files_path):
    try:
        if not os.path.exists(backup):
            os.mkdir(backup)
        if not os.path.exists(backup + '\\' + str(date)):
            os.mkdir(backup + '\\' + str(date))    
        for item in old_files_path:
            shutil.move(item, backup + '\\' + str(date))
    except(Exception) as error:
        logging.exception('File migration to backup err: ')
        print(error)


def move_from_update(new_server, folders, old_server):
    try:
        folders_location = [new_server+folder for folder in folders]   
        for item in folders_location:
            shutil.move(item, old_server)
    except(Exception) as error:
        logging.exception('File migration from update err: ')
        print(error)


def move_old_client(old_client, backup, date, old_files_path):
    try:
        if not os.path.exists(backup):
            os.mkdir(backup)
        if not os.path.exists(backup + '\\' + str(date)):
            os.mkdir(backup + '\\' + str(date))    
        for item in old_files_path:
            shutil.move(old_client, backup + '\\' + str(date))
    except(Exception) as error:
        logging.exception('Client migration to backup err: ')
        print(error)


def move_new_client(new_client, jboss_home):
    try:
        shutil.move(new_client, jboss_home + '\\..\\')
    except(Exception) as error:
        logging.exception('Client migration from update err: ')
        print(error)