import cmath

def compute_data(a, b, c):
    return (-b + (cmath.sqrt(b**2 - 4 * a * c)))/ (2*a)
print(compute_data(22, 66, 9))
print(compute_data(9, 1, 4))
