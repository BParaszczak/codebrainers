# program wyświetla aktualną datę i godzinę

import datetime

now = datetime.datetime.now()

print('Current date and time:')
print(now.strftime('%Y-%m-%d %H:%M:%S'))
