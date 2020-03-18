from math import sqrt


class Compl:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        if self.y == 1:
            return f'{self.x} + i'
        elif self.y == -1:
            return f'{self.x} - i'
        elif self.y > 0:
            return f'{self.x} + {self.y}i'
        elif self.y < 0:
            return f'{self.x} - {abs(self.y)}i'
        else:
            return f'{self.x}'

    def abs(self):
        return round(sqrt(self.x**2 + self.y**2), 2)

    def __add__(self, other):
        if isinstance(other, Compl):
            return Compl(self.x + other.x, self.y + other.y)
        elif isinstance(other, float) or isinstance(other, int):
            return Compl(self.x + other, self.y)
        else:
            raise TypeError

    def __radd__(self, other):
       return Compl.__add__(self, other)

    def __sub__(self, other):
        return Compl.__add__(self, (-1)*other)

    def __rsub__(self, other):
        return Compl.__add__(self, (-1)*other)

    def __mul__(self, other):
        if isinstance(other, Compl):
            return Compl(self.x*other.x - self.y*other.y, self.y*other.x + self.x*other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Compl(self.x * other, self.y * other)
        else:
            raise TypeError

    def __rmul__(self, other):
        return Compl.__mul__(self, other)

    def __eq__(self, other):
        if isinstance(other, Compl):
            return self.x == other.x and self.y == other.y
        else:
            return self.x == other


if __name__ == '__main__':
    A = Compl(1, 0)
    B = Compl(1, 1)
    B *= -1
    print(2-B)