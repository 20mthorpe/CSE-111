# as many functions as you can
# print(str(round(float(input("Enter a number")), 1)))

#import sys
#use all 5 arguments in the print function

#print("hello, I", 20, sep=" am ", end=' How old are you?', file=sys.stdout, flush=True)

import math

#num = (math.ceil(17**9 / 3) - 6)

#if (num % 2) == 0:
 #   num = True
  #  print(num)

#else:
 #   num = False
  #  print(num)

#def random_math():
#    return (math.ceil(17**9 / 3) - 6) % 2 == 0

#print(random_math())

#import random

#random_nums = []
#while len(random_nums) < 10:
 #   random_nums.append(random.randint(1, 50))

#random_nums.sort()
#print(random_nums)

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

display_message = "odd minute"
if now.minute % 2 == 0:
    display_message = "even minute"
print(display_message)



