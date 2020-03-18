class Person:
    count = 0

    def __init__(self, name, job='None', pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        Person.count += 1

    def __str__(self):
        return ', '.join([f'{key}: {value}'for key, value in self.__dict__.items()])

    def __setattr__(self, key, value):
        if key in self.__dict__.keys():
            print('Пошел вон отсюда нахуй')
        else:
            self.__dict__[key] = value

    def up(self, persent=10):
        self.pay = round(self.pay*(1 + persent/100), 2)

    def __del__(self):
        Person.count -= 1


class Dev(Person):
    count = 0

    def __init__(self, name, pay):
        Person.__init__(self, name, job='dev', pay=pay)
        Dev.count += 1

    def up(self, persent=10, bonus=5):
        Person.up(self, persent+bonus)

    def __del__(self):
        Person.__del__(self)
        Dev.count -= 1


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
    A = Person('Alice', job='man', pay=500)
    B = Dev('Bob', 1000)
    A.name = '1'
    B.name = '2'
    print(A, B)
    Firm = Sotrudniki(A, B)
    print(Firm[1])
    print(len(Firm))
    # import shelve
    Firm.showall()
    # D = Person('Tom', job='sucker', pay=700)
    # db = shelve.open('persondb')
    # for i in A, B, D:
    #     db[i.name] = i
    # for i in db:
    #     print(db[i])
    # Person.a = 1
    # print(A.a)
    # db.close()
    # print()


