def pass_fail():
    name = input("Enter your name")
    marks=int(input("Enter your marks"))
    if(marks>35):
        print(name, "is pass")
    else:
        print(name,"is fail")
pass_fail()