class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __repr__(self) -> str:
        return "Point({}, {})".format(self.x, self.y)
    
    def __str__(self) -> str:
        return "({}, {})".format(self.x, self.y)

    def get_halfway_point_to(self, target):
        midx = (self.x + target.x)/2
        midy = (self.y + target.y)/2

        return MyPoint(midx, midy)

class MyFraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self) -> str:  
        return "MyFraction(numerator = {}, denominator = {})".format(self.numerator, self.denominator)
    
    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, otherFraction):
        sumNumerator =  (self.numerator * otherFraction.denominator)\
                      + (otherFraction.numerator * self.denominator)
        sumDenominator = self.denominator * otherFraction.denominator

        return MyFraction(sumNumerator, sumDenominator)