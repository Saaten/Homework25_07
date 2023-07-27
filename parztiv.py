'''ստուգել նեռմուծված թիվը պարզ է թէ ոչ '''

tiv=int(input("Enter the number"))
if tiv<=0:
    print("Error")
else:
    k=0
    kes=tiv//2
    for i  in range(2,kes):
        if tiv%i==0:
            k+=1
    if k==0:
        print("the number is prime")
    else:
        print("the number isn't prime")
