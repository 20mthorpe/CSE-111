import math

items_man = int(input("What is the number of manufactured items? "))
items_in_box = int(input("What is the number of items that you will pack per box? "))

print(f"For {items_man} items, packing {items_in_box} items in each box, you will need {math.ceil(items_man/items_in_box)} boxes.")