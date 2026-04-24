import tkinter as tk
from tkinter import PhotoImage
import platform
import socket
import psutil
import os

def show_info():
    info = ""
 
    # OS Info
    info += "🖥️ OS: " + platform.system() + " " + platform.release() + "\n"

    # CPU Info
    info += "⚡ CPU Cores: " + str(psutil.cpu_count()) + "\n"

    # RAM Info
    ram = psutil.virtual_memory()
    info += "🧠 Total RAM: " + str(round(ram.total / (1024**3), 2)) + " GB\n"

    # IP Info
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    info += "🌐 IP Address: " + ip + "\n"

    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, info)

# Main window
root = tk.Tk()
root.title("System Information Tool")
root.geometry("500x450")
root.configure(bg="#34495e")

# Title
title = tk.Label(root, text="System Information Tool",
                 font=("Arial", 20, "bold"),
                 bg="#34495e", fg="white")
title.pack(pady=15)

# Button with icon (if you have icons)
# Make sure to have icon images in the same folder or update the path
# Example: cpu_icon.png, ram_icon.png, os_icon.png, ip_icon.png
btn = tk.Button(root, text="Show Info",
                font=("Arial", 14, "bold"),
                bg="#1abc9c", fg="white",
                padx=10, pady=5,
                command=show_info)
btn.pack(pady=10)

# Text box
text_box = tk.Text(root, height=12, width=55,
                   font=("Consolas", 11),
                   bg="#ecf0f1", fg="black")
text_box.pack(pady=10)

# Footer
footer = tk.Label(root, text="Developed by Sameer",
                  bg="#34495e", fg="white")
footer.pack(side="bottom", pady=5)

root.mainloop()