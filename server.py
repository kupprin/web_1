from socket import *
import tkinter as tk
import threading
from PIL import ImageTk, Image

Hostname = gethostname()
Host_IP = gethostbyname(Hostname)
print(Host_IP)

def change_image():
    global image_index, lab
    image_index = (image_index + 1) % len(images)
    image = images[image_index]
    lab.configure(image=image)
    lab.image = image


def start_server():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((Host_IP, 4001))
    server.listen()

    user, addr = server.accept()

    while True:
        data = user.recv(1)
        if not data:
            break
        change_image()


def finish():
    win.destroy()


new_thread = threading.Thread(target=start_server)
new_thread.start()

win = tk.Tk()
win.title('CLICKcatCLICK')
win.geometry("256x256+150+80")
win.config(bg='#84c3be')
win.minsize(256, 256)
img = ImageTk.PhotoImage(Image.open("images/cat1.png"))
lab = tk.Label(win, image=img)
lab.pack()

images = [
    ImageTk.PhotoImage(Image.open("images/cat1.png")),
    ImageTk.PhotoImage(Image.open("images/cat2.png")),
]
image_index = 0

win.protocol("WM_DELETE_WINDOW", finish)
win.mainloop()
