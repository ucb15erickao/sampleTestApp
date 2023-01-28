import datetime
timestamp = str(datetime.datetime.now())[:10] + '_' + str(datetime.datetime.now())[11:19]

import random
totalCount = random.randint(1000, 1080)
passCount = random.randint(888, totalCount)

with open(timestamp + '.log', 'w') as logFile:
  logFile.write('This log file represents the results of running  ' + str(totalCount) + '  tests.\n\n')
  logFile.write('Tests passed:' + '{:>8}'.format(str(passCount)) + '\n')
  logFile.write('Tests failed:' + '{:>8}'.format(str(totalCount - passCount)) + '\n\n\n')
  logFile.write('    <Additional details logged during test run>\n\n\n')
  logFile.write('Test timestamp:  ' + timestamp + '\n')