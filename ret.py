import tkinter
from tkinter import messagebox


window = tkinter.Tk()
window.title("login form")
window.geometry("300x200")
window.configure(bg = "lavender")

def login():
    username = "siryeedmase@gmail.com" or "john26"
    password = "bway17"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title ="login success",message = "you have successfully logged in")
    else:
        messagebox.showerror(title = "login failed",message = "invalid username or password")

frame = tkinter.Frame(window,bg = "lavender")

login_label = tkinter.Label(frame,text = "login",bg ="lavender",fg ="red",font = ("Arial",32))
username_label = tkinter.Label(frame,text = "username or email:",bg = "lavender",fg = "red",font = ("Arial",16))
username_entry = tkinter.Entry(frame,font =("Arial",16))
password_label = tkinter.Label(frame,text = "password:",bg ="lavender",fg = "red",font =("Arial",16))
password_entry = tkinter.Entry(frame,show = "*",font= ("Arial",16))
login_button = tkinter.Button(frame,text = "login", bg = "blue", fg = "white",font=("Arial",16),command=login)


login_label.grid(row = 0,column = 0, columnspan=2,sticky = "news",pady =16)
username_label.grid(row = 1, column = 0,sticky= "news")
username_entry.grid(row = 1,column = 1,pady = 8)
password_label.grid(row = 2,column = 0,sticky = "news")
password_entry.grid(row = 2,column = 1,pady =8)
login_button.grid(row = 3,column = 0,columnspan=2)

frame.pack()

window.mainloop()
