from tkinter import *
import os
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



def generate():
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    #print(f"Your password is: {password}")
        
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    website_info = website_entry.get()
    password_info = password_entry.get()
    email_info = email_username_entry.get()
    
    
    if len(website_info) == 0:
        error_message = messagebox.showerror(title='Text', message='Please fill out the website information.')    
    
    if len(email_info) == 0:
        error_message = messagebox.showerror(title='Text', message='Please fill out the Email/Username information.')    

    
    if len(password_info) == 0:
        error_message = messagebox.showerror(title='Text', message='Please fill out the password information.')
        
    

    elif len(password_info) and len(website_info) and len(email_info) >= 1:
        
        
        is_ok = messagebox.askokcancel(title=website_info, message=f'These are the details entered: \nEmail: {email_info} \nPassword: {password_info} \nIs it ok to save?')
        if is_ok == True:
            
            folder_path = os.getcwd()
            filename = 'data.txt'
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, 'a') as file:
                file.write(f'Website: {website_info} \nEmail: {email_info} \nPassword: {password_info} \n \n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()
            
        



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightcolor='Black', highlightthickness=1)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=photo)
canvas.grid(column=1, row=0)


#website
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

#email/username
email_username_label = Label(text='Email/Username:')
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=40)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "john.aldrin.rivero@gmail.com")

#password
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_entry = Entry(text = "", width=22)
password_entry.grid(column=1, row=3)


#generate button
generate_button = Button(text='Generate Password', command=generate)
generate_button.grid(column=2, row=3)



#add button
add_button = Button(text="Add", width=35, command=add )
add_button.grid(column=1, row=4, columnspan=2)











































window.mainloop()