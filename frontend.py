"""
A program that stores book information-
		Title, Author, Year, ISBN

User can:
	View records
	Search for entry
	Add entry
	Update entry
	Delete entry
	Close
"""
from tkinter import *
import backend
import time

def get_selected_row(event) :
	global selected_row
	index = list1.curselection()[0]
	selected_row = list1.get(index)

	e1.delete(0,END)
	e1.insert(END,selected_row[1])

	e2.delete(0,END)
	e2.insert(END,selected_row[2])

	e3.delete(0,END)
	e3.insert(END,selected_row[3])

	e4.delete(0,END)
	e4.insert(END,selected_row[4])
	
	return(selected_row)

def clear() :
	list1.delete(0,END)

def view_button() :
	list1.delete(0,END)
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)
	e4.delete(0,END)
	for row in backend.view() :
		list1.insert(END,row)

def search_button() :
	list1.delete(0,END)
	for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()) :
		list1.insert(END,row)
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)
	e4.delete(0,END)

def add_button() :
	backend.add(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
	list1.delete(0,END)
	list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)
	e4.delete(0,END)

def delete_button() :
	backend.delete(selected_row[0])
	list1.delete(0,END)
	list1.insert(END, view_button())

def update_button() :
	backend.update(title_text.get(),author_text.get(),year_text.get(),isbn_text.get(),selected_row[0])
	list1.insert(END, view_button())
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)
	e4.delete(0,END)

window = Tk()
window.wm_title("Book Store")

l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = Label(window, text='Author')
l2.grid(row=0, column=2)

l3 = Label(window, text='Year')
l3.grid(row=1, column=0)

l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, width=38)
list1.grid(row=3, column=1, rowspan=7)

sb1 = Scrollbar(window)
sb1.grid(row=3, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text='View All', command=view_button)
b1.grid(row=3, column=3)

b2 = Button(window, text='Search', command=search_button)
b2.grid(row=4, column=3)

b3 = Button(window, text='Add', command=add_button)
b3.grid(row=5, column=3)

b4 = Button(window, text='Update', command=update_button)
b4.grid(row=6, column=3)

b5 = Button(window, text='Delete', command=delete_button)
b5.grid(row=7, column=3)

b6 = Button(window, text='Close')
b6.grid(row=8, column=3)

b7 = Button(window, text='Clear', command=clear)
b7.grid(row=9, column=3)



window.mainloop()

