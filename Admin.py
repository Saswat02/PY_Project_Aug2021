

def add_employee(emp_id, emp_name, emp_doj, emp_designation, emp_salary):
    e = open("employee.txt", "a")
    e.write(f"ID:{emp_id};NAME:{emp_name};DATE OF JOIN:{emp_doj};DESIGNATION:{emp_designation};SALARY:{emp_salary}\n")
    e.close()


def add_hr(hr_id, hr_dept, hr_role):
    h = open("hr.txt", "a")
    h.write(f"ID:{hr_id};DEPARTMENT:{hr_dept};ROLE:{hr_role}\n")
    h.close()


def remove_employee(emp_id):
    e = open("employee.txt", "r")
    lines = e.readlines()
    for line in lines:
        if f"ID:{emp_id}" in line.split(";"):
            print(f"Employee Removed: {line}")
            lines.remove(line)
            break
    e.close()
    e1 = open("employee.txt", 'w')
    for l1 in lines:
        e1.writelines(l1)
    e1.close()


def remove_hr(emp_id):
    h = open("hr.txt", "r")
    lines = h.readlines()
    for line in lines:
        if f"ID:{emp_id}" in line.split(";"):
            print(f"HR Removed: {line}")
            lines.remove(line)
            break
    h.close()
    h1 = open("hr.txt", 'w')
    for l1 in lines:
        h1.writelines(l1)
    h1.close()


def search_employee(emp_id):
    e1 = open("employee.txt", "r")
    flag = False
    lines = e1.readlines()
    for line in lines:
        if f"ID:{emp_id}" in line.split(";"):
            flag = True
            break

    e1.close()
    if flag is True:
        return True
    else:
        return False


def add_login(id1, pw):
    l1 = open("login.txt", 'a')
    l1.write(f"{id1} {pw}\n")
    l1.close()


def remove_login(id1):
    a = open("login.txt", 'r')
    lines = a.readlines()
    for line in lines:
        if id1 in line:
            print(f"Login Credential Removed: {line}")
            lines.remove(line)
            break
    a.close()
    l2 = open("login.txt", 'w')
    for z in lines:
        l2.writelines(z)
    l2.close()


def choice_admin():
    i = 0
    while i != 5:
        print("\nSelect the following operation...")
        print("1 - Add an Employee to the database.")
        print("2 - Remove an Employee in database.")
        print("3 - Add a HR to the database.")
        print("4 - Remove a HR in database.")
        print("5 - Exit")
        i = int(input("Enter your choice: "))
        if i == 1:
            i = input("\nEnter the ID of the Employee: ")
            n = input("Enter the Name of the Employee: ")
            d = input("Enter the DOJ of the Employee: ")
            des = input("Enter the Designation of the Employee: ")
            s = float(input("Enter the Salary of the Employee: "))
            add_employee(i, n, d, des, s)
            add_login(i, n)

        elif i == 2:
            x = input("\nEnter the ID: ")
            remove_employee(x)
            remove_login(x)

        elif i == 3:
            ih = input("\nEnter the ID of the HR: ")
            t = search_employee(ih)
            if t is True:
                dept = input("Enter the department for HR: ")
                role = input("Enter the role for HR: ")
                add_hr(ih, dept, role)
            else:
                print("Invalid ID...")

        elif i == 4:
            x = input("\nEnter the ID: ")
            remove_hr(x)

        elif i == 5:
            exit(0)

        else:
            print("\nPlease enter a valid choice...")

