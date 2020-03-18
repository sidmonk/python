class Person:
    def __init__(self, name, job='None', pay=0):
        self.name = name
        self.job = job
        self.pay = pay


    def __str__(self):
        return ', '.join([f'{key}: {value}'for key, value in self.__dict__.items()])


    def up(self, persent=10):
        self.pay = round(self.pay*(1 + persent/100), 2)




class Dev(Person):
    count = 0

    def __init__(self, name, pay=1100):
        Person.__init__(self, name, job='dev', pay=pay)
        Dev.count += 1

    def up(self, persent=10, bonus=5):
        Person.up(self, persent+bonus)


class Dev1:
    """Делегирование."""

    count = 0

    def __init__(self, name, pay):
        self.person = Person(name, job='dev', pay=pay)
        Dev1.count += 1

    def __getattr__(self, item):
        return getattr(self.person, item)

    def up(self, persent=10, bonus=5):
        self.person.up(persent+bonus)

    def __str__(self):
        return ', '.join([f'{key}: {value}'for key, value in self.__dict__.items()])


class Sotrudniki:
    count = 0

    def __init__(self, *args):
        Sotrudniki.count += len(args)
        self.sotr = list(args)

    def __getitem__(self, item):
        return self.sotr[item]

    def __len__(self):
        return len(self.sotr)

    def append(self, *new):
        for i in new:
            print(f'{i.name} - наш новый сотрудник')
            Sotrudniki.count += 1
        self.sotr += list(new)

    def up(self, *args):
        if len(args) == 0:
            args = self.sotr
        for i in self.sotr:
            if i in args:
                i.up()

    def showall(self):
        print('Сотрудники:')
        for i in self:
            print(i)

    def uvol(self, *args):
        for i in args:
            if i in self.sotr:
                print(f'{i.name} - уволен')
                self.sotr.remove(i)
                Sotrudniki.count -= 1

    @staticmethod
    def houmany():
        print(Sotrudniki.count)


if __name__ == '__main__':
    a = Person('Bob', 'Manager', 1000)

    b = Person('Alice', 'Shalava', 1500)

    import shelve


    with shelve.open('per') as db3:
        db3[a.name] = a
        db3[b.name] = b

    # with shelve.open('per') as db3:
    #     fields = ('name', 'job', 'pay')
    #     while True:
    #         key = input('key => ')
    #         if not key:
    #             break
    #         elif key in db3.keys():
    #             record = db3[key]
    #         else:
    #             record = Person(name='?')
    #         for field in fields:
    #             curr_value = getattr(record, field)
    #             new_value = input('\t{} = {}\n\t\tnew? => '.format(field, curr_value))
    #             if new_value:
    #                 setattr(record, field, new_value)
    #             db3[key] = record
    #
    # with shelve.open('per') as db3:
    #     for key in db3.keys():
    #         print(db3[key])

