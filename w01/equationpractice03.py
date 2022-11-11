import math

def compute_area(r):
    return math.pi * r * r

radius = float(input("what is the radius "))
print(f"the area is: {compute_area(radius)}")
