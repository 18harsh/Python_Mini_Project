# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:35:40 2020

@author: Harsh
"""


from tkinter import*
from backend import Database

database=Database("books.db")

def get_selected_row(event):
  try:  
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
  except IndexError:
      pass
def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)
def search_command():
    list1.delete(0,END)
    for row in database.search(e1.get(),e2.get(),e3.get(),e4.get()):
            list1.insert(END,row)
def entry_command():   
    list1.delete(0,END)
    database.insert(e1.get(),e2.get(),e3.get(),e4.get())
    list1.insert(END,"Data Save successfully")
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
def delete_command():
    database.delete(selected_tuple[0])
    view_command()
def update_command():    
    # print(selected_tuple[0],e1.get(),e2.get(),e3.get(),e4.get())
    database.update(selected_tuple[0],e1.get(),e2.get(),e3.get(),e4.get())
    view_command()
root=Tk()
root.wm_title("BookStore")
info=[]
l1=Label(root,text="Title").grid(row=0,column=0)
e1=Entry(root)
info.append(e1)
e1.grid(row=0,column=1)

l2=Label(root,text="Author").grid(row=0,column=2)
e2=Entry(root)
info.append(e2)
e2.grid(row=0,column=3)

l3=Label(root,text="Year").grid(row=1,column=0)
e3=Entry(root)
info.append(e3)
e3.grid(row=1,column=1)

l4=Label(root,text="ISBN").grid(row=1,column=2)
e4=Entry(root)
info.append(e4)
e4.grid(row=1,column=3)

list1=Listbox(root,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(root)
sb1.grid(row=2,column=2,rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(root,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)
b2=Button(root,text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)
b3=Button(root,text="Add Entry",width=12,command=entry_command)
b3.grid(row=4,column=3)
b4=Button(root,text="Update Selected",width=12,command=update_command)
b4.grid(row=5,column=3)
b5=Button(root,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=6,column=3)
b6=Button(root,text="Close",width=12,command=root.destroy)
b6.grid(row=7,column=3)

root.mainloop()