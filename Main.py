import tkinter as tk
from tkinter import ttk,END
from tkinter import *
from Ip_Lookup import ip_lookup
from Whois_Lookup import get_whois_info,format_date
from SubDomains_Scanner import Subdomains_Scanner
from Email_Finder import email_finder
from tkinter import simpledialog

root = Tk()
root.title("Automation OSINT")
root.geometry("1920x1080")

text_area = Text(root,height=20,width=150)
text_area.pack()

valeur = StringVar()
valeur.set("")

root.configure(bg="#23272A")
text_area.configure(bg="#23272A",fg="white",font=("consolas",12))

style = ttk.Style()
style.configure("Hover.TButton",font=("Arial",12,"bold"),foreground="black", background="#5865F2", padding="10")

def on_enter(e):
    e.widget.configure(style="Hover.TButton")
    
def on_leave(e):
    e.widget.configure(style="TButton")    

def ip_lookup_main():
    ip = simpledialog.askstring("Ip Input", "Enter an IP adresse to scan : ")
    if not ip:
        text_area.insert(END,"Please, enter an appropriate IP adress. \n")
        return
    ip_lookup(ip)

def Subdomains_Scanner_main():
    Subdomain = simpledialog.askstring("Subdomain input","Enter a domain's name to scan : ")
    if not Subdomain:
        text_area.insert(END,"Please, enter an appropriate domain's name. \n")
        return
    Words_Length = simpledialog.askinteger("Word Length input", "Enter the Word range you want to test in the word list (Max 114441) : ")
    if not Words_Length:
        text_area.insert(END,"Please enter a correct value : ")
        return
    Subdomains_Scanner(Subdomain)
    
def Whois_Lookup_main():
    Domain = simpledialog.askstring("Domain input","Enter a domain's name : ")
    if not Domain:
        text_area.insert(END,"Please enter an appropriate domain's name. \n")
        return
    get_whois_info(Domain)

def email_finder_scan():
    Domain = simpledialog.askstring("Domain input","Enter a domain's name : ")
    if not Domain:
        text_area.insert(END,"Enter a valid domain name. \n ")
        return
    email_finder(Domain)
    
    #faire le bouton pour cette fonction
    

    
Button_IP = ttk.Button(root,text="IP Lookup",command=ip_lookup_main, style="TButton")
Button_IP.bind("<Enter>", on_enter)
Button_IP.bind("<Leave>", on_leave)
Button_IP.pack()

Button_Subdomains = ttk.Button(root, text="Subdomains Scanner",command=Subdomains_Scanner_main,style="TButton")
Button_Subdomains.bind("<Enter>", on_enter)
Button_Subdomains.bind("<Leave>", on_leave)
Button_Subdomains.pack()   

Button_Whois = ttk.Button(root,text="Whois Lookup",  command=Whois_Lookup_main, style="TButton")
Button_Whois.bind("<Enter>", on_enter)
Button_Whois.bind("<Leave>", on_leave)
Button_Whois.pack()    

    
Button_Email = ttk.Button(root,text="Email finder", command=email_finder_scan, style="TButton")
Button_Email.bind("<Enter>", on_enter)
Button_Email.bind("<Leave>", on_leave)
Button_Email.pack()


root.mainloop()
