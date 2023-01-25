import datetime
date = str(datetime.datetime.now())[:10] + '_' + str(datetime.datetime.now())[11:19]

results = 'These are the results for the test run on ' + date + '.'
print('test.py has been executed')

with open(date + '.log', 'w') as logFile:
  logFile.write(results)