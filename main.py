import os
import random
import datetime
import tkinter as tk
from tkinter import messagebox

def generate_password():

    letters_small = "abcdefghijklmnopqrstuvwxyz"
    letters_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_chars = "!@#$%^&*()_+{}[]|:;<>,.?/~`"

    try:
        user_input = int(entry_length.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")
        return
    
    if user_input < 8:
        output_var.set("\nPassword length must be at least 8 characters!\n")
        return

    title = entry_title.get()
    if(not title):
        output_var.set("Please enter a title.")
        return
    
    password = []
    for _ in range(user_input):    

        i = random.randint(0, 3)
        match i:
            case 0:
                password.append(random.choice(letters_small))
            case 1:
                password.append(random.choice(letters_big))
            case 2: 
                password.append(random.choice(numbers))
            case 3: 
                password.append(random.choice(special_chars))

    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("date: %Y-%m-%d\ntime: %H:%M")

    generate_password = ''.join(password)
    output_var.set(f"Password created for {title}\npassword: {generate_password}\n{formatted_time}")

    home_directory = os.path.expanduser("~")
    file_path = os.path.join(home_directory, "randPwd.txt")

    with open("randPwd.txt", "a") as file:
        file.write(f"FOR: {title}\npassword: {generate_password}\n{formatted_time}\n\n")

    messagebox.showinfo("Info", "Password created successfully!")

def copy_to_clipboard():
    generated_password = output_var.get()
    if "password:" in generated_password:
        try:
            # Şifre kısmını ayıkla
            password = generated_password.split("password:")[1].split("\n")[0].strip()
            root.clipboard_clear()
            root.clipboard_append(password)
            root.update()  # Panoyu güncelle
            messagebox.showinfo("Info", "Password copied to clipboard!")
        except IndexError:
            messagebox.showerror("Error", "Unexpected password format!")
    else:
        output_var.set("No password to copy!")
        
def reset_fields(): 
    entry_length.delete(0, tk.END)
    entry_title.delete(0,tk.END)
    output_var.set("")


root = tk.Tk()
root.title("Password Generator")

label_length = tk.Label(root, text = "Enter a number for password length: ")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()

label_title = tk.Label(root, text="Enter a title: ")
label_title.pack()

entry_title = tk.Entry(root)
entry_title.pack()

output_var = tk.StringVar()
label_output = tk.Label(root, textvariable= output_var, height=4, wraplength=300, justify="center")
label_output.pack(pady=5)

generate_button = tk.Button(root, text= "Generate Password: ", command=generate_password, bg="lightgreen")
generate_button.pack(pady=3)

copy_button = tk.Button(root, text="Copy Password", command=copy_to_clipboard, bg="lightblue")
copy_button.pack(pady=3)

reset_button = tk.Button(root, text="Reset", command=reset_fields, bg="lightcoral")
reset_button.pack(pady=3)


root.mainloop()