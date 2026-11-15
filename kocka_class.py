import tkinter as tk
from tkinter import ttk, messagebox
import random

class Kockadobas:
    def __init__(self, root):
        self.root = root
        self.root.title("Kockázás")
        self.root.geometry("600x400")
        self.eredmenyek = {i: 0 for i in range(1, 7)}

        self.cim_cimke = ttk.Label(root, text='Kockajáték',font='Arial 16 bold')
        self.cim_cimke.grid(row=0, column=1, padx=10, pady=10)

        self.dobas_szam = tk.StringVar(value="10")
        self.dobas_szam_be = ttk.Entry(root, textvariable=self.dobas_szam, width=10)
        self.dobas_szam_be.grid(row=1, column=0, padx=70, pady=10)

        self.dobas_gomb = ttk.Button(root, text='Dobás', command=self.dobas)
        self.dobas_gomb.grid(row=2, column=1, padx=10, pady=10)

        self.kilepes_gomb = ttk.Button(root, text='Kilépés', command=root.destroy)
        self.kilepes_gomb.grid(row=1, column=3, padx=10, pady=10)

        self.dobas_eredmenye = ttk.Label(root, text='Eredmény', font='Arial 16 bold')
        self.dobas_eredmenye.grid(row=2, column=0)

    def dobas(self):
        try:
            db = int(self.dobas_szam.get())
        except ValueError:
            messagebox.showerror('Hiba', 'Nem sikerül számmá átalakítani!')
            return

        if not 1 <= db <= 10000:
            messagebox.showerror('Hiba', 'A dobások számának 1 és 10000 közé kell esnie!')
            return

        self.eredmenyek = {i: 0 for i in range(1, 7)}
        for _ in range(db):
            dobott_ertek = random.randint(1, 6)
            self.eredmenyek[dobott_ertek] += 1

        szoveg = '\n'.join(f'{oldal}.  =  {darab}' for oldal, darab in self.eredmenyek.items())

        self.dobas_eredmenye.config(text=szoveg)

if __name__ == '__main__':
    root = tk.Tk()
    app = Kockadobas(root)
    root.mainloop()
