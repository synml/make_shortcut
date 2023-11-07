import os
import random

while True:
    file_name = f'link_{str(random.randint(0, 100000)).zfill(6)}.url'
    if not os.path.exists(file_name):
        break

url = input('URL 입력: ')
with open(file_name, 'w') as f:
    f.write('[InternetShortcut]\n')
    f.write(f'URL={url}')
