import tkinter as tk
import random

def displayLabel():
    kuji = ["大吉", "中吉", "小吉", "凶"]
    label.configure(text=random.choice(kuji))

root = tk.Tk()
root.geometry("400x400")
root.title(u"おみくじ")

label = tk.Label(text="")
button = tk.Button(text="おみくじを引く", command=displayLabel)

label.pack()
button.pack()
tk.mainloop()
