import sqlite3

class Database() :
	# Function to create a database connection after instantiating the class.
	def __init__(self,db) :
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
		self.conn.commit()

	# These functions actually query the database.
	def commit(self) :
		self.conn.commit()

	def add(self,title,author,year,isbn) :
		self.cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title,author,year,isbn)) 
		self.commit()

	def view(self) :
		self.cur.execute("SELECT * FROM books")
		rows = self.cur.fetchall()
		return rows

	def search(self,title=None,author=None,year=None,isbn=None) :
		self.cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
		rows = self.cur.fetchall()
		return rows

	def delete(self,id) :
		self.cur.execute("DELETE FROM books WHERE id=?", (id,))
		self.commit()

	def update(self,title,author,year,isbn,id) :
		self.cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
		self.commit()

	def __del__(self) :
		self.conn.close()




