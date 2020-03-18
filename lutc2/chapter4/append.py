open('data.txt', 'a').write('q\n')   #append запишет сразу в конец
with open('data.txt', 'r+') as f:   #read + write
    f.seek(0, 2)    # прыгнуть на нулевую позицию от конца файла
    f.write('Sid')