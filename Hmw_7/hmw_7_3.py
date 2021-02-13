class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return (self.quantity * "*")

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print(None)

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))


    def make_order(self, cells_in_line):
        line = ''
        for i in range(int(self.quantity / cells_in_line)):
            line += f'{"*" * cells_in_line} \n'
        line += f'{"*" * (self.quantity % cells_in_line)}'
        return line

cells_1 = Cell(17)
cells_2 = Cell(6)
print(f'Cells:\n{cells_1}')
print(f'Сумма:\n{cells_1 + cells_2}')
print(f'Вычитание:\n{cells_1 - cells_2}')
print(cells_2.make_order(3))
print(cells_1.make_order(7))
print(f'Деление:\n{cells_1 / cells_2}')
#test