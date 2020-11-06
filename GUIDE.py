import tkinter
from tkinter import *
import time

def hit_me():
    canvas.create_rectangle(60,10,110,60,fill="blue")  # 上
    canvas.pack()
    window.update()
    time.sleep(2)
    canvas.create_rectangle(60,10,110,60,fill = 'white')
    canvas.pack()
    window.update()
    time.sleep(1)

    canvas.create_rectangle(10,60,60,110,fill="blue")  # 左
    canvas.pack()
    window.update()
    time.sleep(2)
    canvas.create_rectangle(10,60,60,110,fill = 'white')
    canvas.pack()
    window.update()
    time.sleep(1)

    canvas.create_rectangle(60,110,110,160,fill="blue")  # 下
    canvas.pack()
    window.update()
    time.sleep(2)
    canvas.create_rectangle(60,110,110,160,fill = 'white')
    canvas.pack()
    window.update()
    time.sleep(1)

    canvas.create_rectangle(110,60,160,110,fill="blue")  # 右
    canvas.pack()
    window.update()
    time.sleep(2)
    canvas.create_rectangle(110,60,160,110,fill = 'white')
    canvas.pack()
    window.update()

window = tkinter.Tk()
window.geometry("220x240")
window.title("guide window")
window.config(bg = "white")
canvas = Canvas(window,height=170,width=170)
canvas.config(bg = "white")
canvas.create_rectangle(60,10,110,60)#上
canvas.create_rectangle(10,60,60,110)#左
canvas.create_rectangle(110,60,160,110)#右
canvas.create_rectangle(60,110,110,160)#x0,y0,x1,y1下
canvas.pack()

b = Button(window,text='run',fg='black',command=hit_me)
b.pack()

window.mainloop()
