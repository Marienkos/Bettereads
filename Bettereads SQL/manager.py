import sqlite3

class Book:
    def __init__(self, title, author, date):
        self.title = title
        self.author = author
        self.date = date

def viewAll():
    cur.execute("SELECT * FROM books")
    righe = cur.fetchall()

    print(righe)

def askBook():
    title = input("Title: ")
    author = input("Author: ")
    date = input("Date: ")
    return Book(title, author, date)

def addBook(book : Book):
    cur.execute("""
        INSERT INTO books (title, author, date)
        VALUES (?, ?, ?)
    """,
    (book.title, book.author, book.date)
    )

conn = sqlite3.connect("books.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    date TEXT NOT NULL
)
""")

cmd = input("Specify command (view, add): ")

match cmd:
    case "view": viewAll()
    case "add": addBook(askBook())

conn.commit()
conn.close()