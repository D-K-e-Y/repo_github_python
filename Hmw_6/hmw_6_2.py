class Road:
    def __init__(self, _lenght, _width, _mass, _cm):
        self.lenght = _lenght
        self.width = _width
        self.mass = _mass
        self.cm = _cm
    def formula(self):
        return self.lenght * self.width * self.mass * self.cm
test_road = Road(100, 1500, 30, 7)
print(test_road.formula())