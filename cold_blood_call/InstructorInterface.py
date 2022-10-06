"""
    Created by Stephen Leveckis, Mert Yapucuoglu 1/12/2022
    Creates self.window GUI for cold calling program

    Installs Requried:
        Tkinter: sudo apt-get install python3.6-tk

Create and allow interaction with a GUI window using tkinter.

Used By:
    ColdCall.py

Members:
    Member Name:                : Type           : Default Val                -> Description
    ------------------------------------------------------------------------------------------------------------------------------------------
    self._topBar                : tkinter        : Tk()                       -> the main tkinter window that will hold the names and accept input

    self.Canvas                 : tkinter.canvas : tkinter.canvas             -> The canvas in the topBar that will hold texts and buttons

    self._rosterConfirmWindow   : tkinter        : Tk()                       -> the roster confirmation window that will show the list and ask confirmation

    self.textColors             : list[string]   : ["white", "white",         -> The color array defining the color of text for each student name on the window
                                                    "white", "white"]

    self.screen_w               : int            : tk.winfo_screenwidth()     -> Contains the width of the user display

    self.screen_h               : int            : tk.winfo_screenheight()    -> Contains the height of the user display

    self.deck                   : list[Student]  : deck(parameter)            -> a list of Student objects that show who are currently on deck

    self.roster                 : list[Student]  : None                       -> a list of Student that will be shown on initial file load for review

    self.moveToPost             : method         : moveToPost(parameter)      -> a method given to the class on insertDeck call from ColdCall.py to move student to deck after being chosen

    self.markAbsent             : method         : markAbsent(parameter)      -> a method given to the class on insertDeck call from ColdCall.py to mark a student absent

    self.resetSystem            : method         : resetSystem()              -> a method given to the class on insertDeck call from ColdCall.py to reset the system

    self.highlightList          : list[bool]     : [True, False,              -> A list of bools showing which label is indexed on the GUI.
                                                    False, False]

    self.resetButton            : tk.button      : button                     -> A button in the _topBar that calls self.resetSystem() upon click

    self.confirmButton          : tk.button      : button                     -> A button in the _rosterConfirmWindow that confirms the input roster

    self.rejectButton           : tk.button      : button                     -> A button in the _rosterConfirmWindow that rejects the input roster

    self.scrollbar              : tk.Scrollbar   : scrollbar                  -> A scrollbar in the _rosterConfirmWindow to help user navigate the list of student

    self.student_list           : tk.Listbox     : [Listbox]                  -> A list in the _rosterConfirmWindow containing student names to be displayed

Methods:

    Private:                                                                     Return:
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self._displayText(self)                                     |   ->  None
                                                                                |
    Usage:          self.<direction>ArrowKey(self,event)                        |
                                                                                |
    Description:    Delete all the name labels on the current window and        |
                    recreate them with the updated colors and names             |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self._increaseCounter(self)                                 |   ->  None
                                                                                |
    Usage:          self._leftArrowKey(self, event)                             |
                                                                                |
    Description:    Increases the highlight counter that indicates which name   |
                    is being currently selected                                 |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self._decreaseCounter(self)                                 |   ->  None
                                                                                |
    Usage:          self._rightArrowKey(self, event)                            |
                                                                                |
    Description:    Decreases the highlight counter that indicates which name   |
                    is being currently selected                                 |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self._leftArrowKey(self, event)                             |   ->  None
                                                                                |
    Usage:          self._topBar.bind(<Left>)                                   |
                                                                                |
    Description:    Upon user left arrow input, calls self._decreaseCounter()   |
                    to change the highlighted index, changes the highlightList  |
                    with the new index and calls self._displayText() to refresh |
                    the GUI window.                                             |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self._rightArrowKey(self, event)                            |   ->  None
                                                                                |
    Usage:          self._topBar.bind(<Right>)                                  |
                                                                                |
    Description:    Upon user right arrow input, calls self._increaseCounter()  |
                    to change the highlighted index, changes the highlightList  |
                    with the new index and calls self._displayText() to refresh |
                    the GUI window.                                             |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self._chooseWithFlag(self, event)                           |   ->  None
                                                                                |
    Usage:          self._topBar.bind(<.>)                                      |
                                                                                |
    Description:    Upon user . key input, finds the highlighed index and calls |
                    self.moveToPost(index) which is a method passed on by init  |
                    from the ColdCall, which also imported it from the          |
                    Classroom.py in order to move the selected student from deck|
                    to postdeck because he/she has been cold called. Also sets  |
                    up the flag for the selected student.                       |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self._chooseWithoutFlag(self, event)                        |   ->  None
                                                                                |
    Usage:          self._topBar.bind(<,>)                                      |
                                                                                |
    Description:    Upon user, key input, finds the highlighed index and calls  |
                    self.moveToPost(index) which is a method passed on by init  |
                    from the ColdCall, which also imported it from the          |
                    Classroom.py in order to move the selected student from deck|
                    to postdeck because he/she has been cold called.            |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self._chooseAbsent(self, event)                             |   ->  None
                                                                                |
    Usage:          self._topBar.bind(</>)                                      |
                                                                                |
    Description:    Upon user / key input, finds the highlighed index and calls |
                    self.markAbsent(index) which is a method passed on by init  |
                    from the ColdCall, which also imported it from the          |
                    Classroom.py in order to mark the student as absent and     |
                    remove them from all the decks for the class instance.      |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self._showRosterModified(self,message)                      |   ->  None
                                                                                |
    Usage:          self.insertDeck                                             |
                                                                                |
    Description:    Called by insertDeck function when the top bar deck is      |
                    created. This method creates a window to notify the user    |
                    that the save file has been modified from outside. It also  |
                    accepts a new message in order to be used for other         |
                    notifications.                                              |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self._confirmRoster(self)                                   |   ->  None
                                                                                |
    Usage:          self._rosterConfirmWindow.rejectButton click                |
                                                                                |
    Description:    Called by roster confirm window cancel button. If the       |
                    user confirms the roster input we set rosterConfirmed       |
                    variable to 1. Then we destroy both GUI windows.            |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self._rejectRoster(self)                                    |   ->  None
                                                                                |
    Usage:          self._rosterConfirmWindow.rejectButton click                |
                                                                                |
    Description:    Called by roster confirm window reject button. If the       |
                    user rejects the roster input we destroy both GUI windows   |
                    and prepare to re-prompt for a file.                        |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self._systemReset(self)                                     |   ->  None
                                                                                |
    Usage:          self.topBar.resetButton click                               |
                                                                                |
    Description:    Called by top bar if the reset button is pressed. Resets    |
                    the saved roster and closes the program.                    |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------

    Public:                                                                      Return:
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self._startGUI(self)                                        |   ->  None
                                                                                |
    Usage:          main() in ColdCall.py                                       |
                                                                                |
    Description:    Called by self.insertDeck() when a valid roster is found.   |
                    Sets the GUI window to the top and foreground, and starts   |
                    the tkinter mainloop for the GUI to function.               |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self.getRosterFileInput(self, errorMessage)                 |   ->  string  - An absolute file path given by
                                                                                |                 the user
    Usage:          main() in ColdCall.py                                       |
                                                                                |
    Description:    This is called by main when there is no valid roster file.  |
                    Takes an errorMessage and shows it on the GUI. Pops up a    |
                    file input screen and lets the user choose a roster file.   |
                    Sets the GUI window to the top and foreground, and starts   |
                    the tkinter mainloop for the GUI to function.               |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self.insertDeck(self,deck, moveToPost)                      |   ->  None
                                                                                |
    Usage:          main() in ColdCall.py                                       |
                                                                                |
    Description:    This is called by main to feed the GUI with the student     |
                    deck. It also takes in the moveToPost function of the       |
                    classroom class and saves it for future use for cold call.  |
                    It then calls self._displayText() to update the window with |
                    the student names, and then calls self._startGUI() to start |
                    the GUI mainloop.                                           |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self.createRosterConfirmWindow(self,deck)                   |   ->  None
                                                                                |
    Usage:          main() in ColdCall.py                                       |
                                                                                |
    Description:    This is called by the main to show the user the roster list |
                    and ask for confirmation. Creates a window to show the user |
                    the input of the roster file they provided, along with      |
                    2 buttons, confirm and cancel, to choose if they want to    |
                    use thisroster for the rest of the program.                 |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self.getRosterConfirmationResult(self)                      |   ->  boolean
                                                                                |
    Usage:          main() in ColdCall.py                                       |
                                                                                |
    Description:    Returns the confirmation result of the cofirmation window   |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self.changeMessage(self, message)                           |   ->  None
                                                                                |
    Usage:          main() in ColdCall.py and in many methods                   |
                                                                                |
    Description:    Overrides the text in the top bar and displayes the message |
                    given.                                                      |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------
    Declaration:    self.killMain(self)                                         |   ->  None
                                                                                |
    Usage:          main() in ColdCall.py                                       |
                                                                                |
    Description:    Destroys the top bar tkinter window, causing the program    |
                    proceed.                                                    |
                                                                                |
    ----------------------------------------------------------------------------|-------------------------------------------------

"""
# Import Tkinter library to create GUI windows
import tkinter as tk
from tkinter import *
from tkinter import filedialog

# Importing sys to exit out of program if user terminates or resets
import sys

#Importing time use sleep to wait on notifications before closing
import time

class InstructorInterface():
    def __init__(self, deck=""):

        # The main GUI window object
        self._topBar = tk.Tk()

        # The main GUI window title name
        self._topBar.title("Cold Call System")

        # All text starts as white by default
        self.textColors = ["white", "white", "white", "white"]
        self.deck = deck
        self.roster = None
        self.moveToPost = None
        self.markAbsent = None
        self.rosterConfirmed = 0

        # Leftmost value is True (highlighted) by default
        self.highlightList = [True, False, False, False]
        self.highlight_counter = 0

        # Key listeners as part of the Tkinter library, waits for key press
        self._topBar.bind('<Right>', self._rightArrowKey)
        self._topBar.bind('<Left>', self._leftArrowKey)
        self._topBar.bind('<comma>', self._chooseWithoutFlag)
        self._topBar.bind('<period>', self._chooseWithFlag)
        self._topBar.bind('<slash>', self._chooseAbsent)

        # Gets native screen resolution width and height
        self.screen_w = self._topBar.winfo_screenwidth()
        self.screen_h = self._topBar.winfo_screenheight()

        # 19 is a scalar modifier that happens to create a decent
        # screen height for our self._topBar based on original native screen height
        self.win_h = self.screen_h/22
        self.win_w = self.screen_w

        # Make a string "widthxheight" to pass to geometry function
        dimensions = "%dx%d+%d+%d" % (self.win_w, self.win_h,0,0)
        # Sets the self.window size to these dimensions
        self._topBar.geometry(dimensions)

        # Canvas object
        self.canvas = Canvas(self._topBar, width = self.win_w, height = self.win_h, bg = "black")

        """
        Create 4 widgets, one for each displayed name.

        This process, creating 4 widgets must be done once initially, here,
        and then once for every keypress to display the updated text
        (done in the arrow key functions)
        """

        # Sets the color for the highligted student to red
        for i in range(len(self.highlightList)):
            if (self.highlightList[i] is True):
                self.textColors[i] = "red"

        # If the input is not a valid deck, it is an error message, show it
        if not isinstance(self.deck,list):
            self.canvas.create_text(5,15, text=self.deck, fill = "white", font = ('Helvetica 18 bold'), anchor='w')
            self.canvas.pack(fill=BOTH, expand=True)



    """
    Deletes all old text objects and replaces them with updated ones based on the
    textColors list. This is called after every key press event to reflect which name should be highlighted.
    """
    def _displayText(self):
        self.canvas.delete("all")
        self.canvas.create_text(5,15, text=self.deck[0], fill = self.textColors[0], font = ('Helvetica 15 bold'), anchor='w')
        self.canvas.create_text(self.win_w/4, 15, text=self.deck[1], fill = self.textColors[1], font = ('Helvetica 15 bold'), anchor='w')
        self.canvas.create_text(self.win_w/2, 15, text=self.deck[2], fill = self.textColors[2], font = ('Helvetica 15 bold'), anchor='w')
        self.canvas.create_text(((self.win_w*3) /4), 15, text=self.deck[3], fill = self.textColors[3], font = ('Helvetica 15 bold'), anchor='w')
        self.canvas.pack(side=tk.LEFT, fill=BOTH, expand=True)


    """
    Increases highlight_counter with a bound that prevents it from
    increasing past 3, the rightmost name on our Deck.
    """
    def _increaseCounter(self):
        if ((self.highlight_counter +1) > 3):
            self.highlight_counter = 3
        else:
            self.highlight_counter = self.highlight_counter + 1

    """
    Decreases highlight_counter with a bound that prevents it from
    decreasing past zero, the leftmost name on our Deck.
    """
    def _decreaseCounter(self):
        if((self.highlight_counter -1) < 0):
            self.highlight_counter = 0
        else:
            self.highlight_counter = self.highlight_counter - 1


    """
    Upon a <Left> Arrow Key press, updates highlight_counter and the corresponding data
    structures to represent highligting the name to the left of the current highlighted name.
    """
    def _leftArrowKey(self, event):
        # Set the boolean list to reflect which index
        # in the list we want to be highlighted
        self._decreaseCounter()
        self.highlightList[self.highlight_counter+1] = False
        self.highlightList[self.highlight_counter] = True

        # Update the textColors list to reflect which name on Deck
        # should be red/highlighted
        for i in range(len(self.highlightList)):
            if (self.highlightList[i] is True):
                self.textColors[i] = "red"
            else:
                self.textColors[i] = "white"

        # After updating the data structures, call the function
        # that will display the text accordingly
        self._displayText()


    """
    Upon a <Right> Arrow Key press, updates highlight_counter and the corresponding data
    structures to represent highligting the name to the left of the current highlighted name.
    """
    def _rightArrowKey(self, event):
        # Set the boolean list to reflect which index
        # in the list we want to be highlighted
        self._increaseCounter()
        self.highlightList[self.highlight_counter-1] = False
        self.highlightList[self.highlight_counter] = True

        # Update the textColors list to reflect which name on Deck
        # should be red/highlighted
        for i in range(len(self.highlightList)):
            if (self.highlightList[i] is True):
                self.textColors[i] = "red"
            else:
                self.textColors[i] = "white"

        # After updating the data structures, call the function
        # that will display the text accordingly
        self._displayText()


    """
    Removes the currently highlighted student from the Deck
    """
    def _chooseWithFlag(self, event):
        # Moves the highlighted student to the post-deck,
        # which moves them off the Deck.
        for i in range(len(self.highlightList)):
            if (self.highlightList[i] is True):
                self.moveToPost(i,True)
                break
        # Displays the text after modifying relevant data structures
        # (the removed student will no longer be shown on the Deck.
        # print("yeah")
        self._displayText()


    """
    Removes the currently highlighted student from the Deck,
    and "flags" them (reflected in the output log file)
    for user purposes.
    """
    def _chooseWithoutFlag(self, event):
        # Moves the highlighted student to the post-Deck,
        # which moves them off the Deck.
        for i in range(len(self.highlightList)):
            if (self.highlightList[i] is True):
                self.moveToPost(i)
                break
        # Displays the text after modifying relevant data structures
        # (the removed student will no longer be shown on the Deck.
        self._displayText()


    """
    Upon the key input, will remove the student with the highlight from the list
    while marking them as absent and removing them from the active students.
    """
    def _chooseAbsent(self,event):
        for i in range(len(self.highlightList)):
            if (self.highlightList[i] is True):
                self.markAbsent(i)
                break
        # Displays the text after modifying relevant data structures
        # (the removed student will no longer be shown on the Deck.
        self._displayText()


    """
    Start the GUI itself (nothing is displayed without mainloop()),
    and set window properties.
    The win.lift() function ensures our window is always displayed
    above other application GUIs on the user screen.
    """
    def _startGUI(self):
        self._topBar.wm_attributes("-topmost", "true")
        self._topBar.lift()
        self._topBar.mainloop()


    """
    Opens a file explorer to input a roster file if one
    has not been supplied yet by the user. Shows the error message
    provided by errorMessage parameter on the screen.
    """
    def getRosterFileInput(self, errorMessage):
        self.changeMessage(errorMessage)                                                                           #add the errormessage to the window
        rosterFile = filedialog.askopenfilename(initialdir = "", title="Please choose your roster file")           #Take file path input from a pop-up window
        return rosterFile                                                                                          #return the path


    """
    Takes a deck parameter and saves  it to the self.deck to be used as a roster.
    Tkaes a moveToPost parameters method that will be called to move students
    out of the deck. Refreshes the GUI window with the provided deck names with
    self._displayText(). And starts the GUI functionality with self._startGUI()
    """
    def insertDeck(self, deck, moveToPost, markAbsent, rosterModified, resetSystem):

        self.deck = deck
        self.moveToPost = moveToPost
        self.markAbsent = markAbsent
        self.rosterModified = rosterModified
        self.resetSystem = resetSystem                                # Accept the parameters to the class
        self._displayText()                                           # Create the names on the top bar
        self.resetButton = Button(self.canvas, text="Reset", command=self._systemReset) # Create the reset button on top Bar
        self.resetButton.pack(side=tk.RIGHT)
        if self.rosterModified:                                        # If the roster is modified, show notification
            self._showRosterModified()
        self._startGUI()                                               # Start the GUI mainloop


    """
    Called by insertDeck function when the top bar deck is created. This method
    creates a window to notify the user that the save file has been modified
    from outside. It also accepts a new message in order to be used for other
    notifications.
    """
    def _showRosterModified(self, message = "Roster changes detected."):
        self.modificationNotification = Tk()                                        # Creates the notification window
        self.modificationNotification.title("Notification")                         # Gives it a title
        dimensions = "%dx%d+%d+%d" % (400, 60, self.screen_w*2/5, self.screen_h/3)  # Sets place and dimensions
        self.modificationNotification.geometry(dimensions)
        canvas = Canvas(self.modificationNotification, width=50, height=50, bg="black") # Creates a canvas on the window
        canvas.create_text(5,15, text=message,                                          # Creates the message text
                fill = "white", font = ('Helvetica 18 bold'), anchor='w')
        canvas.pack(fill=BOTH, expand=True)


    """
    Creates a window to show the user the input of the roster file they provided,
    along with 2 buttons, confirm and cancel, to choose if they want to use this
    roster for the rest of the program.
    """
    def createRosterConfirmWindow(self,deck):
        """
        Create the list of student with another window.
        credit: https://blog.csdn.net/m0_38039437/article/details/80549931
        """

        # The side GUI window object
        self._rosterConfirmWindow = Tk()
        self.deck = deck
        # Setup side window name
        self._rosterConfirmWindow.title("Student Roster")

        # setting the side window size and display location (under main window)
        self._rosterConfirmWindow.geometry("%dx%d+0+%d" % (self.screen_w/8, self.screen_h/2.5, self.screen_h/8))
        self._rosterConfirmWindow.configure(bg = "black")

        # setup vertical scroll bar
        self.scrollbar = Scrollbar(self._rosterConfirmWindow)

        # setting scroll bar display location in window
        self.scrollbar.pack(side = RIGHT, fill = Y)

        # add scrollbar module into Listbox
        self.confirmButton = Button(self._rosterConfirmWindow, text="Confirm", command= self._confirmRoster)
        self.confirmButton.pack(side=tk.TOP)
        self.rejectButton = Button(self._rosterConfirmWindow, text="Cancel", command=self._rejectRoster)
        self.rejectButton.pack(side=tk.TOP)
        self.student_list = Listbox(self._rosterConfirmWindow, width = int(self.screen_w/8), height = int(self.screen_h/2.5), yscrollcommand = self.scrollbar.set, font = ('Helvetica 13 bold'), bg = "black", fg = "white")

        # Input student names into Listbox
        for i in range(len(self.deck)):
          # insert each student name at END of the list
          self.student_list.insert(END, "%s %s" % (self.deck[i][0], self.deck[i][1]))

        # setup Listbox on window
        self.student_list.pack(side=tk.BOTTOM)
        # self.confirmButton.pack()

        # setting scrollbar command using Listbox.yview() method
        self.scrollbar.config(command = self.student_list.yview)
        self._rosterConfirmWindow.mainloop()


    """
    Called by roster confirm window confirm button. If the user confirms the
    roster input, we set rosterConfirmed to 1. And then destroy both GUI windows.
    """
    def _confirmRoster(self):
        self.rosterConfirmed = 1            # Sets the confirm boolean to 1
        self._rosterConfirmWindow.destroy() # Kills the confirm window
        self._topBar.destroy()              # Kills the top bar for refresh


    """
    Called by roster confirm window cancel button. If the user rejects the
    roster input we destroy both GUI windows and prepare to re-ask.
    """
    def _rejectRoster(self):
        self._rosterConfirmWindow.destroy() # Kills the confirm window
        self._topBar.destroy()              # Kills the top bar for refresh


    """
    Called by: ColdCall.py

    Returns: self.rosterConfirmed: int. 1 for confirm, 0 for reject

    Will be called by ColdCall after the roster confirm/reject process is done in
    order to receive user choice.
    """
    def getRosterConfirmationResult(self):
        return self.rosterConfirmed


    """
    Called by: ColdCall.py

    Returns: None

    Will be called by ColdCall.py in order to change the error message on the
    top window.
    """
    def changeMessage(self, message):
        self.canvas.delete("all")                                                                                  # Clear the canvas GUI
        self.canvas.create_text(5,15, text=message, fill = "white", font = ('Helvetica 18 bold'), anchor='w')      # Create a text with the errorMessage
        self.canvas.pack(fill=BOTH, expand=True)


    """
    Called by the reset button on the top bar to reset the roster save. It then
    exits the program.
    """
    def _systemReset(self):
        self._showRosterModified("Resetting the system")    # Display the message
        time.sleep(1)                                       # Allow time for the user to understand the reset
        self.resetSystem()                                  # Calls the method passed by Datastream to reset
        sys.exit()                                          # Terminates the whole program

    """
    Closes the GUI.
    """

    def killMain(self):
        self._topBar.destroy()
