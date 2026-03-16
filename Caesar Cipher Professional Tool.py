import tkinter as tk
from tkinter import ttk, messagebox

"""
 you need to install python pip packages.
 the code run perfectly

"""
# ---------------- LOGIC ----------------
def caesar_cipher(text, shift, mode):
    shift %= 26
    result = ""

    for char in text:
        if char.isupper():
            base = ord('A')
            result += chr((ord(char) - base + (shift if mode == "encrypt" else -shift)) % 26 + base)
        elif char.islower():
            base = ord('a')
            result += chr((ord(char) - base + (shift if mode == "encrypt" else -shift)) % 26 + base)
        else:
            result += char

    return result


def process(mode):
    try:
        text = input_box.get("1.0", tk.END).strip()
        shift = int(shift_entry.get())

        if not text:
            messagebox.showwarning("Input Required", "Please enter a message.")
            return

        result = caesar_cipher(text, shift, mode)

        output_box.config(state="normal")
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)
        output_box.config(state="disabled")

        status.set(f"Operation completed: {mode.title()}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")


def clear_all():
    input_box.delete("1.0", tk.END)
    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.config(state="disabled")
    shift_entry.delete(0, tk.END)
    status.set("Cleared all fields")


# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Caesar Cipher | Professional Tool")
root.geometry("720x560")
root.resizable(False, False)

# ---------------- STYLE ----------------
style = ttk.Style()
style.theme_use("clam")

style.configure("App.TFrame", background="#f4f6f8")
style.configure("Card.TFrame", background="white")
style.configure("Title.TLabel", font=("Segoe UI", 22, "bold"))
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 11), padding=8)

# ---------------- MENU ----------------
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Clear", command=clear_all)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo(
    "About",
    "Caesar Cipher Tool\n\nBuilt using Python & Tkinter\nProfessional UI Version"
))

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)
root.config(menu=menu_bar)

# ---------------- MAIN FRAME ----------------
main = ttk.Frame(root, style="App.TFrame", padding=20)
main.pack(fill="both", expand=True)

card = ttk.Frame(main, style="Card.TFrame", padding=25)
card.pack(fill="both", expand=True)

# ---------------- TITLE ----------------
ttk.Label(card, text="Caesar Cipher", style="Title.TLabel").pack(pady=(0, 20))

# ---------------- INPUT ----------------
ttk.Label(card, text="Message").pack(anchor="w")
input_box = tk.Text(card, height=6, font=("Consolas", 11), wrap="word")
input_box.pack(fill="x", pady=(5, 15))

# ---------------- SHIFT ----------------
shift_frame = ttk.Frame(card)
shift_frame.pack(anchor="w", pady=5)

ttk.Label(shift_frame, text="Shift Value:").pack(side="left")
shift_entry = ttk.Entry(shift_frame, width=10)
shift_entry.pack(side="left", padx=10)

# ---------------- BUTTONS ----------------
btn_frame = ttk.Frame(card)
btn_frame.pack(pady=20)

ttk.Button(btn_frame, text="Encrypt", command=lambda: process("encrypt")).pack(side="left", padx=10)
ttk.Button(btn_frame, text="Decrypt", command=lambda: process("decrypt")).pack(side="left", padx=10)
ttk.Button(btn_frame, text="Clear", command=clear_all).pack(side="left", padx=10)

# ---------------- OUTPUT ----------------
ttk.Label(card, text="Result").pack(anchor="w")
output_box = tk.Text(
    card,
    height=6,
    font=("Consolas", 11),
    wrap="word",
    state="disabled",
    bg="#f9fafb"
)
output_box.pack(fill="x", pady=(5, 0))

# ---------------- STATUS BAR ----------------
status = tk.StringVar(value="Ready")
status_bar = ttk.Label(root, textvariable=status, relief="sunken", anchor="w", padding=6)
status_bar.pack(side="bottom", fill="x")

root.mainloop()
