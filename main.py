from tkinter import *
from random import randint

root = Tk()
root.geometry('420x280')
root.title('random number')
root['bg'] = 'green'


n = ''

def random():
    global n
    n = (randint(1, 10000))
    text1.configure(text=n)


def clearTextInput():
   text1.config(text='')

text1 = Label(root,font='Arial 13 bold',width=80,height=3)
text1.pack()

btn = Button(root,text='Сгенерировать',font='Arial 13 bold',height=5,width=20,command=random)
btn.pack()

btn1 = Button(root,text='Очистить',font='Arial 13 bold',height=5,width=20,command=clearTextInput)
btn1.pack(padx=10)

root.mainloop()
