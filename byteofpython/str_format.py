age = 26
name = 'Swaroop'
print('Возраст {0} -- {1} лет.'.format(name, age))
print('Почему {0:10} забавляется с этим Python?'.format(name))
print('{:05}'.format(3))
print('{:*^11}'.format('hello'))

person = {'f':'Reuven', 'l':'Lerner', 's':'T'}
print("Good morning, {f} {l}".format(**person))

a = 5
b = 10
print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')
#
# def greet(name, question):
#     return f"Hello, {name}! How's it {question}? Give me a name."
# print(greet('Bob', 'going'))
#
# from string import Template
# t = Template('Ok. Now my name is $name!')
# print(t.substitute(name=input()))

s = 'Это строка. \
Это строка продолжается.'
print(s)



