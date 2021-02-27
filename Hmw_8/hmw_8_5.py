class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, item: "OfficeEquipment"):
        self.__storage.append(item)

    def transfer(self, idx: int, department: str):
        item: OfficeEquipment = self.__storage[idx]
        item.department = department

    def filter_by(self, **kwargs):
        for idx, item in enumerate(self):
            a: OfficeEquipment = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield idx, item

    def __getitem__(self, key):
        return self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"Devices in stock: {len(self.__storage)}"

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


storage = Storage()
storage.add(Printer("Canon", "JZ-352", "Black", 1200))
storage.add(Scanner("HP", "312", "White", 900))
storage.add(Xerox("Phaser", "450-A", "Green", 1100))
print(storage)

for idx, itm in storage.filter_by():
    print(idx, itm)



