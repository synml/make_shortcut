pyinstaller -F make_shortcut.py
move dist\\make_shortcut.exe
rmdir /s /q build dist
del make_shortcut.spec
