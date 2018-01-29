from tkinter import *

root = Tk()

frame = Frame(root, width=300, height=250, bg="black")
frame.pack()

label_1 = Label(root, text="Weather", fg="purple")
label_2 = Label(root, text="Calender And TODO", fg="purple")
label_3 = Label(root, text="News", fg="purple")


label_1.pack(side=TOP)
label_2.pack(side=RIGHT)
label_3.pack(side=BOTTOM)


root.mainloop()
