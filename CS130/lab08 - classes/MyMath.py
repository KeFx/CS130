class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

class MyFraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self) -> str:
        return "MyFraction({}, {})".format(self.numerator, self.denominator)