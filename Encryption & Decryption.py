import tkinter as tk

# Function to encrypt the message
def encrypt_message():
    message = entry_message.get()
    encrypted_message = ''

    for char in message:
        encrypted_message += chr(ord(char) + 3)  # Shift each character by 3 positions

    entry_encrypted.delete(0, tk.END)
    entry_encrypted.insert(0, encrypted_message)
    show_hide_button.grid(row=1, column=3, padx=5, sticky="w")

# Function to decrypt the message
def decrypt_message():
    encrypted_message = entry_encrypted.get()
    decrypted_message = ''

    for char in encrypted_message:
        decrypted_message += chr(ord(char) - 3)  # Shift each character back by 3 positions

    entry_decrypted.delete(0, tk.END)
    entry_decrypted.insert(0, decrypted_message)
    show_hide_button.grid_forget()

# Function to show/hide text in the encrypted message box
def show_hide_message():
    if show_hide_button.config('text')[-1] == 'Show':
        entry_encrypted.config(show="")
        show_hide_button.config(text="Hide")
    else:
        entry_encrypted.config(show="*")
        show_hide_button.config(text="Show")

# Function to toggle between light and dark themes
def toggle_theme():
    global dark_theme

    if dark_theme:
        root.config(bg="white")
        label_message.config(bg="white", fg="black")
        label_encrypted.config(bg="white", fg="black")
        label_decrypted.config(bg="white", fg="black")
        entry_message.config(bg="white", fg="black")
        entry_encrypted.config(bg="white", fg="black")
        entry_decrypted.config(bg="white", fg="black")
        button_encrypt.config(bg="#4CAF50", fg="white", activebackground="#4CAF50", activeforeground="white")
        button_decrypt.config(bg="#FF5722", fg="white", activebackground="#FF5722", activeforeground="white")
        show_hide_button.config(bg="white", fg="black")
        theme_button.config(text="Dark Theme", bg="#f0f0f0", fg="black", width=8)
    else:
        root.config(bg="#121212")
        label_message.config(bg="#121212", fg="white")
        label_encrypted.config(bg="#121212", fg="white")
        label_decrypted.config(bg="#121212", fg="white")
        entry_message.config(bg="#121212", fg="white")
        entry_encrypted.config(bg="#121212", fg="white")
        entry_decrypted.config(bg="#121212", fg="white")
        button_encrypt.config(bg="#388E3C", fg="white", activebackground="#388E3C", activeforeground="white")
        button_decrypt.config(bg="#D32F2F", fg="white", activebackground="#D32F2F", activeforeground="white")
        show_hide_button.config(bg="#121212", fg="white")
        theme_button.config(text="Light Theme", bg="#1E88E5", fg="white", width=8)

    dark_theme = not dark_theme

# Create the main window
root = tk.Tk()
root.title("Secret Message Encryption & Decryption Tool")
root.geometry("500x350")
root.config(bg="white")

# Light theme colors
light_bg = "white"
light_fg = "black"

# Dark theme colors
dark_bg = "#121212"
dark_fg = "white"

# Flag for current theme
dark_theme = False

# Create labels
label_message = tk.Label(root, text="Enter your message:", font=("Helvetica", 12), bg=light_bg, fg=light_fg)
label_encrypted = tk.Label(root, text="Encrypted message:", font=("Helvetica", 12), bg=light_bg, fg=light_fg)
label_decrypted = tk.Label(root, text="Decrypted message:", font=("Helvetica", 12), bg=light_bg, fg=light_fg)

# Create entry fields
entry_message = tk.Entry(root, width=30, font=("Helvetica", 12), bg=light_bg, fg=light_fg)
entry_encrypted = tk.Entry(root, width=30, font=("Helvetica", 12), show="*", bg=light_bg, fg=light_fg)
entry_decrypted = tk.Entry(root, width=30, font=("Helvetica", 12), bg=light_bg, fg=light_fg)

# Create frame for encrypt/decrypt buttons
button_frame = tk.Frame(root, bg=light_bg)
button_frame.grid(row=3, column=0, columnspan=2, pady=10)

# Create buttons
button_encrypt = tk.Button(button_frame, text="Encrypt", command=encrypt_message, font=("Helvetica", 12), bg="#4CAF50", fg="white", activebackground="#4CAF50", activeforeground="white")
button_decrypt = tk.Button(button_frame, text="Decrypt", command=decrypt_message, font=("Helvetica", 12), bg="#FF5722", fg="white", activebackground="#FF5722", activeforeground="white")
show_hide_button = tk.Button(root, text="Hide", command=show_hide_message, bg="white", fg="black")

# Theme toggle button
theme_button = tk.Button(root, text="Dark Theme", command=toggle_theme, bg="#f0f0f0", fg="black", bd=0, highlightthickness=0, width=8)

# Layout
label_message.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
label_encrypted.grid(row=1, column=0, padx=10, pady=5, sticky="w")
label_decrypted.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_message.grid(row=0, column=1, padx=10, pady=(10, 5))
entry_encrypted.grid(row=1, column=1, padx=10, pady=5)
entry_decrypted.grid(row=2, column=1, padx=10, pady=5)
button_encrypt.grid(row=0, column=0, padx=(0, 5), sticky="ew")
button_decrypt.grid(row=0, column=1, padx=(5, 0), sticky="ew")
show_hide_button.grid(row=1, column=3, padx=5, sticky="w")
theme_button.grid(row=4, column=0, columnspan=2, pady=(10, 0), padx=10, sticky="ew")

# Run the application
root.mainloop()
