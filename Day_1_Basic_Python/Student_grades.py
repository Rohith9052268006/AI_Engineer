def pass_fail(marks):
    if(marks<0 or marks>100):
        print("Invalid Marks")
    if(marks>=35):
        print("Result: PASS")
        if(marks>=90):
            print("Grade: A")
        elif(marks>=75):
            print("Grade: B")
        elif(marks>=60):
            print("Grade: C")
        else:
            print("Grade: D")
    else:
        print("Result: FAIL")

marks=int(input("Marks:"))
pass_fail(marks)