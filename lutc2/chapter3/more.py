import sys

def getreply():
    """
    читает клавиишу, нажатую пользователем, даже если
    stdin перенаправлен в файл или канал
    """
    if sys.stdin.isatty():      # если stdin связан с консолью
        return input('?')       # читать ответ stdin
    else:
        if sys.platform[:3] == 'win':
            import msvcrt
            msvcrt.putch(b'?')
            key = msvcrt.getch()
            msvcrt.putch(b'\n')
            return key
        else:
            assert False, 'platform not suported'

def more(text, numlines=15):
    """
    построчный вывод содержимого строки в stdout
    при запуске вместе с аргументом коммандной строки интерактивно будет пролистывать текст указанного файла
    """
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and getreply() not in (b'y', b'Y'):
            break

if __name__ == '__main__':
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read())