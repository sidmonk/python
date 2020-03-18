"""
С помощью этого модуля можно создавать двунаправленные потоки обмена данными и связывать вывод одной программы
с вводом другой
"""

from subprocess import Popen, PIPE, call

X = call('python hello-out.py')     # функция-обертка
print(X)

X = Popen('python hello-out.py')
X.communicate()[0]      # отправляет данные в stdin, читает данные из (stdout, stderr)
X.returncode    # код завершения

X = Popen('python hello-out.py', stdout=PIPE)   # подключились к stdout
print(X.stdout.read())
X.wait()    # код завершения

pipe = Popen('python hello-in.py', stdin=PIPE)      # подключились к stdin
pipe.stdin.write(b"SIDMONKUS")  # записали b строку
pipe.stdin.close()
pipe.wait()
print(open('hello-in.txt').read())