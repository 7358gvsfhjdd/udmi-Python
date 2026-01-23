class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))
    
    def print_point(self):
        return f"X is {self.x} and y is {self.y}"
    
p1 = Point (3, 2)
p2 = Point (5, 3)
    
p = p1.sum(p2)
p.print_point()