url = input('URL 입력: ')
title = input('바로가기 파일 이름 입력: ')

with open(title + '.url', 'w') as f:
    f.write('[InternetShortcut]\n')
    f.write('URL=' + url)

print('바로가기 생성완료.')
