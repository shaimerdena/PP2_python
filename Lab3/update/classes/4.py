import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("x:", self.x, "y:", self.y)

    def move(self, x1, y1):
        self.x = x1
        self.y = y1

    def dist(self, point2):
        d1 = self.x - point2.x 
        d2 = self.y - point2.y 
        distance = math.sqrt(d1**2 + d2**2)
        return distance
    
x = int(input())
y = int(input())
points1 = Point(x,y)
points1.show()

x1 = int(input())
y1 = int(input())
points2 = Point(x1, y1)

print(points1.dist(points2))


