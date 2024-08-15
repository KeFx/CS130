class Address():
    def __init__(self, street, city, postal_code, is_residential) -> None:
        self.street = street
        self.city = city
        self.postal_code = postal_code
        self.is_residential = is_residential

    def calculate_postage_cost(self):
        return (4 if self.is_residential else 10)
    
    def __str__(self) -> str:
        return f"Shipping to {self.street}, {self.city}({self.postal_code}) \
                costs ${self.calculate_postage_cost()}."

class Person():
    def __init__(self, name, street, city, postal_code, is_residential) -> None:
        self.name = name
        self.address = Address(street, city, postal_code, is_residential)

    def __str__(self) -> str:
        return f"{self.name}: {self.address}"
    
class RegularPolygon():
    def __init__(self, num_sides = 3, side_length = 1) -> None:
        self.num_sides = num_sides
        self.side_length = side_length

    def get_perimeter(self):
        return self.num_sides * self.side_length
    
    def __str__(self) -> str:
        return "Polygon({perimeter:.2f})".format(perimeter = self.get_perimeter())
    
class Block():
    def __init__(self) -> None:
        self.polygons = []

    def add_polygon(self, num_sides, side_length):
        self.polygons.append(RegularPolygon(num_sides, side_length))

    def get_polygon(self, index):
        return self.polygons[index]
    
    def __str__(self) -> str:
        if len(self.polygons) == 0:
            return "EMPTY BLOCK"
        else:
            polygonStringsList = [str(polygon) for polygon in self.polygons]
            print(polygonStringsList)
            
            return ('\n').join(polygonStringsList)
        
block1 = Block()
block1.add_polygon(4, 4.3)
block1.add_polygon(6, 14)
block1.add_polygon(3, 2.5)
print(block1)
print(type(block1))
polygon1 = block1.get_polygon(1)
print(type(polygon1))
print(polygon1)
print(block1.get_polygon(0))
block2 = Block()
print(block2)
print(type(block2))