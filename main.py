#Created by Fariyan Ishraq
from tkinter import*
from pyforest import*
from tkinter.ttk import Progressbar

a='white'
b=('Calibri (Body)',70,'bold')
c='black'
d='cyan'
e=('Calibri (Body)',30)
title = 'sub-title'

UI_window = Tk()
UI_window.configure(bg=c)

width_of_window = 693
height_of_window = 349
screen_width = UI_window.winfo_screenwidth()
screen_height = UI_window.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
UI_window.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

UI_window.overrideredirect(1)



ui_text1 = Label(UI_window ,text="  Your Application",fg=a,bg=c)
ui_text1.configure(font=b)
ui_text1.pack(padx=20 , pady=20)

ui_text2 = Label(UI_window ,text=title,fg=d,bg=c)
ui_text2.configure(font=e)
ui_text2.pack()
ui_progress = Progressbar(UI_window,orient=HORIZONTAL,length=500,mode='determinate')
ui_progress.start()
ui_progress.after(6000,UI_window.destroy)
ui_progress.pack(pady=20)
#UI_window.after(5000,UI_window.destroy)
UI_window.mainloop()
