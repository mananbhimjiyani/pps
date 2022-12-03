from tkinter import *
import mysql.connector
import time

# connecting to the database
db = mysql.connector.connect(host="localhost", user="root", passwd="", database="project")
mycur = db.cursor()


def error_destroy():
    err.destroy()


def succ_destroy():
    succ.destroy()
    root1.destroy()


def error():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x100")
    Label(err, text="All fields are required..", fg="red", font="bold").pack()
    Label(err, text="").pack()
    Button(err, text="Ok", bg="grey", width=8, height=1, command=error_destroy).pack()


def userexsist():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x100")
    Label(err, text="User Already Exist", fg="red", font="bold").pack()
    Label(err, text="").pack()
    Button(err, text="Ok", bg="grey", width=8, height=1, command=error_destroy).pack()

def patientexist():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x100")
    Label(err, text="Patient Already Exist", fg="red", font="bold").pack()
    Label(err, text="").pack()
    Button(err, text="Ok", bg="grey", width=8, height=1, command=error_destroy).pack()


def success():
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("200x100")
    Label(succ, text="Registration successful...", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=8, height=1, command=succ_destroy).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()
    if username_info == "":
        error()
    elif password_info == "":
        error()
    else:
        sql = "SELECT SELECT user FROM `login"
        if username_info == sql:
            sql = "insert into login values(%s,%s)"
            t = (username_info, password_info)
            mycur.execute(sql, t)
            db.commit()
            Label(root1, text="").pack()
            time.sleep(0.50)
            success()
        else:
            userexsist()


def user_registration():
    global root1
    root1 = Toplevel(root)
    root1.title("Registration Portal")
    root1.geometry("300x250")
    global username
    global password
    Label(root1, text="Register your account", bg="grey", fg="black", font="bold", width=300).pack()
    username = StringVar()
    password = StringVar()
    Label(root1, text="").pack()
    Label(root1, text="Username :", font="bold").pack()
    Entry(root1, textvariable=username).pack()
    Label(root1, text="").pack()
    Label(root1, text="Password :").pack()
    Entry(root1, textvariable=password, show="*").pack()
    Label(root1, text="").pack()
    Button(root1, text="Register", bg="red", command=register_user).pack()


def login():
    global root2
    root2 = Toplevel(root)
    root2.title("HMS Portal")
    root2.geometry("300x300")
    global username_varify
    global password_varify
    Label(root2, text="Log-In Portal", bg="grey", fg="black", font="bold", width=300).pack()
    username_varify = StringVar()
    password_varify = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", font="bold").pack()
    Entry(root2, textvariable=username_varify).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :").pack()
    Entry(root2, textvariable=password_varify, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Log-In", bg="red", command=login_varify).pack()
    Label(root2, text="")


def logg_destroy():
    logg.destroy()
    root2.destroy()


def fail_destroy():
    fail.destroy()


def logged():
    global logg
    logg = Toplevel(root2)
    logg.title("Logged IN")
    logg.geometry("300x300")
    Label(logg, text="Welcome {} ".format(username_varify.get()), fg="green", font="bold").pack()
    Label(logg, text="HOSPITAL MANAGEMENT SYSTEM", font="bold").pack()
    Label(logg, text="").pack()
    Button(logg, text="Registering Patient", bg="grey", width=15, height=1, command=patient_registration).pack()
    Label(logg, text="").pack()
    Button(logg, text="Registering Doctor", bg="grey", width=15, height=1, command=Doctor_Registration).pack()
    Label(logg, text="").pack()
    Button(logg, text="Log-Out", bg="grey", width=8, height=1, command=logg_destroy).pack()


def patient():
    name_info = p_name.get()
    age_info = p_age.get()
    problem_info = p_problem.get()
    phone_info = p_phone.get()

    if name_info == "":
        error()
    elif age_info == "":
        error()
    elif problem_info == "":
        error()
    elif phone_info == "":
        error()
    else:
        sql="SELECT p_name FROM patient_details"
        if phone_info == sql:
            sql = "insert into patient_details values(%s,%s,%s,%s)"
            t = (name_info, age_info, problem_info, phone_info)
            mycur.execute(sql, t)
            db.commit()
            Label(root1, text="").pack()
            time.sleep(0.50)
            success()
        else:
            patientexist()


def patient_registration():
    global root1
    global p_name, p_age, p_problem, p_phone
    root1 = Toplevel(root)
    root1.title("Patient Registration")
    root1.geometry("500x500")
    Label(root1, text="Patient Registration", bg="grey", fg="black", font="bold", width=300).pack()
    p_name = StringVar()
    p_age = StringVar()
    p_problem = StringVar()
    p_phone = StringVar()
    Label(root1, text="").pack()
    Label(root1, text="Enter Patient Name:", font="bold").pack()
    Entry(root1, textvariable=p_name).pack()
    Label(root1, text="").pack()
    Label(root1, text="Enter Age:").pack()
    Entry(root1, textvariable=p_age, ).pack()
    Label(root1, text="").pack()
    Label(root1, text="Enter the Problem/Disease:").pack()
    Entry(root1, textvariable=p_problem, ).pack()
    Label(root1, text="").pack()
    Label(root1, text="Enter Phone number:").pack()
    Entry(root1, textvariable=p_phone, ).pack()
    Label(root1, text="").pack()
    Button(root1, text="Log-In", bg="red", command=patient).pack()
    Label(root1, text="")


def Doctor_Registration():
    global logg
    logg = Toplevel(root2)
    logg.title("Logged IN")
    logg.geometry("300x300")
    Label(logg, text="Welcome {} ".format(username_varify.get()), fg="green", font="bold").pack()
    Label(logg, text="HOSPITAL MANAGEMENT SYSTEM", font="bold").pack()
    Label(logg, text="").pack()
    Button(logg, text="Registering Patient", bg="grey", width=15, height=1, command=patient_registration).pack()
    Label(logg, text="").pack()
    Button(logg, text="Registering Doctor", bg="grey", width=15, height=1, command=Doctor_Registration).pack()
    Label(logg, text="").pack()
    Button(logg, text="Log-Out", bg="grey", width=8, height=1, command=logg_destroy).pack()


def failed():
    global fail
    fail = Toplevel(root2)
    fail.title("Invalid")
    fail.geometry("200x100")
    Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", bg="grey", width=8, height=1, command=fail_destroy).pack()


def login_varify():
    user_varify = username_varify.get()
    pas_varify = password_varify.get()
    sql = "select * from login where user = %s and password = %s"
    mycur.execute(sql, [(user_varify), (pas_varify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()


def main_screen():
    global root
    root = Tk()
    root.title("HMS Portal")
    root.geometry("300x300")
    Label(root, text="Welcome to HMS Protal", font="bold", bg="grey", fg="black", width=300).pack()
    Label(root, text="").pack()
    Button(root, text="Log-IN", width="8", height="1", bg="red", font="bold", command=login).pack()
    Label(root, text="").pack()
    Button(root, text="Registration", height="1", width="15", bg="red", font="bold", command=user_registration).pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="Developed By Manan and Megha").pack()


main_screen()
root.mainloop()

# conn = sql.connect(host='localhost', user='root', passwd='', database='project')
# if conn.is_connected():
#     print('successfully connected')
# c1 = conn.cursor()
# print('---------------------------------------------')
# print("HOSPITAL MANAGEMENT SYSTEM")
# print('---------------------------------------------')
# print('"GOD WISHES YOU"')
# print("1.LOGIN")
# print("2.EXIT")
# choice = int(input("ENTER YOUR CHOICE:"))
# if choice == 1:
#     u1 = input("enter user name:")
#     pwd1 = input("enter the password:")
#     while u1 == 'vasu' and pwd1 == 'vasu6072':
#         print('connected')
#
#         print("WELCOME TO HOSPITAL")
#         print("successfully connected")
#         print('1.RegisteringPatient details')
#         print('2.RegisteringDoctor details')
#         print('3.RegisteringWorker details')
#         print("4.total patient details")
#         print("5.total doctor details")
#         print("6.total worker details")
#         print('7.Patient detail')
#         print('8.Doctor detail')
#         print('9.Worker detail')
#         print('10.Exit')
#         choice = int(input('ENTER YOUR CHOICE:'))
#         if choice == 1:
#             p_name = input('Enter Patient Name:')
#             p_age = int(input('Enter Age:'))
#             p_problems = input('Enter the Problem/Disease:')
#             p_phono = int(input('Enter Phone number:'))
#             sql_insert = "insert into patient_details values(""'" + p_name + "'," + str(
#                 p_age) + ",'" + p_problems + "'," + str(p_phono) + ")"
#             c1.execute(sql_insert)
#             print('SUCCESSFULLY REGISTERED')
#             conn.commit()
#
#         elif choice == 2:
#             d_name = input('Enter Doctor Name:')
#             d_age = int(input('Enter Age:'))
#             d_department = input('Enter the Department:')
#             d_phono = int(input('Enter Phone number:'))
#             sql_insert = "insert into doctor_details values(""'" + d_name + "'," + str(
#                 d_age) + ",'" + d_department + "'," + str(d_phono) + ")"
#             c1.execute(sql_insert)
#             print('successfully registered')
#             conn.commit()
#
#         elif choice == 3:
#             w_name = input('Enter Worker Name:')
#             w_age = int(input('Enter Age:'))
#             w_workname = input('Enter type of work:')
#             w_phono = int(input('Enter Phone number:'))
#             sql_insert = "insert into worker_details values(""'" + w_name + "'," + str(
#                 w_age) + ",'" + w_workname + "'," + str(w_phono) + ")"
#             c1.execute(sql_insert)
#             print('successfully registered')
#             conn.commit()
#
#         elif choice == 4:
#             sql_w = 'select*from patient_details '
#             c1.execute(sql_w)
#             r = c1.fetchall()
#             for i in r:
#                 print(i)
#
#         elif choice == 5:
#             sql_x = "select*from doctor_details"
#             c1.execute(sql_x)
#             s = c1.fetchall()
#             for i in s:
#                 print(i)
#
#         elif choice == 6:
#             sql_y = "select*from worker_details"
#             c1.execute(sql_y)
#             t = c1.fetchall()
#             for i in t:
#                 print(i)
#
#         elif choice == 7:
#             h = input("Enter the name:")
#             sql_w = 'select*from patient_details where p_name=("{}")'.format(h)
#             c1.execute(sql_w)
#             u = c1.fetchall()
#             for i in u:
#                 print(i)
#
#         elif choice == 8:
#             d = input("Enter the name:")
#             sql_d = 'select*from doctor_details where p_name=("{}")'.format(d)
#             c1.execute(sql_d)
#             v = c1.fetchall()
#             for i in v:
#                 print(i)
#
#         elif choice == 9:
#             f = input("Enter the name:")
#             sql_f = 'select*from worker_details where p_name=("{}")'.format(f)
#             c1.execute(sql_f)
#             w = c1.fetchall()
#             for i in w:
#                 print(i)
#
#         elif choice == 10:
#             exit()
#             break
#     else:
#         print('wrong username&password')
# if choice == 2:
#     exit()
