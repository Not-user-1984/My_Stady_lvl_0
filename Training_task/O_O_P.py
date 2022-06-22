
class Point:
    color = 'red'
    circle = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        print("Удaление " + str(self))

    def set_coords(self, x=0, y=3):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point(2, 4)


print(pt.__dict__)

