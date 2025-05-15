import tkinter as tk
from tkinter import filedialog, messagebox
from pydub import AudioSegment
import os

def select_files():
    global files
    files = filedialog.askopenfilenames(title="Select audio files")
    if files:
        file_label.config(text=f"{len(files)} file(s) selected")

def convert_files():
    if not files:
        messagebox.showwarning("No files", "Please select audio files first.")
        return

    format_selected = format_var.get().lower()
    if not format_selected:
        messagebox.showwarning("No format", "Please select an output format.")
        return

    output_dir = filedialog.askdirectory(title="Select output folder")
    if not output_dir:
        return

    for file_path in files:
        try:
            audio = AudioSegment.from_file(file_path)
            filename = os.path.splitext(os.path.basename(file_path))[0]
            output_path = os.path.join(output_dir, f"{filename}.{format_selected}")
            audio.export(output_path, format=format_selected)
        except Exception as e:
            messagebox.showerror("Conversion Error", f"Error converting {file_path}: {e}")
            return

    messagebox.showinfo("Success", "Conversion completed!")

# GUI Setup
root = tk.Tk()
root.title("<CNVRTR>")
root.geometry("350x200")

files = []

tk.Button(root, text="Select Audio Files...", command=select_files).pack(pady=10)
file_label = tk.Label(root, text="No files selected")
file_label.pack()

tk.Label(root, text="Select Format:").pack()
format_var = tk.StringVar()
format_entry = tk.Entry(root, textvariable=format_var)
format_entry.pack()

tk.Button(root, text="Convert", command=convert_files).pack(pady=20)

root.mainloop()
