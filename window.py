from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("961x476")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 476,
    width = 961,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

window.resizable(False, False)
window.mainloop()
