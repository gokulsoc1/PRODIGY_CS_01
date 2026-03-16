# PRODIGY_CS_01
# Caesar Cipher Professional Tool

The **Caesar Cipher Professional Tool** is a graphical desktop application built using **Python and Tkinter** that allows users to **encrypt and decrypt text messages** using the classical **Caesar Cipher algorithm**.

This application demonstrates how a historical cryptographic technique can be implemented in a modern **graphical user interface (GUI)** with a clean and professional design.

The tool is designed for **students, cybersecurity beginners, and programming learners** who want to understand how basic encryption algorithms work.

---

#  Project Overview

The **Caesar Cipher** is one of the oldest and simplest encryption techniques used in classical cryptography. It works by shifting letters in the alphabet by a fixed number of positions.

For example, with a shift value of **3**:

  Plaintext : HELLO
  
  Encrypted : KHOOR


Each letter moves **three positions forward** in the alphabet.

This project provides a **professional GUI interface** where users can easily:

- Enter a message
- Select a shift value
- Encrypt or decrypt the message
- View results instantly

---

#  Features

- 🔐 Encrypt text using Caesar Cipher
- 🔓 Decrypt encrypted messages
- 🖥️ Professional graphical user interface
- 📝 Multi-line message input
- 🔢 Custom shift value selection
- 📋 Clear input and output fields
- 📊 Status bar for operation feedback
- 📑 Menu system (File and Help)
- ⚠️ Error handling for invalid input
- 🎨 Clean and modern UI styling

---

# How the Caesar Cipher Works

The Caesar Cipher shifts alphabet letters using modular arithmetic.

Encryption formula:

  Encrypted Letter = (Original Letter + Shift) mod 26

Decryption formula:

  Original Letter = (Encrypted Letter - Shift) mod 26


Only alphabetical characters are shifted, while:

- Numbers
- Spaces
- Punctuation

remain unchanged.

---

#  Graphical User Interface

The application includes a clean interface with the following components:

### Title Section
Displays the name of the application.

### Message Input Box
A text area where the user enters the message to encrypt or decrypt.

### Shift Value Field
Allows the user to enter the numeric shift value.

### Action Buttons

- **Encrypt** – Converts plaintext into ciphertext
- **Decrypt** – Converts ciphertext back into plaintext
- **Clear** – Clears all input and output fields

### Result Output Box
Displays the encrypted or decrypted message.

### Status Bar
Shows application messages such as:

- Operation completed
- Fields cleared
- Ready state

---

The entire application logic and interface are implemented in a single Python file.

---

# 🧰 Technologies Used

| Technology | Purpose |
|------------|--------|
| Python | Core programming language |
| Tkinter | Graphical user interface |
| ttk | Modern themed widgets |
| MessageBox | User notifications |
| Text Widgets | Multi-line input and output |

---

# ⚙️ Requirements

To run this project you need:

- **Python 3.x**
- Tkinter (usually pre-installed with Python)

No external libraries are required.

---



