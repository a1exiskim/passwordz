import main
from tkinter import * 
from PIL import ImageTk, Image 

root = Tk()

root.title('passwordz') 


def make_basic():
    pw = main.generate_password('b')
    result_label.config(text = f'your password is: {pw}')

def make_creative():
    pw = main.generate_password('c')
    result_label.config(text = f'your password is: {pw}')


blank_label = Label(root, text = "     ")
title_label = Label(root, text = 'passwordz', bg = '#FFCCFA')
basic_button = Button(root, text = 'basic', command = make_basic, bg = '#FFCCFA')
creative_button = Button(root, text = 'creative', command = make_creative, bg = '#FFCCFA')
result_label = Label(root, text = '', bg = '#FFCCFA')

title_label.pack()
basic_button.pack()
creative_button.pack()
result_label.pack()

root.mainloop()