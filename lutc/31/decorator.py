class dec:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args,):
        self.count += 1
        print(f'{self.func}{args}, call: {self.count}')


@dec
def printer(*a):
    print(*a)

printer(1, 2, 3)
printer(1, 3)
printer(2)