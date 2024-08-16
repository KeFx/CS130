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
        
class Point():
    def __init__(self, x = 1, y = 1) -> None:
        self.x = x
        self.y = y 
    
    def __str__(self) -> str:
        return "({}, {})".format(self.x, self.y)
    
    def get_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**(1/2)

class PolyLine():
    def __init__(self) -> None:
        self.points = []

    def __str__(self) -> str:
        return "->".join([str(point) for point in self.points])

    def get_point(self, index):
        return self.points[index]
    
    def add_point(self, x, y):
        self.points.append(Point(x, y))

    def get_total_length(self):
        total_dist = 0
        for idx, point in enumerate(self.points):
            if idx + 1 < len(self.points):
                total_dist += point.get_distance(self.points[idx+1])
        return total_dist
    
class Rainfall():
    def __init__(self, location = "UNKOWN") -> None:
        self.location = location 
        self.monthly_rainfall_list = []

    def add_rainfall(self, measurement) :
        self.monthly_rainfall_list.append(measurement)

    def get_annual_rainfall(self):
        return sum(self.monthly_rainfall_list)
    
    def get_average_monthly_rainfall(self):
        return sum(self.monthly_rainfall_list)/len(self.monthly_rainfall_list)
    
    def __str__(self) -> str:
        if len(self.monthly_rainfall_list) == 0:
            return f"No rainfall data for {self.location}"
        else: 
            return f"Location: {self.location}, Average Monthly Rainfall: \
                    {self.get_average_monthly_rainfall():.2f} mm"
        
class RainfallCollection():
    def __init__(self) -> None:
        self.rainfall_records = []

    def add_record(self, rainfall_record):
        if rainfall_record.get_annual_rainfall() > 0:
            self.rainfall_records.append(rainfall_record) 
    
    def get_total_annual_rainfall(self):
        totalAnnualRainfall = 0
        for record in self.rainfall_records:
            totalAnnualRainfall += record.get_annual_rainfall()
        return totalAnnualRainfall
    
    def __str__(self) -> str:
        return "\n".join([str(rainfall_record) for rainfall_record in self.rainfall_records])