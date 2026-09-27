from customtkinter import *
from random import randint
from PIL import Image

window = CTk()
window.geometry("400x400")
window.title("Соціальне опитування")

def new_window():
    window1 = CTkToplevel(window)
    window1.geometry("200x200")
    img = Image.open('mops.jpeg')
    img_ctk = CTkImage(light_image=img, size=(175, 100))
    label = CTkLabel(window1, text='', image=img_ctk)
    label.pack(pady=10)


def no_btn():
    x=randint(0, window.winfo_width()-no_button.winfo_width())
    y=randint(0, window.winfo_height()-no_button.winfo_height())

    no_button.place(x=x, y=y)


yes_button = CTkButton(window, height=100, width=150, command=new_window, text="мав")
yes_button.place(x=25, y=250)
no_button = CTkButton(window, height=100, width=150, text="не мав", command=no_btn)
no_button.place(x=225, y=250)
ask_label = CTkLabel(window, text="Кіт, ти маму мав?", font=("Arial", 20, "bold"))
ask_label.pack(side=TOP,pady=10)

window.mainloop()