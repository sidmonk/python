class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    def __repr__(self):
        return f'[{self.value}, {self.next}]'

class LinkedList:
    def __init__(self, *a):
        self.lenth = 0
        self.first = None
        self.last = None
        self.append(*a)

    def __repr__(self):
        if self.first != None:
            current = self.first
            out = [str(current.value)]
            while current.next != None:
                current = current.next
                out.append(str(current.value))
            return '[' + ', '.join(out) + ']'
        return '[]'

    def clear(self):
        self.__init__()

    def append(self, *a):
        for i in a:
            self.lenth += 1
            if self.first == None:
                self.last = self.first = Node(i, None)
            else:
                self.last.next = Node(i, None)
                self.last = self.last.next

    def rappend(self, *a):
        for i in a[::-1]:
            if self.first == None:
                self.last = self.first = Node(i, None)
            else:
                self.first = Node(i, self.first)

    def __insert1(self, i, x):
        if self.first == None:
            self.last = self.first = Node(x, None)
            return
        if i == 0:
            self.rappend(x)
            return
        if i >= len(self):
            self.append(x)
            return
        curr = self.first
        count = 0
        while curr != None:
            count += 1
            if count == i:
                curr.next = Node(x, curr.next)
                self.lenth += 1
                break
            curr = curr.next

    def insert(self, i, *a):
        for j in a:
            self.__insert1(i, j)
            i += 1

    def __len__(self):
        return self.lenth

    def remove(self, i=0):
        if self.first == None:
            return
        if i >= len(self) or i < 0:
            raise IndexError
        curr = self.first
        if i == 0:
            self.first = curr.next
            return
        count = 0
        while curr != None:
            if count == i:
                old.next = curr.next
                break
            old = curr
            curr = curr.next
            count += 1


if __name__ == '__main__':
    a = LinkedList(5, 6, 8, 10)
