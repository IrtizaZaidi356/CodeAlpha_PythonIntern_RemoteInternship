"""
CodeAlpha | Python Intern | Remote Internship 
Task No# 02: URL Shortener 
Perform Task

Develop a URL shortening service like Bitly. Users can input a
long URL, and the application will generate a shorter, unique
URL that redirects to the original link
"""

import tkinter as tk
import pyperclip
import shortuuid

def shorten_url():
    long_url = entry_long_url.get()
    if long_url:
        short_url = "http://short.url/" + shortuuid.uuid()[:8]
        entry_short_url.delete(0, tk.END)
        entry_short_url.insert(0, short_url)
        entry_short_url.config(state="readonly")
        pyperclip.copy(short_url)
        status_label.config(text="Short URL copied to clipboard!", fg="green")
    else:
        status_label.config(text="Please enter a long URL.", fg="red")

# GUI setup
root = tk.Tk()
root.title("URL Shortener")
root.geometry("500x300") 

label_long_url = tk.Label(root, text="Enter Long URL:")
label_long_url.pack(pady=5)

entry_long_url = tk.Entry(root, width=40)
entry_long_url.pack(pady=10)

btn_shorten = tk.Button(root, text="Shorten URL", command=shorten_url)
btn_shorten.pack(pady=10)

label_short_url = tk.Label(root, text="Shortened URL:")
label_short_url.pack(pady=5)

entry_short_url = tk.Entry(root, width=40, state="readonly")
entry_short_url.pack(pady=10)

status_label = tk.Label(root, text="", fg="black")
status_label.pack(pady=10)

root.mainloop()
