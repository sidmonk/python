import os

# выполнить команду
os.system('python helloworld.py')
# перехват вывода команды
out = os.popen('python helloworld.py').read()
print(out)

# обеспечивает больше возможностей
import subprocess
# как os.system
subprocess.call(r'python helloworld.py')
# добавление "start" делает процесс независимым
subprocess.call(r"start python helloworld.py", shell=True)    # shell for Linux
print('q')

pipe = subprocess.Popen("python helloworld.py", stdout=subprocess.PIPE)
print(pipe.stdout.read())
print(pipe.communicate()[0])

# открыть файл
os.startfile('text.txt')
