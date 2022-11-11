#calling functions
from datetime import datetime

today = datetime.today()
day_value = (today.weekday())
customer_sub = 1

while customer_sub > 0:

    item_price = float(input("What is the price of the item? "))
    item_amount = float(input("How many items are you buying? "))

    customer_sub = item_price * item_amount

    if (day_value == 1 or day_value == 2):
        if customer_sub >= 50:
            print(f"The discounted is ${customer_sub*.1:2f}.")
            customer_sub = customer_sub * .9
        else:
            print(f"if you spend $ {50 - customer_sub} more, you can get 10% off")

    sales_tax = customer_sub * .06
    total = customer_sub * 1.06
    print(f"Sales tax is ${sales_tax:.2f}")
    print(f"Your total is ${total:.2f}")
