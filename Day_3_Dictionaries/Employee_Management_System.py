import json
def add_employee(employees,employee):
    employees.append(employee)

def view_employees(employees):
    for employee in employees:
        for key,value in employee.items():
            print(key,":",value)

def search_employee(employees,id):
    for emp in employees:
        if emp.get("id")==id:
            for key,value in emp.items():
                print(key,":",value)
            break

def update_salary(employees,empid,salary):
    for emp in employees:
        if emp.get("id")==id:
            emp["Salary"]=salary
            break

def delete_employee(employees,id):
    for i in range(len(employees)):
        if employees[i].get("id")==id:
            employees.pop(i)
            break

def employee_exist(employees,id):
    for emp in employees:
        if(emp.get("id")==id):
            return True
    return False

employees=[]
while True:
    print("Menu\n1 Add Employee\n2 View Employees\n3 Search Employee\n4 Update Salary\n5 Delete Employee\n6 Save To JSON\n7 Load From JSON\n8 Exit")
    choice=int(input("Please enter your choice"))
    if choice==1:
        id=int(input("Enter your id :"))
        name=input("Enter your name :")
        age=int(input("Enter your age :"))
        salary=int(input("Enter your salary :"))
        if employee_exist(employees,id):
            print("Employee Details already exixts in our database")
        else:
            add_employee(employees,{"id":id,"name":name,"age":age,"Salary":salary})
    elif choice==2:
        if not employees:
            print("Employee details are empty")
        else:
            view_employees(employees)
    elif choice==3:
        id=int(input("Please enter employee id to be searched: "))
        if not employee_exist(employees,id):
            print("Employee details not found")
        else:
            print("Employee Details fetched successfully")
            search_employee(employees,id)
    elif choice==4:
        empid=int(input("Enter Employee ID:"))
        salary=int(input("Enter New Salary:"))
        if not employee_exist(employees,id):
            print("Employee details not found")
        else:
            update_salary(employees,empid,salary)
            print("Employee salary updated suceessfully")
    elif choice==5:
        id=int(input("Please enter employee id to be deleted: "))
        if not employee_exist(employees,id):
            print("Employee details not found")
        else:
            delete_employee(employees,id)
            print("Employee details deleted suceessfully")
    elif choice==6:
        with open("employees.json","w") as file:
            json.dump(employees,file)
        print("Employee details successfully loaded to json file")
    elif choice==7:
        with open("employees.json","r") as file:
            employees=json.load(file)
        print("Employee details successfully fetched from json")
    elif choice==8:
        break
    else:
        print("Invalid Choice. Please Try again!!")

