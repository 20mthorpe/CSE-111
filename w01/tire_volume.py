import math
from datetime import datetime

w = int(input("What is the width of the tire? (in millimeters) "))
a = int(input("What is the aspect ratio of the tire? "))
d = int(input("what is the diameter in inches of the wheen that the tire fits? "))

v = ((math.pi * (w**2) * a) *(w * a + 2540 * d)) / 10000000000

print(f"\nThe approximate volume is {v:.2f} liters\n")
now = datetime.now()
buy = bool(input("Do you want to buy these tires (True/False) "))
if buy:
    phone_number = input("What is your phone number? ")
    new_data = (f"{now} {w} {a} {d} {v} {phone_number}")
else:
    new_data = (f"{now} {w} {a} {d} {v}")

with open("volumes.txt", "a") as f:
    f.write(new_data)

print(new_data)

