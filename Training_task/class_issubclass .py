

class Main:
    def set_class(self):
        raise NotImplementedError('переопределите метод в дочерних классов')


class A(Main):
    def set_class(self):
        print("класс А")


class B(Main):
    def set_class(self):
        print("класс B")


class C(Main):
    def set_class(self):
        print("класс C")


m = Main()
a = A()
b = B()
c = C()


a.set_class()
b.set_class()
c.set_class()
m.set_class()
