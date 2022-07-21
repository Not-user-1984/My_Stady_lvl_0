from string import ascii_letters


class Person:
    S_RUS ='абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_ps(ps)
        self.verify_weignt(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__ps = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИO должно быть строкой ')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат ФИО')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('в ФИО  должен быть хотя бы один символ')
            if len(s.strip(letters)) != 0:
                raise TypeError('в ФИО можно использовать только буквенные символы и дефис')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError(" Возраст должен быть целым числом в диапазоне 14,120 ")

    @classmethod
    def verify_weignt(cls, w):
        if type(w) != float or w < 20:
            raise TypeError('Вес должен быть вещественным числом от  20 и выше')

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Неверный формат паспорта')

        for p in s:
            if not p.isdigit():
                raise TypeError('серия и номер паспорта должны быть числами')

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):

        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weignt(weight)
        self.__old = weight

    @property
    def passport(self):
        return self.__ps

    @passport.setter
    def weight(self, ps):
        self.verify_weignt(ps)
        self.__ps = ps


p = Person("Иванов Сергей Иванович", 120, '1234 567890', 80.0)
p.fio = "Петр Сергей Иванович"
p.old = 100
p.weight = 30.0
print(p.__dict__)















