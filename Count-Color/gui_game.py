#GUI Game
import random
import time
from tkinter import messagebox,Tk,Label,Button,Canvas
colours=['blue','red','yellow','green','red','pink','red','black','green','cyan']
global i
i=0
global greencount
greencount=0
global redcount
redcount = 0
global canvas
def startclick(a):
    global i
    global canvas
    global redcount
    global greencount
    for i in range(1,a):
            m=random.randint(0,10)
            if m==1 or m==4 or m==6:
                redcount=redcount+1
            if m==3 or m==8:
                greencount = greencount+1
            try:
                a=random.randint(50,250)
                b=random.randint(50,300)
                canvas.create_oval(a,b,a+50,b+50,outline="white",fill=colours[m],width=2)
                canvas.update()
            except:
                print()
    return(1)    
def level1():
    global canvas
    canvas.delete("all")
    global a
    a=10
    startgame(a)
def level2():
    global canvas
    canvas.delete("all")
    global a
    a=50
    startgame(a)
def level3():
    global canvas
    canvas.delete("all")
    global a
    a=100
    startgame(a)    
def refresh():
    global greencount
    greencount=0
    global redcount
    redcount = 0
    global canvas
    canvas.delete("all")    
def startgame(a):
    global canvas
    x=startclick(a)
    if x==1:
        time.sleep(5)
    messagebox.showinfo("ANSWER ","number of red balls =" + str (redcount) + " and number of green balls ="+ str(greencount) )

root=Tk()
root.title("cout the colours")
root.geometry("800x700+20+20")
canvas=Canvas(width = 500,height=500,bg='#87ceeb')
canvas.place(x=20,y=20) 
l1=Button(root, text="Level-1",bg="#e79700",width=15,height=1,font=("Open Sams",13,'bold'),fg='white',command=level1)
l1.place(x=600,y=50)
l2=Button(root, text="Level-2",bg="#e79700",width=15,height=1,font=("Open Sams",13,'bold'),fg='white',command=level2)
l2.place(x=600,y=100)
l3=Button(root, text="Level-3",bg="#e79700",width=15,height=1,font=("Open Sams",13,'bold'),fg='white',command=level3)
l3.place(x=600,y=150)
w = Label(root, text="Can you count the number of red and green coloured balls ?",bg = "black",fg="yellow")
w.place(x=20,y=500)
y = Label(root, text="you have 10 seconds to answer ..press the start button to play !!",bg = "white",fg="blue")
y.place(x=20,y=550)
b= Button(root, text="REFRESH", bg="#e79700", width=20, height=1, font=("Open Sans", 13, 'bold'), fg='white',command=refresh)
b.place(x=20,y=600)
root.mainloop()             
