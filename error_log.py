def error_logger(error):
  with open('.\\error.log', mode='a', encoding='utf-8') as e:
    e.write('Error: ' + str(error))
  