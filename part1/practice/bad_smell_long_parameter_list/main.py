# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self, field, speed=1):
        self.field = field
        self.speed = speed

    def move(self, x_coord, y_coord, direction):
        if direction == 'UP':
            new_y = y_coord + self.speed
            new_x = x_coord
        elif direction == 'DOWN':
            new_y = y_coord - self.speed
            new_x = x_coord
        elif direction == 'LEFT':
            new_y = y_coord
            new_x = x_coord - self.speed
        elif direction == 'RIGTH':
            new_y = y_coord
            new_x = x_coord + self.speed

        self.field.set_unit(x=new_x, y=new_y, unit=self)


class FlyUnit(Unit):

    def __init__(self, field, speed=1.2):
        super().__init__(field, speed)


class CrawlUnit(Unit):

    def __init__(self, field, speed=0.5):
        super().__init__(field, speed)

#     ...
