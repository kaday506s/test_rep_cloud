
class A:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def print(self):
        print('CLASS, ', self.__class__)
        print(self)
        print(self.name)

    def __int__(self):
        return 1


class B(A):

    def __int__(self):
        return 2


print('--- class A ---')
a = A(name='name1')
a.print()

print('--- class B ---')
b = B(name='name2')
b.print()
