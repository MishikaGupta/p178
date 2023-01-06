# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 15:46:25 2022

@author: Beautiful Mishika
"""

from tkinter import *
import random 

root  =Tk()
root.title("Encapsulation")
root.geometry("800x600")

label = Label(root, font=("Arial", 40))
label.place(relx=0.5, rely=0.5,anchor=CENTER)

class game:
    def __init__(self):
        self.__score = 0
        
    def updateGame(self):
        self.text= ["BLACK", "PINK", "GREEN", "BLUE", "YELLOW", "RED"]
        self.random_number_for_text = random.randint(0,5)
        self.color = ["black", "pink", "green", "blue", "yellow", "red"]
        self.random_number_for_color = random.randint(0,5)
        label["text"] = self.text[self.random_number_for_text]
        label["fg"] = self.color[self.random_number_for_color]
        
object = game()

btn = Button(root, text="Start", command=object.updateGame())
btn.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()
