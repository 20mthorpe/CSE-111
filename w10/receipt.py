import csv
from datetime import datetime

def main():

    read_dict("products.csv")
    products_dict = read_dict("products.csv")
    print(products_dict)
    num_items = 0
    subtotal = 0

    with open("request.csv") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)
        print("\nInkom Emporium")

        for row_list in reader:
            
            key_value = row_list[0]
            quantity = int(row_list[1])
            price = products_dict[key_value][2]

            num_items += quantity
            subtotal += (price * quantity)

            print(f"{products_dict[key_value][1]}: {quantity} @ {price}")

        print(f"\nNumber of Items: {num_items}")
        print(f"Subtotal: {subtotal:.2f}")
        sales_tax = subtotal * .06
        print(f"Sales Tax: {sales_tax:.2f}")
        total = subtotal + sales_tax
        print(f"Total: {total:.2f}\n")

        current_date_and_time = datetime.now()

        print("Thank you for shopping at the Inkom Emporium.")
        print(f"{current_date_and_time:%A %B %d %I:%M %p %Y}")


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