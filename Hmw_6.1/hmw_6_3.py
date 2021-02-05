class Worker:
    def __init__(self, name, surname, position, _income = None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': 1000, 'bonus': 200}
class Position(Worker):
    def get_full_name(self):
        return self.name, self.surname, self.position
    def get_total_income(self):
        return self._income
test_position = Position('Dmitrii', 'Vasiliev', 'Ing.')
print(test_position.get_full_name())
print(test_position.get_total_income())
#test
#test