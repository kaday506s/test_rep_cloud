
class A:

    TEXT_MSG = "TEXT"

    def __init__(self, a, b):
        self.name_a = a
        self.name_b = b

        print('init')

    def plus(self):
        return self.name_a + self.name_b

    def print_custom_value(self, value):
        value += 1
        return value

    @classmethod
    def get_msg(cls):
        return cls.TEXT_MSG


class_a = A(a=1, b=2)

print('------------')
print(class_a.plus())
