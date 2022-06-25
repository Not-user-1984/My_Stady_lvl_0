
from turtle import color


class Point:
# атрб класса
    MIN_COORD = 0
    MAX_COORD = 50 

#магич метод созд после созд обьект класса
    def __init__(self, x, y):
        self.x = self.y = 0
        #пример работы @classmethod выполняеться проверка по значением @classmethod.
        if self.validate (x) and self.validate(y):
            self.__x = x
            self.__y = y

    def set_coord(self,x ,y):
        self.__x = x
        self.__y = y


#метод который работает внутри класса
    @classmethod
    def validate (cls,arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

# атрб класса, можно обрщ по внш ссылкам
    color = 'red'
    circle = 2

# магич метод для удаления
    def __del__(self):
        print("Удaление " + str(self))
#функция где self внеш ссылка к пространству имен
    def set_coords(self, x=0, y=3):
        self.x = x
        self.y = y
#
    def get_coords(self):
        return self.__x, self.__y

#
    @staticmethod
    def norm2( x, y):
        return x*x + y*y

#обьект класса
pt = Point(10,20)
suy  = pt.circle
print(pt.__dict__)
print(pt.validate(2))
print(pt.norm2(2,6))
print(pt.get_coords())
pt.set_coord(15,25)
print(pt.get_coords())
print(pt.__dict__)

