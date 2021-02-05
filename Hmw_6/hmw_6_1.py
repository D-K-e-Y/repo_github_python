import time
class Trafficlight:
    __color = None
    def running(self, __color):
        self.color = __color
test_color = Trafficlight()
test_color.running('red')
time.sleep(2)
print(test_color.color)
test_color.running('yellow')
time.sleep(2)
print(test_color.color)
test_color.running('green')
time.sleep(2)
print(test_color.color)
#test