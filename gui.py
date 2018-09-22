from tkinter import *
def helloCallBack():
    s=E1.get()
    f=open("sample.txt",'w+')
    f.write(s)
    f.close()
top = Tk()
L1 = Label(top, text = "The Answer")
L1.pack( side = LEFT)
E1 = Entry(top, bd = 5)
E1.pack(side = RIGHT)
B = Button(top, text = "submit",command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()
