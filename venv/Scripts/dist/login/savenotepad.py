
from tkinter import *
import create2

ids = create2.face_id
# Function to set focus (cursor)
def focus1(event):

    Name.focus_set()


def focus2(event):

    Last_Name.focus_set()


# Function to set focus
def focus3(event):

    Age.focus_set()


# Function to set focus
#def focus4(event):
    # set focus on the contact_no_field box
    #Id.focus_set()


# Function to set focus
def focus5(event):

    Contact_no.focus_set()


# Function to set focus
def focus6(event):

    Symptoms.focus_set()


def focus7(event):

    Prescription.focus_set()

def focus8(event):
    # set focus on the address_field box
    Any_allergies.focus_set()





# Function for clearing the
# contents of text entry boxes
def clear():
    # clear the content of text entry box
    Name.delete(0, END)
    Last_Name.delete(0, END)
    Age.delete(0, END)
    Id.delete(0,END)
    Contact_no.delete(0, END)
    Symptoms.delete(0, END)
    Prescription.delete(0, END)
    Any_allergies.delete(0, END)


# Function to take data from GUI

def insert():
    # if user not fill any entry
    # then print "empty input"

    if (Name.get() == "" and
            Last_Name.get() == "" and
            Age.get() == "" and
            Id.get() == "" and
            Contact_no.get() == "" and
            Symptoms.get() == "" and
            Prescription.get() == ""  and
            Any_allergies.get() == ""):

        print("empty input")

    elif (Id.get() != ids):
        print("please enter the same id as earlier")

    else:

        file = open("D:/patientsdata/" + ids + ".txt", "wt")
        file.write("id :" + ids)
        file.write("\n" + "\n" + "\n")
        file.write("Name :" + Name.get())
        file.write("\n")
        file.write("Last Name :" + Last_Name.get())
        file.write("\n")
        file.write("Age :" + Age.get())
        file.write("\n")
        file.write("Contact no :" + Contact_no.get())
        file.write("\n")
        file.write("Symptoms :" + Symptoms.get())
        file.write("\n")
        file.write("Allergies " + Any_allergies.get())
        file.write("\n")
        file.write("\n")
        file.write("Prescriptions :" + Prescription.get())
        file.close()






        # set focus on the name_field box
        Name.focus_set()

        # call the clear() function
        clear()
        root.destroy()

    # Driver code


if __name__ == "__main__":
    # create a GUI window
    root = Tk()

    # set the background colour of GUI window
    root.configure(background='light green')

    # set the title of GUI window
    root.title("registration form")

    # set the configuration of GUI window
    root.geometry("500x300")



    # create a Form label
    heading = Label(root, text="Form", bg="light green")

    # create a Name label
    Name = Label(root, text="Name", bg="light green")

    # create a Last Name label
    Last_Name = Label(root, text="Last Name", bg="light green")

    # create a AGE label
    Age = Label(root, text="Age", bg="light green")

    Id = Label(root, text="Id", bg="light green")


    # create a Contact No. label
    Contact_no = Label(root, text="Contact No.", bg="light green")

    # create a Id No. lable
    Symptoms = Label(root, text="Symptoms.", bg="light green")

    # create a Email id label
    Prescription = Label(root, text="Prescription", bg="light green")

    # create a address label
    Any_allergies = Label(root, text="Allergies", bg="light green")

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    heading.grid(row=0, column=1)
    Name.grid(row=1, column=0)
    Last_Name.grid(row=2, column=0)
    Age.grid(row=3, column=0)
    Id.grid(row=4, column=0)
    Contact_no.grid(row=5, column=0)
    Symptoms.grid(row=6, column=0)
    Prescription.grid(row=7, column=0)
    Any_allergies.grid(row=8, column=0)

    # create a text entry box
    # for typing the information
    Name = Entry(root)
    Last_Name = Entry(root)
    Age = Entry(root)
    Id = Entry(root)
    Contact_no = Entry(root)
    Symptoms = Entry(root)
    Prescription = Entry(root)
    Any_allergies = Entry(root)

    # bind method of widget is used for
    # the binding the function with the events

    # whenever the enter key is pressed
    # then call the focus1 function
    Name.bind("<Return>", focus1)

    # whenever the enter key is pressed
    # then call the focus2 function
    Last_Name.bind("<Return>", focus2)

    # whenever the enter key is pressed
    # then call the focus3 function
    Age.bind("<Return>", focus3)

    # whenever the enter key is pressed
    # then call the focus4 function
    #Id.bind("<Return>", focus4)

    # whenever the enter key is pressed
    # then call the focus5 function
    Contact_no.bind("<Return>", focus5)

    # whenever the enter key is pressed
    # then call the focus6 function
    Symptoms.bind("<Return>", focus6)
    Prescription.bind("<Return>", focus7)
    Any_allergies.bind("<Return>", focus8)



    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    Name.grid(row=1, column=1, ipadx="100")
    Last_Name.grid(row=2, column=1, ipadx="100")
    Age.grid(row=3, column=1, ipadx="100")
    Id.grid(row=4, column=1, ipadx="100")
    Contact_no.grid(row=5, column=1, ipadx="100")
    Symptoms.grid(row=6, column=1, ipadx="100")
    Prescription.grid(row=7, column=1, ipadx="100")
    Any_allergies.grid(row=8,column=1,ipadx='100')


    # create a Submit Button and place into the root window
    submit = Button(root, text="Submit", fg="Black",
                    bg="Red", command=insert)
    submit.grid(row=9, column=1)

    # start the GUI
    root.mainloop()
    insert()
