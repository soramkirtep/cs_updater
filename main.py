import db_handler
import move_cs_folders
import service_handler
import configparser
import logging
import logging.config
import datetime
import os
import sys
import error_log


logging.config.fileConfig("logging.conf")
logging.info("Getting data from configuration file")
conf = configparser.ConfigParser()
conf.read('main.conf')

TODAY = datetime.date.today()
JBOSS_HOME = os.environ['JBOSS_HOME']

CS_SERVER_BACKUP = JBOSS_HOME + '\\..\\Updates'
CS_SERVER_OLD = JBOSS_HOME + '\\server\\default\\deploy\\'
CS_SERVER_NEW = '..\\update\\data\\jboss\\'
OLD_CLIENT = JBOSS_HOME + '\\..\\client'
NEW_CLIENT = '..\\update\\data\\files\\client'

FOLDERS = ['Clubspire.ear', 'ovladani.sar', 'ovladaniVstupu.sar']
OLD_FILES_PATH = [CS_SERVER_OLD + folder for folder in FOLDERS]

DB_NAME = conf.get('database', 'name')
DB_USER = conf.get('database', 'user')
DB_PASSWORD = conf.get('database', 'password')
CS_VERSION = conf.get('server', 'version')

SERVICE = 'clubspire'
JBOSS_PROCESS = 'JBossService.exe'
CONNECTION_LOOP = 0
CONNECTION_LOOP2 = 0

if __name__ == '__main__':
    try:
        # logging.info("Stopping clubspire service and dependent services.")
        # status = service_handler.service_status(SERVICE)
        # if status == 4:
        #     # Restart WC to run on http
        #     service_handler.stop_service(SERVICE)
        # else:
        #     print(f'{SERVICE} is already stopped')
        #     logging.info(f'{SERVICE} is already stopped')
        
        # logging.info("Creating backup folder with actual date.")
        # if not os.path.exists(CS_SERVER_BACKUP):
        #     os.mkdir(CS_SERVER_BACKUP)
        # if not os.path.exists(CS_SERVER_BACKUP + '\\' + str(TODAY)):
        #     os.mkdir(CS_SERVER_BACKUP + '\\' + str(TODAY))    
        
        # logging.info("Creating db backup")
        # db_handler.backup(DB_NAME, DB_USER, TODAY, CS_SERVER_BACKUP)

        # logging.info("Moving CS server to backup folder with actual date...")
        # move_cs_folders.move_to_backup(CS_SERVER_BACKUP, TODAY, OLD_FILES_PATH)

        # logging.info("Updating cs server...")
        # move_cs_folders.move_from_update(CS_SERVER_NEW, FOLDERS, CS_SERVER_OLD) 

        # logging.info("Moving CS client to backup folder with actual date...")
        # move_cs_folders.move_old_client(OLD_CLIENT, CS_SERVER_BACKUP, TODAY, OLD_FILES_PATH)

        # logging.info("Updating CS client...")
        # move_cs_folders.move_new_client(NEW_CLIENT, JBOSS_HOME)
# no ok
        # values need to be assigned here before func.call
        db_handler.update_by_query(DB_NAME, DB_USER, DB_PASSWORD, CS_VERSION)
        # db_update.db_func(DB_NAME, DB_USER, DB_PASSWORD)




        # Checking clubspire if running.
        # CLUBSPIRE_SERVICE = get_service('clubspire')
        # if service_status(CLUBSPIRE_SERVICE) == 1: 
        #     print("Clubspire is stopped, starting Clubspire...")
        #     print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
        #     while CONNECTION_LOOP < 20:
        #     start_service('clubspire')
        #     time.sleep(10)
        #     clubspire_process_id = get_pid(JBOSS_PROCESS)
        #     established = check_connection(clubspire_process_id)
        #     if established == "1":
        #         print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
        #         stop_service('clubspire')
        #     else:
        #         break
        #     CONNECTION_LOOP += 1
        #     print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
        #     print('Loop restarting clubspire ended successfully...')
        #     # Starting Webclient
        #     start_service('clubspire-webclient')
        #     print('All services are running properly now.')
        # elif service_status(CLUBSPIRE_SERVICE) == 4:
        #     print('Clubspire service is running, verify is comunication is ok.')
        #     while CONNECTION_LOOP2 < 20:
        #     clubspire_process_id = get_pid(JBOSS_PROCESS)
        #     established = check_connection(clubspire_process_id)
        #     if established == "1":
        #         print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
        #         stop_service('clubspire')
        #         time.sleep(10)
        #         start_service('clubspire')
        #     else:
        #         break
        #     CONNECTION_LOOP2 += 1
        #     print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
        # print('Loop restarting clubspire ended successfully...')
        # # Starting Webclient
        # start_service('clubspire-webclient')
        # print('All services are running properly.')
    except(Exception) as error:
        print(error)
        error_log.error_logger(error)   