import tkinter
from tkinter import ttk
from tkinter import messagebox

window = tkinter.Tk()
window.title("Data Entry Form")
frame = tkinter.Frame(window)
frame.pack()
def enter_data():
    accept_var.get()
    
    if accept_var.get() == "accepted":
        


        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        if first_name and last_name :
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality=nationality_combobox.get()
            sex = sex_combobox.get()
            completed_courses =numcourses_spinbox.get()
            completed_semesters = numsemesters_spinbox.get()
            registration_status = reg_status_var.get()
            terms_and_conditions = accept_var.get()
            print("First name:", first_name,"Last name:",last_name,"Title:",title,"Age:",age,"Nationality:",nationality)
            print("Sex:",sex,"Completed courses:",completed_courses,"Completed semesters:",completed_semesters)
            print("Registration status:",registration_status)
            print("..........................")
        else:
            messagebox.showwarning(title="Error",message="First name and last name are required")
    else:
        messagebox.showwarning(title="Terms and Conditions",message="You must accept the terms and conditions to proceed")


user_info_frame = tkinter.LabelFrame(frame,text = "User Information")
user_info_frame.grid(row = 0,column = 0,padx=20,pady=10)

first_name_label = tkinter.Label(user_info_frame,text = "First Name:")
first_name_label.grid(row=0,column=0)
last_name_label = tkinter.Label(user_info_frame,text = "Last Name:")
last_name_label.grid(row= 0,column=1)
first_name_entry =tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row= 1,column= 0)
last_name_entry.grid(row= 1,column= 1)
title_label = tkinter.Label(user_info_frame,text = "Title:")
title_combobox = ttk.Combobox(user_info_frame, values= [" ", "Mr","Mrs","Ms","Dr","Prof"])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)


age_label = tkinter.Label(user_info_frame,text= "Age:")
age_spinbox = tkinter.Spinbox(user_info_frame, from_ =18, to=100)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationality_label = tkinter.Label(user_info_frame,text= "Nationality:")
nationality_combobox = ttk.Combobox(user_info_frame, values= [" ","American","African","Asian","European","Australian"])
nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3,column=1)
sex_label = tkinter.Label(user_info_frame,text= "Sex:")
sex_combobox = ttk.Combobox(user_info_frame,values= ["M","F","Other"])
sex_label.grid(row=2,column=2)
sex_combobox.grid(row=3,column=2)
for Widget in user_info_frame.winfo_children():
    Widget.grid_configure(padx=10,pady=5)
    

courses_frame = tkinter.LabelFrame(frame,text="Registration details")
courses_frame.grid(row=1,column=0,sticky="news",padx=20,pady=10)

registered_label = tkinter.Label(courses_frame,text= "Registration status:")
reg_status_var = tkinter.StringVar(value="not registered")
registered_checkbutton = tkinter.Checkbutton(courses_frame,text="Currently registered",variable=reg_status_var,onvalue="registered",offvalue="not registered")
registered_label.grid(row=0,column=0)
registered_checkbutton.grid(row=1,column=0)
numcourses_label = tkinter.Label(courses_frame,text= "Completed courses:")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_ =0,to="infinity")
numcourses_label.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)
numsemesters_label = tkinter.Label(courses_frame,text= "Completed semesters:")
numsemesters_spinbox = tkinter.Spinbox(courses_frame,from_=0,to=8)
numsemesters_label.grid(row=0,column=2)
numsemesters_spinbox.grid(row=1,column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)


terms_frame_label =tkinter.LabelFrame(frame,text="Terms and Conditions")
terms_frame_label.grid(row=2,column=0,sticky="news",padx=20,pady=10)
accept_var = tkinter.StringVar(value="not accepted")
terms_checkbutton = tkinter.Checkbutton(terms_frame_label,text="I accept the terms and conditions",variable= accept_var,onvalue="accepted",offvalue="not accepted")
terms_checkbutton.grid(row=0,column=0)
button = tkinter.Button(frame,text="Enter Data",bg="blue",fg="white",command= enter_data)
button.grid(row=3,column=0,sticky="news",padx=20,pady=10)


window.mainloop()