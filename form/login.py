from tkinter import *
root = Tk()

root.geometry("500x300")

def getvals():
    print("Accepted")

# Heading
Label(root, text="Registration Form", font="ar 15 bold").grid(row=0, column=3)

# Field name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmode = Label(root, text="Payment mode")

# Packing field
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmodevalue = StringVar
checkvalue = IntVar

# Entry field for variables
name_entry = Entry(root, textvariable=namevalue)
phone_entry = Entry(root, textvariable=phonevalue)
gender_entry = Entry(root, textvariable=gendervalue)
emergency_entry = Entry(root, textvariable=emergencyvalue)
paymentmode_entry = Entry(root, textvariable=paymentmodevalue)

# Packing entry fields
name_entry.grid(row=1,column=3)
phone_entry.grid(row=2,column=3)
gender_entry.grid(row=3,column=3)
emergency_entry.grid(row=4,column=3)
paymentmode_entry.grid(row=5,column=3)

# checkbox
check_button = Checkbutton(text="remember me", variable=checkvalue)
check_button.grid(row=6, column=3)

#Submit button
Button(text="Submit", command=getvals).grid(row=7, column=3)

root.mainloop()
