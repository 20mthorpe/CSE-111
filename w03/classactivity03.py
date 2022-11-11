rectangle_areas = []
count_up = 1

def rectangle_amount():
    amount_of_rectangles = int(input("How many rectangles are there? "))
    return amount_of_rectangles

while count_up <= amount_of_rectangles:
    def get_rectangles_dimensions():
        width = int(input(f"What is the width of the {count_up} rectangle "))
        height = int(input(f"What is the height of the {count_up} rectangle "))
        

def compute_rectangle_area(width, height):
    rectangle_area = width * height
    rectangle_areas.append(rectangle_area)
    return rectangle_area

def add_areas():
    for rectangle_area in rectangle_areas:
        total_area = total_area + rectangle_area
        
    return total_area
    