'''ամենամեծ ընդհանուր բաժանարարը'''

num1=int(input('Enter the first number'))
num2=int(input('Enter the second number'))
if num1<0 or num2<0:
    print("Error")
elif num1==0:
    print('The greatest common divisor is ', num2)
elif num2==0:
    print('The greatest common divisor is ', num1)
else:
    k=1
    for i in range(num1,num2):
        if num1%i==0 and num2%i==0:
            k=i
    print("The greatest common divisor is ", k)



