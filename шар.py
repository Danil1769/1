from tkinter import *
from tkinter import messagebox
import random

a=('да','нет','наверное')

def random_one():
    random.randint(0,2)
    messagebox.showinfo()
root=Tk()
root.title('магический шар')
root.geometry('1000x500')
p=Button(root,text='встряхнуть',width='20', height='15',bg='yellow',command=random_one)
p.pack()
        
root.mainloop