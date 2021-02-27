class Storage:
    pass

class OfficeEquipment:
    def __init__(self, type, brand, model, color, price):
        self.type = type
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    def __str__(self):
        return f"{self.type, self.brand, self.model, self.color, self.price}"

class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Printer', *args)

class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Scanner', *args)

class Xerox(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Xerox', *args)

p1 = Printer("Canon", "JZ-918", "Black", 1200)
print(p1)
###test