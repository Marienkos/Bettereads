import sqlite3

def startSeq():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            date INTEGER NOT NULL
        )"""
    )

def viewAll():
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()

    for book in books:
        print(book)

    if books == []:
        print("There's no book to show!")

def addBook():
    title = input("Title: ")
    author = input("Author: ")
    date = input("Date: ")

    cur.execute("""
        INSERT INTO books (title, author, date)
        VALUES (?, ?, ?)
    """, (title, author, date)
    )

def deleteBook():
    id = input("ID: ")

    cur.execute("DELETE FROM books WHERE id=?", id)

conn = sqlite3.connect("books.db")
cur = conn.cursor()

startSeq()

while True:
    cmd = input("Specify command (view, add, delete, exit): ")

    match cmd:
        case "view": viewAll()
        case "add": addBook()
        case "delete": deleteBook()
        case "exit": break

conn.commit()
conn.close()