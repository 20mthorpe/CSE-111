def compute_data(a, b, c, d):
#    x = a/b * (a/(c**2 + d**2))
#    return x
    return a/b * (a/(c**2 + d**2))

def test_data():
    data = []
    data.append([5, 4, 3, 2, 0.4807692307692308])
    data.append([9, 1, 4, 6, 1.5576923076923077])

    #this is what the data looks like when you append the list like this
    print(data)

    for test in data:
        print(compute_data(test[0], test[1], test[2], test[3])== test[4])

test_data()
print(compute_data(5, 4, 3, 2) == 0.4807692307692308)
print(compute_data(9, 1, 4, 6) == 1.5576923076923077)