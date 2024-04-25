from tkinter import *
import os

root = Tk()
root.geometry("500x300")

def getvals():
    # Retrieve the values entered by the user
    name = Namevalue.get()
    contact = Contactvalue.get()
    address = Addressvalue.get()
    email = Emailvalue.get()
    visit_purpose = VisitPurposevalue.get()
    remember_me = checkvalue.get()


    # Format the data as a string with a newline after each detail
    data = f"Name: {name}\nContact: {contact}\nAddress: {address}\nEmail: {email}\nPurpose of Visit: {visit_purpose}\nRemember Me: {remember_me}\n\n"

    #you can change the directory
    directory = r"E:\coding\projects\Python\Registration Form"

    # Check if the directory exists, if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Create the file path
    file_path = os.path.join(directory, "user_details.txt")

    # Open the file in append mode and write the data
    with open(file_path, "a") as file:
        file.write(data)

    print("Details saved successfully.")

    # Clear the entry fields
    Nameentry.delete(0, END)
    Contactentry.delete(0, END)
    Addressentry.delete(0, END)
    Emailentry.delete(0, END)
    VisitPurposeentry.delete(0, END)
    checkbtn.deselect()

#heading
Label(root, text="Registration Form", font="arial 15 bold").grid(row=0, column=3)

#field name
Name = Label(root, text="Name")
Name.grid(row=1, column=2)

Contact = Label(root, text="Contact")
Contact.grid(row=2, column=2)

Address = Label(root, text="Address")
Address.grid(row=3, column=2)

Email = Label(root, text="Email")
Email.grid(row=4, column=2)

VisitPurpose = Label(root, text="Purpose of Visit")
VisitPurpose.grid(row=5, column=2)

# variable for storing data
Namevalue = StringVar()
Contactvalue = StringVar()
Addressvalue = StringVar()
Emailvalue = StringVar()
VisitPurposevalue = StringVar()
checkvalue = IntVar()

# creating entry field
Nameentry = Entry(root, textvariable=Namevalue)
Nameentry.grid(row=1, column=3)

Contactentry = Entry(root, textvariable=Contactvalue)
Contactentry.grid(row=2, column=3)

Addressentry = Entry(root, textvariable=Addressvalue)
Addressentry.grid(row=3, column=3)

Emailentry = Entry(root, textvariable=Emailvalue)
Emailentry.grid(row=4, column=3)

VisitPurposeentry = Entry(root, textvariable=VisitPurposevalue)
VisitPurposeentry.grid(row=5, column=3)

# creating checkbox
checkbtn = Checkbutton(text="Remember Me?", variable=checkvalue)
checkbtn.grid(row=6, column=3)

# submit button
Button(text="Submit", command=getvals).grid(row=7, column=3)

root.mainloop()
