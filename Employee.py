

def search_employee(emp_id):
    e = open("employee.txt", 'r')
    flag = False
    lines = e.readlines()
    e.close()
    for line in lines:
        line = line.split(";")
        if f"ID:{emp_id}" in line:
            print(line[0])
            print(line[1])
            print(line[2])
            print(line[3])
            print(line[4])
            flag = True
            break

    if flag is False:
        print("Employee not found\n")


def display_hr():
    e = open("employee.txt", 'r')
    h = open("hr.txt", 'r')
    emp = e.readlines()
    hr = h.readlines()
    e.close()
    h.close()
    ids = []
    for x in hr:
        x = x.split(";")
        ids.append(x[0])

    for i in ids:
        for line1 in emp:
            temp1 = line1.split(";")
            if i in temp1:
                print(temp1[1])
                break
        for line2 in hr:
            temp2 = line2.split(";")
            if i in temp2:
                print(temp2[1])
                print(temp2[2])
                break


def display_emp(emp_designation):
    e = open("employee.txt", 'r')
    emp = e.readlines()
    e.close()
    for line in emp:
        temp = line.split(";")
        if emp_designation == "All":
            print(temp[0])
            print(temp[1])
            print(temp[2])
            print(temp[3])
            print(temp[4])
        elif f"DESIGNATION:{emp_designation}" in temp:
            print(temp[0])
            print(temp[1])
            print(temp[2])
            print(temp[3])
            print(temp[4])


def choice_not_hr(x):
    i = 0
    while i != 3:
        print("\nSelect the following operation...")
        print("1 - View own detail.")
        print("2 - View all HR.")
        print("3 - Exit")
        i = int(input("Enter your choice: "))
        if i == 1:
            search_employee(x)

        elif i == 2:
            display_hr()

        elif i == 3:
            exit(0)

        else:
            print("\nPlease enter a valid choice...")


def choice_hr(x):
    i = 0
    while i != 3:
        print("\nSelect the following operation...")
        print("1 - View own detail.")
        print("2 - View all Employees.")
        print("3 - Exit")
        i = int(input("Enter your choice: "))
        if i == 1:
            search_employee(x)

        elif i == 2:
            deg = input("Filter Designation (All for All): ")
            display_emp(deg)

        elif i == 3:
            exit(0)

        else:
            print("\nPlease enter a valid choice...")
