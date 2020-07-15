# अनुवादक

from tkinter import *

screen = Tk()
screen.title('अनुवादक') #name of calculator
screen.configure(bg = 'gray') #backgroud colour of calc
screen.geometry('500x400')

##making of Entry box
var1 = StringVar()
b1 = Entry(screen,width=25,textvariable = var1, font=('arial',15,'bold'))
b1.place(x=200,y=40)


var2 = StringVar()
b2 = Entry(screen,width=25,textvariable = var2, font=('arial',15,'bold'),relief = 'ridge')
b2.place(x=200,y=100)

### Text Labels
lab1= Label(screen,text = 'Enter Text',font=('arial',15,'bold'),bg='gray')
lab1.place(x=5,y=40)

lab2= Label(screen,text = 'Translated Text',font=('arial',15,'bold'),bg='gray')
lab2.place(x=5,y=100)

lab3= Label(screen,text = ' ',font=('arial',15,'bold'),bg='gray')
lab3.place(x=5,y=250)

#### Buttons



screen.mainloop()