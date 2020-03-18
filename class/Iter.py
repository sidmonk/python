class SkipIterator:
    def init(self, wrapped):
        self.wrapped = wrapped                          #  Информация  о  состоянии
        self.offset = 0
        
    def next(self):
        if self.offset >= len(self.wrapped):            #  Завершить  итерации
            raise StopIteration
        else:
            item = self.wrapped[self.offset]  #  Иначе  перешагнуть  и  вернуть
        self.offset += 2
        return item

for i in SkipIterator([1, 2, 3, 4, 5, 6]):
    print(i)