from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()


def move():

    if fill11.get() == "" or fill22.get() == "" or fill33.get() == "" or fill44.get() == "" \
            or fill55.get() == "" or fill66.get() == "" or fill77.get() == "":
        messagebox.showerror("ERROR", "PLEASE RECALL YOUR INPUT")

    else:
        con = sqlite3.connect("Accounts.db")
        c = con.cursor()
        c.execute("INSERT INTO Accounts (name, age, birthday, religion, course, gender, address) "
                  "VALUES (?,?,?,?,?,?,?)",
                  (fill11.get(), fill22.get(), fill33.get(), fill44.get(), fill55.get(),
                   fill66.get(), fill77.get()))
        con.commit()
        con.close()
        messagebox.showinfo("SUCCESSFUL!", "YOU HAVE BEEN REGISTERED!")
        fill11.delete(0, END)
        fill22.delete(0, END)
        fill33.delete(0, END)
        fill44.delete(0, END)
        fill55.delete(0, END)
        fill66.delete(0, END)
        fill77.delete(0, END)


def form():
    paste.pack_forget()
    register.pack()


def show():
    paste.pack_forget()
    register.pack_forget()
    lists.pack()
    display()


def back1():
    register.pack_forget()
    lists.pack_forget()
    paste.place(x=0, y=0)


def back2():
    lists.pack_forget()
    register.pack_forget()
    paste.place(x=0, y=0)


def display():
    con = sqlite3.connect("Accounts.db")
    c = con.cursor()
    c.execute("SELECT * FROM Accounts")
    data = c.fetchall()
    con.close()

    listbox.delete(0, END)

    for row in data:
        listbox.insert(END, row)


window = root
window.title("STUDENT REGISTRATION FORM")
window.geometry("900x540")

paste = Frame(window)
paste.config(height=900, width=1080)
paste.config(bg="GRAY")
paste.pack()

register = Frame(paste)
register.config(bg="GRAY")
register.config(height=900, width=1080)

# FIRST BUTTONS


reg_form = Button(paste, text="STUDENT REGISTRATION", command=form)
reg_form.place(x=250, y=150)

print_list = Button(paste, text="LISTS OF STUDENT", command=show)
print_list.place(x=650, y=150)

# FRAMES AND BACK BUTTON

# FORM

register = Frame()
register.config(bg="GRAY")
register.config(height=900, width=1080)
register.pack()

title = Label(register, text="REGISTRATION FORM", font=("Arial", 20))
title.place(x=350, y=80)

fill1 = Label(register, text="ENTER YOUR NAME", font=("Arial", 10))
fill1.place(x=120, y=150)

fill11 = Entry(register)
fill11.config(width=20)
fill11.place(x=120, y=180)

fill2 = Label(register, text="ENTER YOUR AGE", font=("Arial", 10))
fill2.place(x=120, y=210)

fill22 = Entry(register)
fill22.config(width=30)
fill22.place(x=120, y=240)

fill3 = Label(register, text="ENTER YOUR BIRTHDAY", font=("Arial", 10))
fill3.place(x=120, y=270)

fill33 = Entry(register)
fill33.config(width=30)
fill33.place(x=120, y=300)

fill4 = Label(register, text="ENTER YOUR RELIGION", font=("Arial", 10))
fill4.place(x=120, y=330)

fill44 = Entry(register)
fill44.config(width=30)
fill44.place(x=120, y=360)

fill5 = Label(register, text="ENTER YOUR COURSE/COURSE TAKEN", font=("Arial", 10))
fill5.place(x=120, y=390)

fill55 = Entry(register)
fill55.config(width=30)
fill55.place(x=120, y=420)

fill6 = Label(register, text="GENDER", font=("Arial", 10))
fill6.place(x=450, y=150)

fill66 = Entry(register)
fill66.config(width=30)
fill66.place(x=450, y=180)

fill7 = Label(register, text="ADDRESS", font=("Arial", 10))
fill7.place(x=450, y=220)

fill77 = Entry(register)
fill77.config(width=30)
fill77.place(x=450, y=250)

save = Button(register, text="REGISTER", font=("Arial", 13), command=move)
save.place(x=400, y=470)

undo1 = Button(register, command=back1)
undo1.place(x=880, y=0)

# LISTS/SAVED

lists = Frame()
lists.config(bg="GRAY")
lists.config(height=900, width=1080)

listbox = Listbox(lists)
listbox.config(height=900, width=1080)
listbox.pack()

undo2 = Button(listbox, command=back2)
undo2.place(x=880, y=0)


root.mainloop()
