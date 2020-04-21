from tkinter import *

import os

root=Tk()
root.configure(background="white")
def function1():
    os.system("py savenotepad.py")
def function2():
    os.system("py train.py")
def function3():
    os.system("py newpredict.py")

def function6():
    root.destroy()
def attend():
   root.title("JAR ")

Label(root, text="MED HELP USING FACE RECOGNITION",font=("times new roman",20),fg="white",bg="green",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Enter patient ",font=("times new roman",20),bg="blue",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

Button(root,text="Train Dataset",font=("times new roman",20),bg="blue",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Predict patient",font=('times new roman',20),bg="blue",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


Button(root,text="Exit",font=('times new roman',20),bg="red",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
