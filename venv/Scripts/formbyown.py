from tkinter import *

window = Tk()
#setting the application object here

window.title("Patient information")
window.geometry("300x200+10+20")

#creating button
btn=Button(window, text="Submit", fg='blue')
btn.place(x=80, y=100)

#creating label
lbl=Label(window, text="Enter patienr name", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)

#creating entry
txtfld=Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=80, y=250)

#creating radio button
v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="male", variable=v0,value=1)
r2=Radiobutton(window, text="female", variable=v0,value=2)
r1.place(x=100,y=350)
r2.place(x=180, y=350)


#calling a method when button is clicked
btn = Button(window, text='OK')
#btn.bind('<Button-1>', MyButtonClicked)

window.mainloop()
#wait for events gen by user and gets cloased when cross
#button is pressed

