from tkinter import *
from tkinter import messagebox as msg

def show():
    print(ET1.get()+" "+ET2.get())
    print("با موفقیت وارد  شدید")
    print(choice.get())
    if Check.get() == 1:
        print('اطلاعات ذخیره شد')
    else:
        print('اطلاعات ذخیره نشد')
    print(age.get())
    frist_name = ET1.get()
    LBFN.config(text=f"Frist name :{frist_name}",font=("homa",10))
    Last_name = ET2.get()
    LBLN.config(text=f"Last name :{Last_name}", font=("homa", 10))
    Gender = choice.get()
    LBG.config(text=f"Gender :{Gender}",font=("homa", 10))
    sen = age.get()
    LBA.config(text=f"Age :{sen}",font=("homa", 10))
    if Check.get() == 1:
        msg.showinfo("پیغام","اطلاعات با موفقیت ذخیره شد")
    else:
        msg.showwarning("پیغام", "اطلاعات ذخیره نشد")
win = Tk()
win.title("test")
win.geometry("500x500")
win.resizable(width=False,height=True)
win.minsize(500,500)
win.maxsize(500,550)

Label(text="نام").pack()

ET1= Entry(win)
ET1.pack()

Label(text="نام خانوادگی").pack()

ET2= Entry(win)
ET2.pack()

modes=[("male","مرد"),("female","زن")]
choice= StringVar()
choice.set("مرد")
for a,b in modes:
    Radiobutton(win,text=a , value=b ,variable=choice).pack()

age= Scale(win,from_=14,to=99,orient=HORIZONTAL)
age.pack()

Check = IntVar()
Checkbutton(win,text="ذخیره اطلاعات",variable=Check).pack()

BT1= Button(text="click")
BT1.pack()
BT1.config(font=25,bg="yellow",bd=5,width=5,height=1,command=show)

LB3= Label(text="")
LB3.pack()
LB3.config(font=10)

LBFN= Label(win)
LBFN.pack()
LBFN.config(text="")
LBLN= Label(win)
LBLN.pack()
LBG= Label(win)
LBG.pack()
LBA= Label(win)
LBA.pack()

win.mainloop()