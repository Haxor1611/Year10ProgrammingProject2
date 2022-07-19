from asyncore import write
import tkinter as tk
import json
from tkinter import NO, ttk
from tkinter import *
import sqlite3

from sqlite3 import Error

loggedIn = False
studentNumber = 0

def sql_connection():

    try:

        con = sqlite3.connect('mydatabase.db')

        return con

    except Error:

        print(Error)

def sql_table(con, students):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE Students(id integer PRIMARY KEY, firstName text, secondName text, paper1 int, paper2 int, paper3 int, total int, percentage int, grade int)")

    con.commit()
    for student in students:
        insertIntoTable(cursorObj, student)





def writeJson(dictionary, filename):
    with open(filename, "w") as w:
        jsonencoded = json.dumps(dictionary,indent=3)
        w.write(jsonencoded)
        w.close()

def login(users, username, password):
    global loggedIn
    for user in users:
        if username == user.username and password == user.password:
            loggedIn = True
            print("logged in")
            break
        else:
            print("failed")

def hashpassword(password):
        print("hashing")
        
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Students:
    def __init__(self, students):
        self.students = students

class Student:
    def __init__(self, fname, lname, paper1, paper2, paper3):
        self.fname = fname
        self.lname = lname
        self.paper1 = paper1
        self.paper2 = paper2
        self.paper3 = paper3
        self.total = paper1 + paper2 + paper3
        
    def calcpercent(self):
        total = self.paper1 + self.paper2 + self.paper3
        percentage = int((total/240) * 100)
        if percentage < 90:
            self.grade = int((percentage/10) + 0.5)
        else:
            self.grade = int(percentage/10)
        self.percentage = percentage
        return percentage

        

users = [User("jack", "jack123"), User("Jack","jack123")]
students = []
studentClassList = []
def inputScores(name, lname, paper1, paper2, paper3):
    global loggedIn
    print(loggedIn)
    if loggedIn ==True:
        
        print("Name: " , name, lname, "\n", "Total for score: " , (paper1 + paper2 + paper3))
        student = Student(name, lname, paper1, paper2, paper3)
        print(str(student.calcpercent()) + "%" + "Grade: " + str(student.grade))
        students.append(student.__dict__)
        studentClassList.append(student)
        tk.messagebox.showinfo("Authentication error", "Submitted scores for: " + name)
        
    else:
        tk.messagebox.showinfo("Authentication error", "You  must be logged in!")
        
def insertIntoTable(obj, student):
    obj.execute("INSERT INTO students VALUES(" + str(studentNumber) + ", " + str(student.fname) + ", " + str(student.lname) + ', ' + str(student.paper1) + ", " + str(student.paper2) + ", " + str(student.paper3), + ", " + str(student.total) + ", " + str(student.percentage) + ", " + str(student.grade) + ")")
def completedScores(master):
    print(students)
    studentObj = Students(students)
    print(studentObj.__dict__)
    writeJson(studentObj.__dict__, "students.json")
    sql_table(con, studentClassList)

def getColumn(columnNumber):
    column = []
    for student in students:
        student = student.__dict__
        column.append(student[columnNumber])

    



def draw():
    master = tk.Tk()
    master.title("Test Results system")
    master.geometry("500x1000")
    tk.Label(master, text="Class marking system", padx = 10, font=("Arial", 25)).grid(row=0, column = 4)
    tk.Label(master, text="First Name").grid(row=1, column=3,pady=2)
    tk.Label(master, text="Last Name").grid(row=2, column=3,pady=2)
    tk.Label(master, text="Paper 1: ").grid(row=3, column=3,pady=2)
    tk.Label(master, text="Paper 2: ").grid(row=4, column=3,pady=2)
    tk.Label(master, text="Paper 3: ").grid(row=5, column=3,pady=2)
    
    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e4 = tk.Entry(master)
    e5 = tk.Entry(master)

    e1.grid(row=1, column=4,pady=2)
    e2.grid(row=2, column=4,pady=2)
    e3.grid(row=3, column=4,pady=2)
    e4.grid(row=4, column=4,pady=2)
    e5.grid(row=5, column=4,pady=2)

    button = tk.Button(master, text="Submit scores", width=30,pady=5, command=lambda: inputScores(str(e1.get()), str(e2.get()), int(e3.get()), int(e4.get()), int(e5.get()))).grid(row=9, column=4)
    completeButton = tk.Button(master, text= "Completed Adding scores", width=19, padx=20, command= lambda : completedScores(master)).grid(row=10, column=4,pady=15)



    tk.Label(master, text="Login", font=("Arial", 25)).grid(row=11, column = 4)
    tk.Label(master, text="Username").grid(row=12, column=3,pady=2)
    tk.Label(master, text="Password").grid(row=13, column=3,pady=2)
    usernameinput = tk.Entry(master)
    passwordinput = tk.Entry(master)

    usernameinput.grid(row=12, column=4,pady=2)
    passwordinput.grid(row=13, column=4,pady=2)

    loginButton = tk.Button(master, text="Login", width = 30,pady=5, command = lambda: login(users, str(usernameinput.get()), str(passwordinput.get()))).grid(row=15, column=4,pady=2)
    
   

draw()
con = sql_connection()

