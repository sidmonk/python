import os
# открывает дескриптор в двоичном режиме для чтения-записи выполняя побитовое ИЛИ над двумя флагами
fdfile = os.open('data.txt', (os.O_RDWR | os.O_BINARY))
print(os.read(fdfile, 100))
os.lseek(fdfile, 0, 0)     # вернуться в начало файла

# обертка дескриптора файла объектом файла
objfile = os.fdopen(fdfile, 'rb')
# дескриптор
print(objfile.fileno())
fdfile = os.open('data.txt', (os.O_RDWR | os.O_BINARY))
objfile = os.fdopen(fdfile, 'r', encoding='latin1', closefd=True)
objfile.seek(0)
print(objfile.read())
objfile.close()

os.chmod('data.txt', 0o777)     # разрешить доступ все пользователям
os.rename('data.txt', 'hui.txt')    # переименовать