from MyMath import Point

p1 = Point(15, 27)
p2 = Point(10, 20)
print(p1.x, end = ' ')
print(p2.y, end = ' ')
p1.translate(10, 20)
print(p1.x, p1.y, end = ' ')
p2.translate(20, 30)
print(p1.x, p1.y, end = ' ')
