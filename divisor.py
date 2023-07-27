'''ամենամեծ ընդհանուր բաժանարարը'''
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))

import math
gcd=math.gcd(num1,num2)

if gcd and gcd!=1:
    print("the greatest common devisor is: ", gcd)
else:
    print("there is no devisor")
