from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import smtplib


def fill_form():
    global form
    global mo_no,Email,Name

    form = Tk()
    form.title("Form Page")
    form.geometry("500x250")

    Ln = Label(form, width=20, text="")
    Ln.grid(column=0, row=0)
    Lm = Label(form, width=20, text="")
    Lm.grid(column=0, row=3)
    L1 = Label(form,bg='dim gray', width=20, text="FULL NAME")
    L1.grid(column=0, row=2)
    Name = Entry(form, bd=10, width=30)
    Name.grid(column=2, row=2)
    L2 = Label(form,bg='dim gray',width=20, text="MOBILE NO")
    L2.grid(column=0, row=4)
    mo_no = Entry(form, bd=10, width=30)
    mo_no.grid(column=2, row=4)
    Ln = Label(form, width=20, text="")
    Ln.grid(column=0, row=5)
    L3 = Label(form,bg='dim gray', width=20, text="EMAIL ID")
    L3.grid(column=0, row=6)
    Email = Entry(form, bd=10, width=30)
    Email.grid(column=2, row=6)
    Ln = Label(form, width=20, text="")
    Ln.grid(column=0, row=7)

    B1 = Button(form, text="SUBMIT",bg='deepskyblue3', width=15, command=login1)
    B1.grid(column=1, row=8)

    form.mainloop()


def login1():
    global name
    name = Name.get()
    msg1 = f"{name} You Must Use The Your Email And Mobile Number As A Username And Password"
    showinfo(title='University Login', message=msg1)
    global mo,Email1,login
    mo = str(mo_no.get())
    Email1 = str(Email.get())
    # form.destroy()
    login = Tk()
    login.title("Login Page")
    login.geometry("500x250")
    global E1,E2

    Ln = Label(login, width=20, text="")
    Ln.grid(column=0, row=0)
    Lm = Label(login, width=20, text="")
    Lm.grid(column=2, row=0)
    L1 = Label(login,bg='dim gray', width=20, text="USERNAME")
    L1.grid(column=0, row=1)
    E1 = Entry(login, bd=10, width=30)
    E1.grid(column=2, row=1)
    L2 = Label(login,bg='dim gray',width=20, text="PASSWORD")
    L2.grid(column=0, row=2)
    E2 = Entry(login, bd=10, width=30)
    E2.grid(column=2, row=2)
    L2 = Label(login, text="")
    L2.grid(column=1, row=3)

    B1 = Button(login,bg='cadet blue', text="LOGIN",width=15,command=auth)
    B1.grid(column=1, row=4)

    login.mainloop()

def auth():
    # mo = str(mo_no.get())

    Email1 = str(Email.get())
    if E1.get() == Email1 and E2.get() == str(mo):
        print('login....')
        booking()
    else:
        print('failed')

def booking():
    global window
    window = Tk()
    window.title('Booking Page')
    window.geometry('500x500')

    global city,theatchoosen,Schoosen,Stime,ticket

    L1 = Label(window, bg='dim gray', width=20, text="Enter City", font=("Times New Roman", 10))
    L1.grid(column=0, row=0, padx=25, pady=30)
    city = Entry(window, bd=10, width=25)
    city.grid(column=1, row=0)

    L2 = Label(window,bg='dim gray',text="Select the Theater :", width=20,font=("Times New Roman", 10))
    L2.grid(column=0,row=1, padx=10, pady=25)
    n = tk.StringVar()
    theatchoosen = ttk.Combobox(window, width=27, textvariable=n)
    theatchoosen['values'] = ('PVR','INOX','ICON','PVS')
    theatchoosen.grid(column=1, row=1)
    theatchoosen.current()

    L3 = Label(window, bg='dim gray', text="Select the Screen :", width=20, font=("Times New Roman", 10))
    L3.grid(column=0, row=2, padx=10, pady=25)
    n = tk.StringVar()
    Schoosen = ttk.Combobox(window, width=27, textvariable=n)
    Schoosen['values'] = ('SCREEN1', 'SCREEN2', 'SCREEN3')
    Schoosen.grid(column=1, row=2)
    Schoosen.current()

    L4 = Label(window, bg='dim gray', text="Select the Timing :", width=20, font=("Times New Roman", 10))
    L4.grid(column=0, row=3, padx=10, pady=25)
    n = tk.StringVar()
    Stime = ttk.Combobox(window, width=27, textvariable=n)
    Stime['values'] = ('7AM-10AM', '10.30AM-12.30PM', '12.30PM-3.30PM','3.30PM-6.30PM','6.30PM-9.30PM')
    Stime.grid(column=1, row=3)
    Stime.current()

    L4 = Label(window, bg='dim gray', width=23, text="How Many Ticket(150/person)", font=("Times New Roman", 10))
    L4.grid(column=0, row=4, padx=25, pady=30)
    ticket = Entry(window, bd=10, width=25)
    ticket.grid(column=1, row=4)

    B1 = Button(window, bg='cadet blue', text="SUBMIT", width=25, command=send)
    B1.grid(column=1, row=5, pady=30)

    window.mainloop()

def send():
    global Email1,name
    Email1 = str(Email.get())
    city1 = city.get()
    theatchoosen1 = theatchoosen.get()
    Schoosen1 = Schoosen.get()
    Stime1 = Stime.get()
    ticket1 = int(ticket.get())

    price = 150*ticket1

    msg1 = f"{name} Your Data Is Send On Registered Email ID And Your Amound is {price} For {ticket1} Person"
    showinfo(title='University Login', message=msg1)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication

    s.login("aniketratnaparakhi5354@gmail.com", "Aniket@9834")
    
    message = f"{name} Your Show City Name is {city1} in {theatchoosen1} Theater {Schoosen1} And Time On  {Stime1} And {ticket1} " \
              f"Ticket is Booked \n" \
              f"Your Total Amound Is {price} for {ticket1} Person"

    s.sendmail("aniketratnaparakhi5354@gmail.com", Email1, message)

    # terminating the session
    s.quit()
    form.destroy()
    login.destroy()
    window.destroy()


fill_form()
