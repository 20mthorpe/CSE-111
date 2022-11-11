import csv

def main():

    read_dict("products.csv")
    products_dict = read_dict("products.csv")
    print(products_dict)

    with open("request.csv") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            
            key_value = row_list[0]
            quantity = row_list[1]

            print(f"\nProduct name: {products_dict[key_value][1]}")
            print(f"Requested quantity: {quantity}")
            print(f"Product price: {products_dict[key_value][2]}")

def read_dict(filename):

    products_dict = {}

    with open(filename) as csv_file:

        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:

            #print(row_list)

            product = {row_list[0]: [row_list[0], row_list[1], float(row_list[2])]}
            products_dict.update(product)

    return products_dict

if __name__ == "__main__":
    main()