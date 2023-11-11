import tkinter as tk
from socket import *


def click():
    client.send(bytes("\00", 'ascii'))


def finish():
    win.destroy()


win = tk.Tk()

win.title('CLICKcat')
win.geometry("500x300+400+300")
win.config(bg='#84c3be')
btn = tk.Button(win, text='click', font="Arial 40", width=5, height=2, command=click)
btn.place(relx=0.5, rely=0.5, anchor='center')

client = socket(AF_INET, SOCK_STREAM)
client.connect(("10.193.178.247", 4001))

win.mainloop()
client.close()
