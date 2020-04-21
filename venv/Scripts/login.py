from tkinter import *
import os
import tkinter.messagebox as tm
root = Tk()
root.configure(background="white")
root.geometry("300x300")
root.title("JAR")

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.lblinst=Label(self,text="Please Login to Continue",font=("times new roman",20),justify="center",fg="white",bg="black")
        self.label_username = Label(self, text="Username:",font=("times new roman",20),justify="center", fg='black')
        self.label_password = Label(self, text="Password:",font=("times new roman",20),fg='black')

        self.entry_username = Entry(self)
        self.entry_password = Entry(self,show="*")
        self.lblinst.grid(row=0,sticky=W+E+N+S)
        self.label_username.grid(row=1, sticky=W+E+N+S)
        self.label_password.grid(row=3, sticky=W+E+N+S)
        self.entry_username.grid(row=2, column=0)
        self.entry_password.grid(row=4, column=0)

        self.logbtn = Button(self, text="Login", font=("times new roman",20),bg="green",fg='white',command=self.btnclicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def btnclicked(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "gndec" and password == "jar":
            tm.showinfo("Login info", "Welcome" " "+username)
            root.destroy()
            def func3():
                os.system(" py choice.py")
              #os.system('C:/Users/Lenovo/PycharmProjects/hospital/venv/Scripts/choice.py')
            func3()
        else:
            tm.showerror("Login error", "Incorrect details")
lf = LoginFrame(root)
root.mainloop()
