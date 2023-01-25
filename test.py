import datetime
date = str(datetime.datetime.now())[:19]

results = 'These are the results for the test run on ' + date + '.'
print('test.py has been executed')

with open(date + '_log.txt', 'w') as logFile:
  logFile.write(results)