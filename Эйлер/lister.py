lister.py
class ListInstance:

    def __str__(self):
        return '<Instance of {}, address {}:\n{}>'.format(self.__class__.__name__, id(self), self.__attrnames())

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__): # Словарь атрибутов
            result += '\tname {}={}\n'.format(attr, self.__dict__ [attr])
        return result