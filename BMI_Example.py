from tkinter import *
from math import *

def calculateBMI(event):
    height = float(textBoxHeight.get())
    weight = float(textBoxWeight.get())
    height = height/100
    bmi = weight/pow(height,2)
    Label(mainWindow,text = "BMI = %.2f"%(bmi),fg = "red",font=("iannnnn-DOG-Regular",18)).grid(row=2,column=1)
    Label(mainWindow,text = "ผลลัพธ์",font=("iannnnn-DOG-Regular")).grid(row=3,column=0)
    if bmi>=30.0:
        Label(mainWindow,text = "อ้วนมาก",width = 20,fg = "red",font=("iannnnn-DOG-Regular",18)).grid(row=3,column=1)
    elif bmi>=25.0:
        Label(mainWindow,text = "อ้วน",width = 20,fg = "orange",font=("iannnnn-DOG-Regular",18)).grid(row=3,column=1)
    elif bmi>=23.0:
        Label(mainWindow,text = "นํ้าหนักเกิน",width = 20,fg = "yellow",font=("iannnnn-DOG-Regular",18)).grid(row=3,column=1)
    elif bmi>=18.6:
        Label(mainWindow,text = "นํ้าหนักปกติ เหมาะสม",width = 20,fg = "green",font=("iannnnn-DOG-Regular",18)).grid(row=3,column=1)
    else:
        Label(mainWindow,text = "ผอมเกินไป",width = 20,fg = "#9bc1bc",font=("iannnnn-DOG-Regular",18)).grid(row=3,column=1)


mainWindow = Tk()
labelHeight = Label(mainWindow,text="ส่วนสูง (Cm.)")
labelHeight.grid(row=0,column=0)

textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(mainWindow,text="นํ้าหนัก (Kg.)")
labelWeight.grid(row=1,column=0)

textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(mainWindow,text = "คำนวณ")
calculateButton.grid(row=2)
calculateButton.bind('<Button-1>',calculateBMI)

mainWindow.mainloop()