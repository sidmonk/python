def interact():
    print('Hello stream world')     # print выводит в sys.stdout
    while True:
        try:
            reply = input('Enter a number>')    # input читает из sys.stdin
            print()
        except EOFError:
            break       # исключение при встрече символа eof
        else:
            num = int(reply)
            print(f"{num} squared is {num**2}")
    print('Bye')

#     для запуска из консоли python и вывода результата в файл teststreams.py < numbers.txt > result.txt
if __name__ == '__main__':
    interact()