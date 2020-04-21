# import openpyxl and tkinter modules
from openpyxl import *
from tkinter import *



# globally declare wb and sheet variable

# opening the existing excel file
wb = load_workbook('C:/Users/Lenovo/Desktop/Book1.xlsx')

# create the sheet object
sheet = wb.active


def excel():
    # resize the width of columns in
    # excel spreadsheet
    sheet.column_dimensions['A'].width = 30
    sheet.column_dimensions['B'].width = 30
    sheet.column_dimensions['C'].width = 10
    sheet.column_dimensions['D'].width = 30
    sheet.column_dimensions['E'].width = 20
    sheet.column_dimensions['F'].width = 60
    sheet.column_dimensions['G'].width = 60
    sheet.column_dimensions['H'].width = 60
    sheet.column_dimensions['I'].width = 60
    #sheet.column_dimensions['J'].width = 60

    # write given data to an excel spreadsheet
    # at particular location
    sheet.cell(row=1, column=1).value = "Name"
    sheet.cell(row=1, column=2).value = "Last Name"
    sheet.cell(row=1, column=3).value = "Age"
    sheet.cell(row=1, column=4).value = "Id"
    sheet.cell(row=1, column=5).value = "Contact Nmber"
    sheet.cell(row=1, column=6).value = "Symptoms"
    sheet.cell(row=1, column=7).value = "Prescription"
    #sheet.cell(row=1, column=8).value = "New Prescription"


# Function to set focus (cursor)
def focus1(event):
    # set focus on the course_field box
    Name.focus_set()


# Function to set focus
def focus2(event):
    # set focus on the sem_field box
    Last_Name.focus_set()


# Function to set focus
def focus3(event):
    # set focus on the form_no_field box
    Age.focus_set()


# Function to set focus
def focus4(event):
    # set focus on the contact_no_field box
    Id.focus_set()


# Function to set focus
def focus5(event):
    # set focus on the email_id_field box
    Contact_no.focus_set()


# Function to set focus
def focus6(event):
    # set focus on the address_field box
    Symptoms.focus_set()


def focus7(event):
    # set focus on the address_field box
    Prescription.focus_set()

def focus8(event):
    # set focus on the address_field box
    New_prescription.focus_set()





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
   # New_prescription.delete(0, END)


# Function to take data from GUI
# window and write to an excel file
def insert():
    # if user not fill any entry
    # then print "empty input"
    if (Name.get() == "" and
            Last_Name.get() == "" and
            Age.get() == "" and
            Id.get() == "" and
            Contact_no.get() == "" and
            Symptoms.get() == "" and
            Prescription.get() == "" ):
            #New_prescription.get() == ""):

        print("empty input")

    else:

        # assigning the max row and max column
        # value upto which data is written
        # in an excel sheet to the variable
        current_row = sheet.max_row
        current_column = sheet.max_column

        # get method returns current text
        # as string which we write into
        # excel spreadsheet at particular location
        sheet.cell(row=current_row + 1, column=1).value = Name.get()
        sheet.cell(row=current_row + 1, column=2).value = Last_Name.get()
        sheet.cell(row=current_row + 1, column=3).value = Age.get()
        sheet.cell(row=current_row + 1, column=4).value = Id.get()
        sheet.cell(row=current_row + 1, column=5).value = Contact_no.get()
        sheet.cell(row=current_row + 1, column=6).value = Symptoms.get()
        sheet.cell(row=current_row + 1, column=7).value = Prescription.get()
     #   sheet.cell(row=current_row + 1, column=8).value = New_prescription.get()
        # save the file
        wb.save('C:/Users/Lenovo/Desktop/Book1.xlsx')

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

    excel()

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
    #New_prescription = Label(root, text="New Prescription", bg="light green")

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
   # New_prescription.grid(row=8, column=0)

    # create a text entry box
    # for typing the information
    Name = Entry(root)
    Last_Name = Entry(root)
    Age = Entry(root)
    Id = Entry(root)
    Contact_no = Entry(root)
    Symptoms = Entry(root)
    Prescription = Entry(root)
    #New_prescription = Entry(root)

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
    Id.bind("<Return>", focus4)

    # whenever the enter key is pressed
    # then call the focus5 function
    Contact_no.bind("<Return>", focus5)

    # whenever the enter key is pressed
    # then call the focus6 function
    Symptoms.bind("<Return>", focus6)
    Prescription.bind("<Return>", focus7)
    #New_prescription.bind("<Return>", focus8)



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
   # New_prescription.grid(row=8,column=1,ipadx='100')

    # call excel function
    excel()

    # create a Submit Button and place into the root window
    submit = Button(root, text="Submit", fg="Black",
                    bg="Red", command=insert)
    submit.grid(row=9, column=1)

    # start the GUI
    root.mainloop()