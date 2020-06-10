import math

class Sphere:
    def sphere_square(self):
        radius = float(input("Please enter the radius of sphere: "))
        volume = 3 / 4 * math.pi * pow(radius, 3)
        print("Volume = " + str(volume))

class Triangle:
    def triangle_square(self):
        side_a = float(input("Please enter the side a for triangle: "))
        side_b = float(input("Please enter the side b for triangle: "))
        side_c = float(input("Please enter the side c for triangle: "))
        p_half = (side_a + side_b + side_c) / 2
        square = math.sqrt(p_half * (p_half - side_a) * (p_half - side_b) * (p_half - side_c))
        print(square)

obj1 = Sphere()
obj2 = Triangle()
obj1.sphere_square()
obj2.triangle_square()
