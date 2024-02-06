from tkinter import *

# define the encryption function
def encrypt(plaintext, shift):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            ciphertext += char
    return ciphertext

# define the decryption function
def decrypt(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                plaintext += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plaintext += char
    return plaintext

# define the GUI
class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Encryption/Decryption App")
        self.grid(sticky="nsew")
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        # create the title label
        self.title_label = Label(self, text="Encryption <> Decryption", font=('Arial', 20, 'bold'), bg='#f2f2f2')
        self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        # create the input text box
        self.input_label = Label(self, text="Enter text:", font=('Arial', 12), bg='#f2f2f2')
        self.input_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.input_text = Text(self, height=5, width=50, font=('Arial', 12), relief="flat")
        self.input_text.grid(row=2, column=0, padx=10, pady=10)

        # create the key text box
        self.key_label = Label(self, text="Enter shift key (1-25):", font=('Arial', 12), bg='#f2f2f2')
        self.key_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.key_text = Entry(self, width=50, font=('Arial', 12), relief="flat")
        self.key_text.grid(row=4, column=0, padx=10, pady=10)

        # create the encrypt button
        self.encrypt_button = Button(self, text="Encrypt", command=self.encrypt_data, font=('Arial', 12, 'bold'), bg='#008CBA', fg='white', relief="flat")
        self.encrypt_button.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        # create the output text box
        self.output_label = Label(self, text="Encrypted/Decrypted text:", font=('Arial', 12), bg='#f2f2f2')
        self.output_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.output_text = Text(self, height=5, width=50, font=('Arial', 12), relief="flat")
        self.key_text.grid(row=4, column=0, padx=10, pady=10)

         # create the decrypt button
        self.decrypt_button = Button(self, text="Decrypt", command=self.decrypt_data, font=('Arial', 12, 'bold'), bg='#008CBA', fg='white', relief="flat")
        self.decrypt_button.grid(row=7, column=0, padx=10, pady=10, sticky="w")

    # define the encrypt_data method
    def encrypt_data(self):
        plaintext = self.input_text.get("1.0", "end-1c")
        shift = int(self.key_text.get())
        ciphertext = encrypt(plaintext, shift)
        self.output_text.delete("1.0", END)
        self.output_text.insert(END, ciphertext)

    # define the decrypt_data method
    def decrypt_data(self):
        ciphertext = self.output_text.get("1.0", "end-1c")
        shift = int(self.key_text.get())
        plaintext = decrypt(ciphertext, shift)
        self.input_text.delete("1.0", END)
        self.input_text.insert(END, plaintext)

# create the GUI
root = Tk()
app = App(master=root)
app.mainloop()
