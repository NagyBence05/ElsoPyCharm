import kocka_app
import tkinter as tk
from tkinter import ttk
import requests

def backend_uzenet():
    valasz = requests.get('http://127.0.0.1:5000/api/uzenet')
    uzi = valasz.json()
    backend_cimke.config(text=uzi['uzenet'])

root = tk.Tk()
app = kocka_app.KockaApp(root)

backend_cimke = ttk.Label(root, text='Üzenet')
backend_cimke.grid(column=1, row=4)
backend_gomb =ttk.Button(root, text='Üzenet', command=backend_uzenet)
backend_gomb.grid(column=1, row=3)

root.mainloop()