from tkinter import *

root = Tk() #Always the 1st thing you do with tKinter

# PACK ***************************************************************************
    # myLabel = Label(root, text="Hello World")
    # # Push to screen
    # myLabel.pack()
    # # Event loop to check change screem events EG. mosue movement ro clicks
    # # the keep going until programme ends

# GRID ***************************************************************************
    # Could place the grid statement at the end but cleaner this way
    # myLabel1 = Label(root, text="Hello World")  # .grid(row=0, column=0) how the code looks added on
    # myLabel2 = Label(root, text="My Name is Lawrie")
    # myLabel1.grid(row=0, column=0)
    # myLabel2.grid(row=0, column=1)

# BUTTONS ***********************************************************************

    # def myClick():
    #     myLabel=Label(root, text="I clicked a button")
    #     myLabel.pack()

    # myButton=Button(root, text="Push Me", padx=50, pady=20, command=myClick, fg="blue") #state=DISABLED 
    #     #command calls function do not use() fg="color" bg="background color" colr name or HEX Codes #FFFFFF
    # myButton.pack()

# INPUT BOXES *****************************************************************

# ent=Entry(root, width=50, fg="#ffffff", bg="#000000", borderwidth="5")  #Input Box
# # the function to extract the text from the box for use ** ent.get()
# ent.pack()
# ent.insert(0, "Enter you Name")  # Index, default value

# def myClick():
#     hello = "Hello " + ent.get()
#     myLabel=Label(root, text=hello)
#     myLabel.pack()

# myButton=Button(root, text="Enter Your Name", padx=50, pady=20, command=myClick, fg="blue") #state=DISABLED 
#     #command calls function do not use() fg="color" bg="background color" colr name or HEX Codes #FFFFFF
# myButton.pack()

# Columnspan ******************************************************************

width = 3

label1 = Label(root, text='1 columns wide')
label2 = Label(root, text='%i columns wide' % width)

label1.grid(row=0, column=0, padx=30)
label2.grid(row=0,column=1, columnspan=width)
for i in range(width+1):
    root.grid_columnconfigure(i, weight=1, uniform="foo")

# Note that with only these two labels, you could achieve 
# the same layout by adjusting the width of column 
# 1. Differences will occur still while you populate column 2,3,4...

label2.grid(row=0,column=1) #no columnspan
root.grid_columnconfigure(0, weight=1, uniform="foo")
root.grid_columnconfigure(1, weight=width, uniform="foo")

root.mainloop()



