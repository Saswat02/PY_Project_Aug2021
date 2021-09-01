from Admin import choice_admin
from Employee import choice_not_hr, choice_hr


def welcome(x):
    e = open("employee.txt", 'r')
    h = open("hr.txt", 'r')
    emp = e.readlines()
    hr = h.readlines()
    e.close()
    h.close()
    f = 0
    for line in hr:
        line = line.split(";")
        if f"ID:{x}" in line:
            for line1 in emp:
                temp = line1.split(";")
                if f"ID:{x}" in temp:
                    x = temp[1]
                    t = x.replace("NAME:", '')
                    print(f"Welcome {t} from HR.")
        else:
            for line1 in emp:
                temp = line1.split(";")
                if f"ID:{x}" in temp:
                    x = temp[1]
                    t = x.replace("NAME:", '')
                    f = 1
                    print(f"Welcome {t}")
    return f


def login_sys():
    log = open("login.txt", 'r')
    print("WELCOME TO EMPLOYEE SYSTEM")
    id1 = input("Please Input Login ID: ")
    pw = input("Please Input Password: ")

    cred = log.readlines()
    if f"{id1} {pw}\n" not in cred:
        print("Invalid Credentials...")
        exit(0)

    elif (f"{id1} {pw}\n" in cred) and (id1 == "admin"):
        choice_admin()

    else:
        x = welcome(id1)
        if x == 1:
            choice_not_hr(id1)
        else:
            choice_hr(id1)

    log.close()


login_sys()
