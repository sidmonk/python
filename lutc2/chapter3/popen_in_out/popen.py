import os

pipe = os.popen('python hello-in.py', 'w')  # записали в pipe программу
pipe.write('Shk')   # это сработало как input проги hello-in, которая сейчас живет в pipe
pipe.close()    # pipe запустился
print(open('hello-in.txt').read()) # что и требовалось доказать