class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна:')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно:')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'{self.a} + {self.b} * i'


z1 = ComplexNumber(1, -2)
z2 = ComplexNumber(3, 4)
print(f'z1 = {z1},\nz2 = {z2}')
print(z1 + z2)
print(z1 * z2)
###test