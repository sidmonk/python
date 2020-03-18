from subprocess import PIPE, Popen

pipe = Popen('python reader.py', stdin=PIPE, stdout=PIPE)
pipe.stdin.write(b'Pidor\n')
pipe.stdin.write(b'12\n')
pipe.stdin.close()  # обязательно закрыть
out = pipe.stdout.read()
pipe.wait()
print(out)

p1 = Popen('python writer.py', stdout=PIPE)
p2 = Popen('python reader.py', stdin=p1.stdout, stdout=PIPE)
output = p2.communicate()[0]
print(output)
p2.returncode