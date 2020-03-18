"""
- Любой объект, обладающий методами чтения, может быть присвоен переменной sys.stdin, в результате чего
  стандартный ввод будет осуществляться через методы чтения этого объекта

- Любой объект, обладающий методами записи, может быть присвоен переменной sys.stdout, в результате чего
  стандартный вывод будет осуществляться через методы чтения этого объекта

  Функции print и input просто вызывают методы write и readline объектов, на которые ссылаются sys.stdout
  и sys.stdin, мы можем генерировать и перехватывать стандартные потоки с помощью объектов, реализованных
  с помощью классов
"""

import sys

class Output:
    def __init__(self):
        self.text = ''

    def write(self, string: str):
        self.text += string

    def writelines(self, lines):
        for line in lines:
            self.write(line)

class Input:
    def __init__(self, input=''):
        self.text = input

    def read(self, size=None):
        if size == None:
            rez, self.text = self.text, ''
        else:
            rez, self.text = self.text[:size], self.text[size:]
        return rez

    def readline(self):
        eoln = self.text.find('\n')
        if eoln == -1:
            rez, self.text = self.text, ''
        else:
            rez, self.text = self.text[:eoln+1], self.text[eoln+1:]
        return rez

def redirect(function, pargs=(), kargs={}, input=''):    # перенаправляет stdin/out
    savestreams = sys.stdin, sys.stdout
    sys.stdin = Input(input)
    sys.stdout = Output()
    try:
        result = function(*pargs, **kargs)
        output = sys.stdout.text
    finally:
        sys.stdin, sys.stdout = savestreams
    return (result, output)

