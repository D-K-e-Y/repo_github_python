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

class AppError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

class ValidateEquipmentError(AppError):
    pass

    @staticmethod
    def validate(cnt):
        if not isinstance(cnt, int):
            ValidateEquipmentError(f"'{type(cnt)}'; количество инстансов должен быть типа 'int'")

    @classmethod
    def create(cls, cnt, **properties):
        cls.validate(cnt)
        return [cls(**properties) for _ in range(cnt)]


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
###test