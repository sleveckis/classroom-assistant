import tkinter as tkr
# Credit for base code: https://www.youtube.com/watch?v=d9sHDjoXlP0
# Arrow Key codes: https://stackoverflow.com/questions/19895877/tkinter-cant-bind-arrow-key-events

def char(event):
    print(f'pressed: {repr(event.char)}')
    Log.append(event.char)
    print(Log)

def arrowL(event):
    print("left")
    Log.append("<-")
    print(Log)

def click(event):
    frame.focus_set()
    print(f'clicked at: {event.x}, {event.y}')
    Log.append((event.x, event.y))
    print(Log)

Log = []
master = tkr.Tk()
frame = tkr.Frame(master, height=500, width=500)
frame.bind("<Key>", char)
frame.bind('<Left>', arrowL)
frame.bind("<Button-1>", click)

frame.pack()

master.mainloop()



