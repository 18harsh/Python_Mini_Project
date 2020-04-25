# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:10:20 2020

@author: Harsh
"""


from tkinter import*
from backend import Database

database=Database("books.db")


class Bookstore:
    
    root=Tk()
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


    def __init__(self):
        self.root.title("Book Store")
        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)
        b1=Button(self.root,text="View All",width=12,command=self.view_command)
        b1.grid(row=2,column=3)
        b2=Button(self.root,text="Search Entry",width=12,command=self.search_command)
        b2.grid(row=3,column=3)
        b3=Button(self.root,text="Add Entry",width=12,command=self.entry_command)
        b3.grid(row=4,column=3)
        b4=Button(self.root,text="Update Selected",width=12,command=self.update_command)
        b4.grid(row=5,column=3)
        b5=Button(self.root,text="Delete Selected",width=12,command=self.delete_command)
        b5.grid(row=6,column=3)
        b6=Button(self.root,text="Close",width=12,command=self.root.destroy)
        b6.grid(row=7,column=3)

    def get_selected_row(self,event):
      try:  
        global selected_tuple
        index=self.list1.curselection()[0]
        selected_tuple=self.list1.get(index)
        self.e1.delete(0,END)
        self.e1.insert(END,selected_tuple[1])
        self.e2.delete(0,END)
        self.e2.insert(END,selected_tuple[2])
        self.e3.delete(0,END)
        self.e3.insert(END,selected_tuple[3])
        self.e4.delete(0,END)
        self.e4.insert(END,selected_tuple[4])
      except IndexError:
          pass
    def view_command(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)
    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.e1.get(),self.e2.get(),self.e3.get(),self.e4.get()):
                self.list1.insert(END,row)
    def entry_command(self):   
        self.list1.delete(0,END)
        database.insert(self.e1.get(),self.e2.get(),self.e3.get(),self.e4.get())
        self.list1.insert(END,"Data Save successfully")
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
    def delete_command(self):
        try:
            database.delete(selected_tuple[0])
            self.view_command()
        except:
            self.list1.delete(0,END)  
            self.list1.insert(END,"Select Something")    
    
    def update_command(self):    
        # print(selected_tuple[0],e1.get(),e2.get(),e3.get(),e4.get())
        try:    
            database.update(selected_tuple[0],self.e1.get(),self.e2.get(),self.e3.get(),self.e4.get())
            self.view_command()
        except:
              self.list1.delete(0,END)  
              self.list1.insert(END,"Select Something")  
    

    def run(self):
        self.root.mainloop()    


bookstore=Bookstore()
bookstore.run()
