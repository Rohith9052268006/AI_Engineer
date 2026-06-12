def add_student(students,record):
    students.append(record)
    print("Student Added Successfully")
def remove_student(students,name):
    found=False
    for rec in range(len(students)):
        if students[rec]['name']==name:
            found=True
            students.pop(rec)
            break
    if found:
        print("Student record deleted successfully")
    else:
        print("Student Not Found")
def list_students(students):
    for st in students:
        for key,value in st.items():
            print(key,value)
def search_student(students,name):
    found=False
    for rec in students:
        if rec["name"]==name:
            found=True
            for i,j in rec.items():
                print(i,":",j)
    if not found:
        print("Student Not Found")
def search_student_exist(students,name):
    for i in range(len(students)):
        if students[i]["name"]==name:
            return True
    return False
students = []
while True:
    print("Menu:\n1 Add Student\n2 View Students\n3 Search Student\n4 Remove Student\n5 exit")
    a=int(input("Enter your choice"))
    if a==1:
        name=input("Enter your name: ")
        age=int(input("Enter your age: "))
        marks=int(input("Enter your marks: "))
        if search_student_exist(students,name):
            print("Student record already exists. Please enter another name")
        else:
            add_student(students,{"name":name,"age":age,"marks":marks})
    elif a==2:
        list_students(students)
    elif a==3:
        n=input("Enter the name of the student to be searched: ")
        search_student(students,n)
    elif a==4:
        d=input("Enter the name of the student to be deleted: ")
        remove_student(students,d)
    elif a==5:
        break
    else:
        print("Invalid Input\n Please Try again!!!")


