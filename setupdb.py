import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('mydatabase.db')

        return con

    except Error:

        print(Error)

def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE Students(id integer PRIMARY KEY, firstName text, secondName text, paper1 int, paper2 int, paper3 int, total int, percentage int, grade int)")

    con.commit()

con = sql_connection()

sql_table(con)
