def calculator(a,b):
    print("Addition:",a+b)
    print("Subtraction:",a-b)
    print("Multiplication:",a*b)
    if(b!=0):
        print("Division:",a/b)
    else:
        print("Zero Division error")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
calculator(a,b)