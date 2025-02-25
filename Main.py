import tkinter as tk
from tkinter import Tk
from tkinter import END,ttk
from tkinter import *
from IP_Lookup import ip_lookup
from Whois_Lookup import get_whois_info,format_date
from SubDomains_Scanner import 


root = tk.Tk()

root.title("Automation OSINT")
root.geometry("200x200")

text_area = Text(root,heigh=20,width=150)
text_area.pack()

valeur = StringVar()
valeur.set("")

root.configure(bg="#23272A")
text_area.configure(bg="#23272A",fg="white",font=("consolas",12))

style = ttk.Style()
style.configure("Hover.TButton",font=("Arial",12,"bold"),foreground="black", background="white", padding=10)
root.mainloop()