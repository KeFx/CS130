class Octagon():
    def __init__(self, side_length = 1) -> None:
        self.side_length = side_length
        self.interior_angle = 135
        self.exterior_angle = 45
    
    def set_side_length(self, side_length):
        if side_length > 0:
            self.side_length = side_length
    
    def get_interior_angle(self):
        return self.interior_angle
    
    def get_exterior_angle(self):
        return self.exterior_angle
    
    def get_perimeter(self):
        return 8 * self.side_length
    
    def get_area(self):
        return 2 * (1 + 2**(1/2)) * (self.side_length**2)
    
    def __repr__(self) -> str:
        return f"Octagon({self.side_length})"
    
    def __str__(self) -> str:
        return "An octagon with a perimeter of {:.2f} and an area of {:.2f}."\
                .format(self.get_perimeter(), self.get_area())
    
    def __eq__(self, otherOctagon) -> bool:
        if not isinstance(otherOctagon, Octagon):
            return False
        return self.side_length == otherOctagon.side_length
