print("Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

O=int(input("Enter operator between (1,2,3,4)-"))
a=int(input("Enter first number - "))
b=int(input("Enter second number - "))

if O=='1':
    print("Addition : ",(a+b))
elif O=='2':
    print("Subtraction : ",(a-b))
elif O=='3':
    print("Multiplication :",(a*b))
elif '4':
    if b!=0:
        print("Division :",a/b)
    else:
        print("Cannot divide by zero")    

else:
    print ("invalid operator")
