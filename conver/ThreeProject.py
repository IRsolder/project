from tkinter import *
from tkinter import Listbox
from germ_class import *

def Tabdil():
    data_from = List_from.get(ACTIVE)
    data_to = List_to.get(ACTIVE)
    value = int(EN_from.get())
    ojb= Germ(data_from,data_to,value)
    EN_to.delete(0,END)
    EN_to.insert(END,ojb.Germ())



win= Tk()
win.title("مبدل")
win.resizable(0,0)

Label(win,text="from").grid(row=0,column=0,sticky=W,padx=5)
EN_from= Entry(win)
EN_from.grid(row=1,column=0,sticky=W,padx=5,pady=2)
List_from= Listbox(win,exportselection=False)
List_from.grid(row=2,column=0,sticky=W,padx=5,pady=5,)
List_from.insert(END,"gr")
List_from.insert(END,"kg")
List_from.insert(END,"ton")

Label(win,text="to").grid(row=0,column=1,sticky=W,padx=5)
EN_to= Entry(win)
EN_to.grid(row=1,column=1,sticky=E,padx=5,pady=2)
List_to= Listbox(win,exportselection=False)
List_to.grid(row=2,column=1,sticky=E,padx=5,pady=5)
List_to.insert(END,"gr")
List_to.insert(END,"kg")
List_to.insert(END,"ton")

BT=Button(win,text="تبدیل",command=Tabdil)
BT.grid(row=3,column=0,padx=5,pady=5,columnspan=2,sticky=W+E)


win.mainloop()