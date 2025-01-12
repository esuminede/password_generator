import tkinter as tk
from generate_password import generate_password, reset_fields

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
reset_button = tk.Button(root, text="Reset", command=reset_fields, bg="lightcoral")
reset_button.pack(pady=3)

root.mainloop()