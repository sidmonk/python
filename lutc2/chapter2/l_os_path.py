import os

name = r'C:\temp\data.txt'
# отделить имя от каталога
names = os.path.split(name)
print(names)
print(os.path.join(*names))
# получить имя каталога и имя файла по отдельности
print(os.path.dirname(name), os.path.basename(name), sep=' | ')
# получить расширение
print(os.path.splitext(name))
# получить имя диска
print(os.path.splitdrive(name))
# сменить текущую директорию
os.chdir(r'C:\\')
# текущая дериктория
print(os.getcwd())
# полный путь к папке из текущей директории
print(os.path.abspath(r'windows'))
print(os.path.abspath(r''))

