import sqlite3

def connect() :
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
	conn.commit()
	conn.close()

def add(title,author,year,isbn) :
	conn= sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title,author,year,isbn)) 
	conn.commit()
	conn.close()

def view() :
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM books")
	rows = cur.fetchall()
	conn.close()
	return rows

def search(title=None,author=None,year=None,isbn=None) :
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
	rows = cur.fetchall()
	conn.close()
	return rows

def delete(id) :
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM books WHERE id=?", (id,))
	conn.commit()
	conn.close()

def update(title,author,year,isbn,id) :
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
	conn.commit()
	conn.close()



#print(search('Harry Potter'))

connect()
#add('The Marathon', 'Woodrow Wilson', 2012, 1363455)
#add('Avalanche', 'Tom Hiddleston', 2004, 1345345)
#add('Harry Potter', 'J.K. Rowling', 2001, 24723427)
#print(view())
#delete(1)
#update('Goosebumps', 'L.R. Steyn', 2009, 3)
#print(search('Harry Potter'))
#print(view())

