import tkinter as tk
import json
loggedIn = False

def loadJson(filename):
    with open(filename, "r") as r:
        jsons = r.readlines()
        json.loads(jsons)
        r.close()
        return json

def writeJson(dictionary, filename):
    with open(filename, "w") as w:
        jsonencoded = json.dumps(dictionary)
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

class Student:
    def __init__(self, fname, lname, paper1, paper2, paper3):
        self.fname = fname
        self.lname = lname
        self.paper1 = paper1
        self.paper2 = paper2
        self.paper3 = paper3
    def calcpercent(self):
        total = self.paper1 + self.paper2 + self.paper3
        percentage = int((total/240) * 100)
        return percentage
        
#users = loadJson("users.json")
users = [User("jack", "jack123"), User("Jack","jack123")]
students = []
def inputScores(name, lname, paper1, paper2, paper3):
    global loggedIn
    print(loggedIn)
    if loggedIn ==True:
        print("Name: " , name, lname, "\n", "Total for score: " , (paper1 + paper2 + paper3))
        student = Student(name, lname, paper1, paper2, paper3)
        students.append(student)
        tk.messagebox.showinfo("Authentication error", "You  must be logged in!")
        
    else:
        tk.messagebox.showinfo("Authentication error", "You  must be logged in!")
        

    
def draw():
    master = tk.Tk()
    master.title("Test Results system")
    master.geometry("500x1000")
    tk.Label(master, text="Class marking system", padx = 10, font=("Arial", 25)).grid(row=0, column = 4)
    tk.Label(master, text="First Name").grid(row=1, column=3)
    tk.Label(master, text="Last Name").grid(row=2, column=3)
    tk.Label(master, text="Paper 1: ").grid(row=3, column=3)
    tk.Label(master, text="Paper 2: ").grid(row=4, column=3)
    tk.Label(master, text="Paper 3: ").grid(row=5, column=3)
    
    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e4 = tk.Entry(master)
    e5 = tk.Entry(master)

    e1.grid(row=1, column=4)
    e2.grid(row=2, column=4)
    e3.grid(row=3, column=4)
    e4.grid(row=4, column=4)
    e5.grid(row=5, column=4)

    button = tk.Button(master, text="Submit scores", width=30,pady=5, command=lambda: inputScores(str(e1.get()), str(e2.get()), int(e3.get()), int(e4.get()), int(e5.get()))).grid(row=9, column=4)




    tk.Label(master, text="Login", font=("Arial", 25)).grid(row=10, column = 4)
    tk.Label(master, text="Username").grid(row=11, column=3)
    tk.Label(master, text="Password").grid(row=12, column=3)
    usernameinput = tk.Entry(master)
    passwordinput = tk.Entry(master)

    usernameinput.grid(row=11, column=4)
    passwordinput.grid(row=12, column=4)

    loginButton = tk.Button(master, text="Login", width = 30,pady=5, command = lambda: login(users, str(usernameinput.get()), str(passwordinput.get()))).grid(row=14, column=4)
    
draw()
