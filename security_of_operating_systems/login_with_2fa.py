import os
import tkinter as tk
from tkinter import messagebox
import pyotp
import segno
import bcrypt

def create_qr_code(secret):
    qr = segno.make_qr(f'otpauth://totp/agh:example@gmail.com?secret={secret}&issuer=TestAPP')
    qr.save("test_qrcode.png")
    messagebox.showinfo("Register App", "Register app using QR code saved in file: test_qrcode.png")

def on_destroy():
    try:
        os.remove("test_qrcode.png")
    except FileNotFoundError:
        pass

def register_new_otp(secret):
    global isOPTRegistered
    create_qr_code(secret)
    isOPTRegistered = True

def login(secret, username_entry, password_entry, id_entry, hashed_password):
    if not isOPTRegistered:
        messagebox.showerror("OTP", "REGISTER OTP FIRST")
        return
    
    validator = pyotp.TOTP(secret)
    valid = validator.verify(id_entry.get())
    user_input = username_field.get()
    password_input = password_field.get().encode('utf-8')

    if user_input == USERNAME and bcrypt.checkpw(password_input, hashed_password) and valid:
        messagebox.showinfo("Login Status", "Logged in!")
    else:
        messagebox.showinfo("Login Status", "Not Logged in!")
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    on_destroy()

USERNAME = 'agh'
PASSWORD_HASH = "$2a$12$TET1g55hZP51FtEqs3bXWO7FwOLF.I4H8BD5DkmLcs8udCCF5wvrW" # ! normally hash would be stored in database without password in cleartext !
SECRET = pyotp.random_base32()
isOPTRegistered = False  # Flag to check if OTP is registered

root = tk.Tk()
root.geometry('600x400+20+20')
root.title("Login Window")

tk.Label(root, text="Username").grid(row=0)
tk.Label(root, text="Password").grid(row=1)
tk.Label(root, text="ID").grid(row=2)

username_field = tk.Entry(root)
password_field = tk.Entry(root, show="*")
id_field = tk.Entry(root)

username_field.grid(row=0, column=1)
password_field.grid(row=1, column=1)
id_field.grid(row=2, column=1)

login_button = tk.Button(root, text="Login", command=lambda: login(SECRET, username_field, password_field, id_field, PASSWORD_HASH))
login_button.grid(row=4, columnspan=2)

register_button = tk.Button(root, text="Register a New ID", command=lambda: register_new_otp(SECRET))
register_button.grid(row=5, columnspan=2)

root.mainloop()
