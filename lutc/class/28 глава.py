class Super:
    def delegate(self):
        self.action()

    def action(self):
        assert False, 'action must be defined!'


from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    '''мы лишены возможности создавать экземпляры, если метод не будет определен ниже в дереве классов.'''
    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        pass

class Sub(Super):
    def action(self):
        print(1)

x = Sub()
x.delegate()