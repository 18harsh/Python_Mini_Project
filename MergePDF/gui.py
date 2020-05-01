# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:16:28 2020

@author: Harsh Gandhi
"""

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2
import os

def adjustWindow(window):
    w = 900  # width for the window size
    h = 600  # height for the window size
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen
    x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed
    window.resizable(False, False)    # disabling the resize option for the window
    window.configure(background='white')    # making the background white of the window
#def to open a file
def load_pdf(filename):
    try:
        f = open(filename, 'rb')
        return PyPDF2.PdfFileReader(f)
    except FileNotFoundError:
        pass



    
def loadpdf1():
    try:
        global pdf1,pdf1_pages,s1,e1,start_pdf1,end_pdf1
        root.filename = filedialog.askopenfilename(initialdir="/",title="Select A File",filetypes=(("pdf files", "*.pdf"),("all files", "*.*")))
        filename1=root.filename
        print(filename1)
        pdf1= load_pdf(filename1)
        pdf1_pages= pdf1.getNumPages()
        
        E_table1.insert(0,str(filename1))
        E_table1.config(state='readonly')
        
        filename1 = os.path.basename(filename1)
        
        E_table.insert(0,str(f"{filename1} has {pdf1_pages} pages."))
        E_table.config(state='readonly')
    
        Label(frame, text="Pages: ",background="sky blue").place(x=200,y=90)

        Label(frame, text="Start From : ",background="sky blue").place(x=300,y=90)
        pgnum=[]
        for i in range(1,pdf1_pages+1):
            pgnum.append(i)
        print(pgnum)
        s1=IntVar()
        s1.set(pgnum[0])
        pagemenu=OptionMenu(frame,s1,*pgnum)
        pagemenu.place(x=400,y=90)


        Label(frame, text="End at : ",background="sky blue").place(x=500,y=90)
        e1=IntVar()
        e1.set(pgnum[0])
        pagemenu=OptionMenu(frame,e1,*pgnum)
        pagemenu.place(x=600,y=90)
    except AttributeError:
        pass




def loadpdf2():
    try:
        global pdf2,pdf2_pages,E_table2,E_table21,start_pdf2,end_pdf2,s2,e2
        filename = filedialog.askopenfilename(initialdir="/",title="Select A File",filetypes=(("pdf files", "*.pdf"),("all files", "*.*")))
        filename2=filename
        print(filename2)
        pdf2= load_pdf(filename2)
        pdf2_pages= pdf2.getNumPages()
        E_table21.insert(0,str(filename2))
        E_table21.config(state='readonly')
        
        filename2 = os.path.basename(filename2)
        E_table2.insert(0,str(f"{filename2} has {pdf2_pages} pages."))
        E_table2.config(state='readonly')
        
        Label(frame, text="Pages: ",background="sky blue").place(x=200,y=200)

        Label(frame, text="Start From : ",background="sky blue").place(x=300,y=200)
        pgnum=[]
        for i in range(1,pdf2_pages+1):
            pgnum.append(i)
        print(pgnum)
        s2=IntVar()
        s2.set(pgnum[0])
        pagemenu=OptionMenu(frame,s2,*pgnum)
        pagemenu.place(x=400,y=200)

        Label(frame, text="End at : ",background="sky blue").place(x=500,y=200)
        e2=IntVar()
        e2.set(pgnum[0])
        pagemenu=OptionMenu(frame,e2,*pgnum)
        pagemenu.place(x=600,y=200)
    except AttributeError:
        pass


    
    
def add_to_writer(pdf,writer,start,end):

    for i in range(start-1, end):
        writer.addPage(pdf.getPage(i))

def save_pdf():
    global pdf1,pdf2,s1,e1,s2,e2
    start1=int(s1.get())
    end1=int(e1.get())

    start2=int(s2.get())
    end2=int(e2.get())


    # if output_filename[-4:]==".pdf":
    #     output_filename1=output_filename
    # elif output_filename[-4:]!=".pdf":
    #     output_filename1=f"{output_filename}.pdf"
    # result=filedialog.asksaveasfile(mode='wb',defaultextension=".pdf")
    output_file = filedialog.asksaveasfile(mode='wb',defaultextension=".pdf",filetypes=(("pdf files", "*.pdf"),("all files", "*.*"))) 


    writer= PyPDF2.PdfFileWriter()
  
    add_to_writer(pdf1,writer,start1, end1)
    add_to_writer(pdf2, writer,start2, end2)


    writer.write(output_file)
    
    output_file.close()
    messagebox.showinfo("Succesfull","The PDFs were Merged")


root= Tk()
root.title("PDF Merger")
adjustWindow(root)
Label(root, text="PDF Merger Using Python").pack()
frame=Frame(root, background = "sky blue")
frame.place(x=0,y=100,width=900, height=500)

global filename1,filename2,output_filename,outputtext,s1,e1,start_pdf1,end_pdf1,start_pdf2,end_pdf2
filename1=StringVar()
filename2=StringVar()
output_filename=StringVar()
pages1=IntVar()
start_pdf1=IntVar()
end_pdf1=IntVar()

start_pdf2=IntVar()
end_pdf2=IntVar()




Button(frame, text="Add First PDF",width=20, command=loadpdf1).place(x=10,y=50)
# Label(frame, text="").grid(row=2,column=0)
Button(frame, text="Add Second PDF", width=20,command=loadpdf2).place(x=10,y=150)

E_table=Entry(frame,bd=2,width=50)
E_table.place(x=400,y=52)
E_table1=Entry(frame,bd=2,width=30)
E_table1.place(x=200,y=52)

E_table2=Entry(frame,bd=2,width=50)
E_table2.place(x=400,y=150)
E_table21=Entry(frame,bd=2,width=30)
E_table21.place(x=200,y=150)

# Label(frame,text="Enter the PDF name: ",background="sky blue").place(x=240,y=400)
# save_pdf_entry=Entry(frame,textvariable=output_filename,width=24)
# save_pdf_entry.place(x=380,y=400)
    

Button(frame, text="Combine/Save PDF as : ",command=lambda:save_pdf(),width=20).place(x=380,y=430)
   
root.mainloop()
