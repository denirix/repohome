# Ex_1-2
import time
class Auto:
    def __init__(self, brand, age, mark, color='', weight=''):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age +=1
        print(self.age)

auto_1 = Auto('BMW', 2000, 'X5')
auto_1.move()
auto_1.stop()
auto_1.birthday()

class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color='', weight=''):
        super().__init__(brand, age, mark, color='', weight='')
        self.max_load = max_load
    def move(self):
        print('attention!!!')
        super().move()

    def load(self):
        time.sleep(1)
        print('sleep')
        time.sleep(1)

truck_1 = Truck('MAN', 2010, 'TG', 15000)
truck_1.move()
truck_1.load()

truck_2 = Truck('KAMAZ', 1998, '4410', 20000)
truck_2.move()
truck_2.load()

class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color='', weight=''):
        super().__init__(brand, age, mark, color='', weight='')
        self.max_speed = max_speed
    def move(self):
        super().move()
        print(f'max speed is {self.max_speed}')


car_1 = Car('Tesla', 2018, 'X', 280)
car_1.move()

car_2 = Car('Volkswagen', 2020, 'Polo', 200)
car_2.move()