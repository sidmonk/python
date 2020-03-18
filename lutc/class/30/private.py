class C1:
    def meth1(self):
        self.__X = 88  # Теперь X - мой атрибут


class C2:
    def metha(self):
        self.__X = 99  # И мой тоже


class C3(C1, C2):
    pass


I = C3()  # В I два имени X
I.meth1()
I.metha()
print(I.__dict__)
I.__dict__['_C1__X'] = 87
print(I.__dict__)
I.meth2()
I.methb()
