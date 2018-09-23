from tkinter import*
def func1():
    s=entry1.get()
    f=open("answer1.txt",'w+')
    f.write(s)
    f.close()
def func2():
    p=entry2.get()
    f=open("answer2.txt",'w+')
    f.write(p)
    f.close()
def func3():
    q=entry3.get()
    f=open("answer3.txt",'w+')
    f.write(q)
    f.close()
def func4():
    r=entry4.get()
    f=open("answer4.txt",'w+')
    f.write(r)
    f.close()
root=Tk()
topframe=Frame(root)
lab1=Label(topframe,text="question1")
lab1.pack()
entry1=Entry(topframe)
entry1.pack()
button=Button(topframe,text="submit1",command=func1)
button.pack()
lab2=Label(topframe,text="question2")
lab2.pack()
entry2=Entry(topframe)
entry2.pack()
button=Button(topframe,text="submit2",command=func2)
button.pack()
lab3=Label(topframe,text="question3")
lab3.pack()
entry3=Entry(topframe)
entry3.pack()
button=Button(topframe,text="submit3",command=func3)
button.pack()
lab4=Label(topframe,text="question4")
lab4.pack()
entry4=Entry(topframe)
entry4.pack()
button=Button(topframe,text="submit4",command=func4)
button.pack()


topframe.pack(side=TOP)
bottomframe=Frame(root)












root.mainloop()
