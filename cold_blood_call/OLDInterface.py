from tkinter import *
import tkinter as tk
from tkinter import filedialog
import random
from threading import Thread
import time


class InstructorInterface():
    def __init__(self, given, callback):
        self.root = Tk()
        if not given:
            self.rosterFile = filedialog.askopenfilename(initialdir="", title="Please choose your roster file")
            return

        # self.frame = Frame(self.root, padding=50)
        # self.frame.grid()
        self.root.grid()
        self.root.geometry("+1000+0")
        self.roster = given
        self.index = 0
        self.callback = callback
        self.deckSize = 4
        self.nameLabels = []

        y = 15
        for i in range(self.deckSize):
            if (i==self.index):
                label = Label(self.root,text=f"{self.roster[i]}",bg = "red")
            else:
                label = Label(self.root,text=f"{self.roster[i]}",bg = "green")
            label.pack(padx=5, pady=y, side=tk.LEFT)
            y+=10
            self.nameLabels.append(label)

        button = Button(self.root, text="click", command=self.buttonHit)
        button.pack(padx=5, pady=30, side=tk.LEFT)

        self.root.bind('<Left>', self.leftKey)
        self.root.bind('<Right>', self.rightKey)
        self.root.bind('<Up>', self.upKey)
        self.root.bind('<Down>', self.downKey)


    def startGUI(self):
        self.root.wm_attributes("-topmost", "true")
        self.root.lift()
        self.root.mainloop()

    def kill(self):
        self.root.destroy()

    def buttonHit(self):

        # print("asd")
        # self.callback(self.index)
        # if (self.index == 3):
        #     self.index = 0
        # else:
        #     self.index += 1


        # Wait for two seconds
        self.root.update_idletasks()
        for index,label in enumerate(self.nameLabels):
            if (index == self.index):
                label.config(text=f"{self.roster[index]}", bg="red")
            else:
                label.config(text=f"{self.roster[index]}", bg="green")
            label.update()

        print("roster")
        print(self.roster)
        time.sleep(0.1)

    def leftKey(self,event):
        if self.index == 0:
            self.index = self.deckSize -1
        else:
            self.index -= 1

        self.updateGUI()

    def rightKey(self,event):
        if self.index == self.deckSize -1:
            self.index = 0
        else:
            self.index += 1

        self.updateGUI()

    def upKey(self,event):
        self.deck = self.callback(self.index, 1)
        self.updateGUI()

    def downKey(self, event):
        self.deck = self.callback(self.index)
        self.updateGUI()

    def updateGUI(self):
        self.root.update_idletasks()
        for index,label in enumerate(self.nameLabels):
            if (index == self.index):
                label.config(text=f"{self.roster[index]}", bg="red")
            else:
                label.config(text=f"{self.roster[index]}", bg="green")
            label.update()

        print("roster")
        print(self.roster)
        time.sleep(0.1)

    def getRosterFileInput(self):
        return self.rosterFile
