class Car:
    def __init__(self, speed, color, name, is_police = True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return 'The car is going.'
    def stop(self):
        return 'The car is stop.'
    def turn(self, direction):
        return 'The car turn to ' + direction
    def show_speed(self):
        return None

class TownCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
        if speed >= 60:
            print('Oh my god! Brake down!')
        else:
            print(speed)

class SportCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

class WorkCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
        if speed >= 40:
            print('Oh my god! Brake down!')
        else:
            print(speed)

class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

town = TownCar('Renault', 70, 'Red', True)
print(town.name, town.speed, town.color)
print(town.go, town.stop, town.turn('Rodeo'))

sport = SportCar('Maserati', 210, 'White', False)
print(sport.name, sport.speed, sport.color)
print(sport.go, sport.stop, sport.turn('Race'))

work = WorkCar('Ford', 35, 'Yellow', True)
print(work.name, work.speed, work.color)
print(work.go, work.stop, work.turn('Work Place'))

police = PoliceCar('VW', 55, 'Black', True)
print(police.name, police.speed, police.color)
print(police.go, police.stop, police.turn('Patrol Place'))
#test