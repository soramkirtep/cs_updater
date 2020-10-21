import subprocess
import time
import os
import win32serviceutil


# Get service version and data
def get_service(name):
  '''
  service lookup, param str: [service name]
  '''
  try:
      lookup_service = str(subprocess.check_output('sc query state=all | find "SERVICE_NAME: ' + name +'"', shell=True))
      if not lookup_service:
        return ('There is not ' + name + ' service installed')
      service_name = lookup_service.split()[1]
      service = service_name.split('\\')[0]
      return service
  except(Exception) as error:
    logging.exception('Get service err: ')
    print(error)

def service_status(service):
  '''
  param str: [service name]
  returns 1 = stopped, 2 = start pending, 3 = stopped pending, 4 = running, 
  '''
  status = win32serviceutil.QueryServiceStatus(service)[1]
  return status

def start_service(service):
  '''
  param str: [service name]
  '''
  subprocess.run('net start '+ service)

def stop_service(service):
  '''
  param str: [service name]
  stops the service with all dependent services
  '''
  subprocess.run('net stop '+ service +' /yes')   

# Get PID of given process name
def get_pid(process_name):
  try:
    lookup_process = str(subprocess.check_output('tasklist | find "'+ process_name + '"', shell=True))
    if lookup_process != 1:
      result = lookup_process.split()[1]
      return result
    else:
      print("There is not running any process with name " + process_name)
  except(Exception) as error:
    logging.exception('Get PID err: ')
    print(error)

# Check connection on port
def check_connection(process_id):
  try:
    connection = str(subprocess.call('netstat -ano | find ":8093" | find "' + process_id + '"', shell=True))    
    if connection != "1":
      DEPLOY_LOOP = 0
      while DEPLOY_LOOP < 90:
        connection_state = str(subprocess.check_output('netstat -ano | find ":8093" | find "' + process_id + '"', shell=True))
        print(connection_state.split()[-3])
        if connection_state.split()[-3] != "0.0.0.0:0":
          print('Connection has been established on IP ' + connection_state.split()[-3])
          break
        time.sleep(10)
        DEPLOY_LOOP += 1
        print('Connection is not established yet, loop number ' + str(DEPLOY_LOOP) + ' of 20 attempts.')
    else:
      print('Communication was not established with clubspire process ' + process_id)
      return connection
  except(Exception) as error:
    logging.exception('Check connection err: ')
    print(error)

