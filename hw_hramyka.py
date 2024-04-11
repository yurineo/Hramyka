

import logging

import argparse

FORMAT = '{levelname:<8}{asctime}. Строка {lineno:03d} функция "{funcName}", сообщение: "{message}"'
DATEFMT = '%d-%m-%Y %H:%M:%S'

# Создание  логгера объекта

logging.basicConfig(filename='fileLog.log', filemode='w', encoding='utf-8', format=FORMAT, style='{', datefmt=DATEFMT, level=logging.NOTSET) #устанавливаем уровень NOTSET - уровень не задан. Все события регистрируются.
logger = logging.getLogger('main') # создаем логгер !!!!!

# Создание парсера
parser = argparse.ArgumentParser(description='Прога для работы с прямоугольниками') # создаем объект парсера
parser.add_argument('-width', type=int, help='Ширина прямоугольника') # добавляем  ширину
parser.add_argument('-height', type=int, nargs='?', default=1, help='Высота прямоугольника') # добавляем высоту
args = parser.parse_args() # вывод Namespace с  width и height
class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            logger.error(f'Ширина положительная, а не {width}')
            raise NegativeValueError(f'Ширина положительная, а не {width}')
        self._width = width

        if height is None:
            self._height = width
        else:
            if height <= 0:
                logger.error(f'Высота положительная, а не {height}')
                raise NegativeValueError(f'Высота положительная, а не {height}')
            self._height = height
            logger.info(f'Создание прямоугольника со сторонами {self._width} и {self._height}')

    @property
    def width(self):
        logger.info(f'Ширина: {self._width}')
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
            logger.info(f'Изменяем ширину на {self._width}')
        else:
            logger.error(f'Ширина положительная, а не {value}')
            raise NegativeValueError(f'Ширина  положительная, а не {value}')

    @property
    def height(self):
        logger.info(f'Высота : {self._height}')
        return self._height


    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
            logger.info(f'Изменяем высота прямоугольника на {self._height}')
        else:
            logger.error(f'Высота должна быть только положительной, а не {value}')
            raise NegativeValueError(f'Высота должна быть только положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)


    def area(self):

        return self._width * self._height


    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        if width == 0:
            logger.error('Результат вычитания двух прямоугольников не может с шириной 0')
            return None
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


r = Rectangle(4,4)
r.width = 2
r.perimeter()
r.area()
r.__add__(Rectangle(2, 3))
r.__sub__(Rectangle(2, 3))
r.__lt__(Rectangle(2, 3))
r.__eq__(Rectangle(2, 3))
r.__le__(Rectangle(2, 3))
r.__str__()

r = Rectangle(args.width, args.height)

# r'''
# примеры запуска:
# py.\hw_hramyka.py -width 19 -height 29
# py.\hw_hramyka.py -h
# '''

