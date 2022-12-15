class Unit:

    def move(self, field, x_coord: int, y_coord: int, direction: str, is_fly: bool, is_crawl: bool, speed: int = 1):
        """Функция реализует перемещение юнита по полю.
        """

        if is_fly and is_crawl:
            raise ValueError('Рожденный ползать летать не должен!')
        if not is_fly and not is_crawl:
            raise ValueError('Похоже рыба, раз не ползает и не летает!')

        if is_fly:
            speed *= 1.2
        elif is_crawl:
            speed *= 0.5


        if direction == 'UP':
            new_y = y_coord + speed
            new_x = x_coord
        elif direction == 'DOWN':
            new_y = y_coord - speed
            new_x = x_coord
        elif direction == 'LEFT':
            new_y = y_coord
            new_x = x_coord - speed
        elif direction == 'RIGHT':
            new_y = y_coord
            new_x = x_coord + speed

        field.set_unit(x=new_x, y=new_y, unit=self)
