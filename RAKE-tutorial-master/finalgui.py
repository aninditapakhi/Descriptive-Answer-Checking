from tkinter import *
from tkinter import messagebox
def func1():
    s=entry1.get()
    f=open("answer1.txt",'w+')
    f.write(s)
    disp1="Q.1 Answered"
    messagebox.showinfo("Result",disp1)
    f.close()
    entry1.delete(0,len(s))
def func2():
    p=entry2.get()
    f=open("answer2.txt",'w+')
    f.write(p)
    disp1="Q.2 Answered"
    messagebox.showinfo("Result",disp1)
    f.close()
    entry2.delete(0,len(p))
def func3():
    q=entry3.get()
    f=open("answer3.txt",'w+')
    f.write(q)
    disp1="Q.3 Answered"
    messagebox.showinfo("Result",disp1)
    f.close()
    entry3.delete(0,len(q))
def func4():
    r=entry4.get()
    f=open("answer4.txt",'w+')
    f.write(r)
    disp1="Q.4 Answered"
    messagebox.showinfo("Result",disp1)
    f.close()
    entry4.delete(0,len(r))
root=Tk()
lab0=Label(root,text="ANSWER ALL THE FOLLOWING QUESTIONS",bg="lightyellow",bd=20)
#lab0.config(font=(22,'bold')
lab0.grid(row=0,column=50)

lab1=Label(root,text="Q.1:  Write a short note on k-nearest neighbour",bd=10,bg="lightblue")
lab1.grid(row=30,column=50)
#lab1.pack(fill=X)
entry1=Entry(root)
entry1.grid(row=50,column=50)

button=Button(root,text="submit1",command=func1)
button.grid(row=70,column=50)

lab2=Label(root,text="Q.2:  Define operators and its types",bd=20,bg="lightblue")
lab2.grid(row=130,column=50)

entry2=Entry(root)
entry2.grid(row=150,column=50)

button=Button(root,text="submit2",command=func2)
button.grid(row=170,column=50)
lab3=Label(root,text="Q.3:  Define linked list and its types",bd=20,bg="lightblue")
lab3.grid(row=210,column=50)
entry3=Entry(root)
entry3.grid(row=230,column=50)
button=Button(root,text="submit3",command=func3)
button.grid(row=250,column=50)
lab4=Label(root,text="Q.4:  Explain supervised learning and its types",bd=20,bg="lightblue")
lab4.grid(row=310,column=50)
entry4=Entry(root)
entry4.grid(row=330,column=50)
button=Button(root,text="submit4",command=func4)
button.grid(row=350,column=50)


#topframe.pack(side=TOP)
bottomframe=Frame(root)












root.mainloop()
