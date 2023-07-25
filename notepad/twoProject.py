from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog as f

def login():
    print("hi")
    msg.showinfo("info","خوش آمدید")
def logout():
    print("bye")
    x=msg.askyesnocancel("هشدار","آیا میخواهید از اکانت خود خارج شوید؟")
    if x:
        print("bye")
        msg.showinfo("info","خدانگهدار")
def quit():
    a=msg.askyesno("خروج از برنامه","آیا میخواهید از برنامه خارج شوید")
    if a:
        win.quit()
def save_file():
    save_files = f.asksaveasfile(mode="w",defaultextension=".txt")
    txt=text1.get(1.0,END)
    save_files.write(txt)
    save_files.close()
    msg.showinfo("save","با موفقیت ذخیره شد")

def open_file():
    open_files = f.askopenfile(mode="r")
    text1.insert(INSERT,open_files.read())
    open_files.close()
    msg.showinfo("open","فایل با موفقیت باز شد")
def clear_file():
    text1.delete(1.0,END)

win = Tk()
win.title("notepad")
win.geometry("800x500")
menu1= Menu(win)

profile_menu=Menu(menu1,tearoff=0)
profile_menu.add_command(label="login",command=login)
profile_menu.add_command(label="logout",command=logout)


menu1.add_cascade(label="login",menu=profile_menu)

file_menu=Menu(menu1,tearoff=0)
file_menu.add_command(label="open",command=open_file)
file_menu.add_command(label="save",command=save_file)


menu1.add_cascade(label="file",menu=file_menu)

menu1.add_command(label="clear",command=clear_file)

menu1.add_command(label="exit",command=quit)
win.config(menu=menu1)

text1= Text(win)
text1.pack(fill="both",expand=True)

win.mainloop()