import tkinter as tk
from cryptography.fernet import Fernet

# create the key
key = Fernet.generate_key()

# start the object Fernet with the key
fernet = Fernet(key)

# encrypt the message
def encrypt_message():
    message = input_box.get("1.0", tk.END).encode()
    encrypted_message = fernet.encrypt(message)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, encrypted_message)

# decrypt the message
def decrypt_message():
    message = input_box.get("1.0", tk.END).encode()
    decrypted_message = fernet.decrypt(message)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, decrypted_message)

# create the window
window = tk.Tk()
window.title("Cryptography")

# input and output boxes
input_box = tk.Text(window, height=5, width=50)
input_box.grid(row=0, column=0)

output_box = tk.Text(window, height=5, width=50)
output_box.grid(row=1, column=0)

# encrypt and decrypt buttons
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_message)
encrypt_button.grid(row=0, column=1)

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_message)
decrypt_button.grid(row=1, column=1)

# open the window
window.mainloop()


