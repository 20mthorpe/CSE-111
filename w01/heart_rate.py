"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
print("Hi! I will compute your maximum heart rate, as well as how high your heart rate should be when you excersize!")

age = int(input("What is your age? "))

maximum = 220 - age

sixtyfive = maximum * .65

eightyfive = maximum * .85

print(f"{maximum} is your maximum heart rate.")
print(f"you should keep your heart rate between {sixtyfive} and {eightyfive} while working out to strengthen your heart.")