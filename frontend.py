from tkinter import *
from tkinter import messagebox 
import backend

window = Tk()
window.title('Book Inventory')

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        title_entry.delete(0,END)
        title_entry.insert(END, selected_tuple[1])
        author_entry.delete(0,END)
        author_entry.insert(END, selected_tuple[2])
        year_entry.delete(0,END)
        year_entry.insert(END, selected_tuple[3])
        isbn_entry.delete(0,END)
        isbn_entry.insert(END, selected_tuple[4])
    except IndexError:
        pass

def update_command():
    backend.update(selected_tuple[0], title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    print(title_value.get(), author_value.get(), year_value.get(), isbn_value.get())

def delete_command():
    backend.delete(selected_tuple[0])

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(title_value.get(), author_value.get(), year_value.get(), isbn_value.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    list1.delete(0, END)
    list1.insert(END, (title_value.get(), author_value.get(), year_value.get(), isbn_value.get()))

#Title
title=Label(window, text="Title")
title.grid(row=0, column=0)

title_value=StringVar()
title_entry=Entry(window, textvariable=title_value)
title_entry.grid(row=0, column=1)

#Author
author=Label(window, text="Author")
author.grid(row=0, column=2)

author_value=StringVar()
author_entry=Entry(window, textvariable=author_value)
author_entry.grid(row=0, column=3)

#Year
year=Label(window, text="Year")
year.grid(row=1, column=0)

year_value=StringVar()
year_entry=Entry(window, textvariable=year_value)
year_entry.grid(row=1, column=1)

#ISBN
isbn=Label(window, text="ISBN")
isbn.grid(row=1, column=2)

isbn_value=StringVar()
isbn_entry=Entry(window, textvariable=isbn_value)
isbn_entry.grid(row=1, column=3)

#List
list1=Listbox(window, height=6, width=45)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll_bar=Scrollbar(window)
scroll_bar.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

#View All
b1=Button(window,text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

#Search
b2=Button(window,text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

#Add Entry
b3=Button(window,text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

#Update
b4=Button(window,text="Update selected", width=12, command=update_command)
b4.grid(row=5, column=3)

#Delete
b5=Button(window,text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

#Close
b6=Button(window,text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()

