"""
    File: ColdCall.py
    Description: The main function is a driver to start the software system
    with three modules. The sofeware system will read the roster from
    initial_roster.txt file or Saved/boot roster file to load student infomation.
    The system will output three files when program exit. (Log file, Saved/Boot file
    and perfermance file)
    Last update time: 1/24/2022
    Dependencies: Classroom, InstructorInterface, DataStream
    Credit: n/a
"""

# Import module
from Classroom import Classroom
from InstructorInterface import InstructorInterface
from DataStream import *

"""
    main(): the driver to control modules for the system
"""
class ColdCallSystem:
    def __init__(self):
        # loading Saved/Boot Roster, return a list of lists
        # readRoster() failed then return False
        self.rosterModified = checkRosterChange()[1]                  # Check for any modifications in the roster save
        (self.rosterStringList, self.isInitialBoot) = readRoster()    # Try to read the roster file, isInitialBoot is false if can read
        self.exitProgram = 0                                          # Will be checked after to determine quit condition

    def run(self):
        haveValidRoster = self._getCheckConfirmRosterFile()   # Call function to check roster validity, if not prompt the user
        if not haveValidRoster:                               # If the user cancels the file input prompt, quit
            return
        self._startDeckGUI()                                  # Create the top deck bar and manage the decks
        self._exitAndSave()                                   # Merge the decks and save the data



    def _getCheckConfirmRosterFile(self):
        # If the roster read return is a valid list, not an error mesage, return
        if isinstance(self.rosterStringList,list):
            return 1
        # If the roster read return is an error message, prompt the user
        rosterGUI = InstructorInterface(self.rosterStringList)                   # Creating a GUI for roster file input

        while not isinstance(self.rosterStringList,list):                        # if rosterStringList is a string and not a list, it is an error
            newRosterFile = rosterGUI.getRosterFileInput(self.rosterStringList)  # asking the user for a roster file path

            if newRosterFile == "":                            # if the path given is empty or the user tried 3 times, exit program
                rosterGUI.killMain()
                self.exitProgram = 1
                break
            else:
                # save the file name and most recent time for it
                saveRosterInfo(newRosterFile)

            (self.rosterStringList, self.isInitialBoot) = readRoster(newRosterFile)   # Check and try to read the new given roster file path

            if isinstance(self.rosterStringList,list):                           #if the read is successful
                rosterGUI.changeMessage("Please Confirm the Student Roster, cancel to re-enter roster file")
                rosterGUI.createRosterConfirmWindow(self.rosterStringList)       #Show the roster window and ask the user to confirm or cancel
                rosterConfirmed = rosterGUI.getRosterConfirmationResult()   #if confirmed, 1 will be returned. Regardless of choice the GUI will be destroyed
                if rosterConfirmed:                                         #break roster input loop if confirmed
                    break
                else:                                                       #else reset the roster file
                    self.rosterStringList = "Please choose your roster file"
                    rosterGUI = InstructorInterface(self.rosterStringList)       #since the GUI was destroyed, make a new one and repeat the loop

        return (not self.exitProgram)

    def _startDeckGUI(self):
        self.ourClassroom = Classroom(self.rosterStringList, 4)   # call Classroom module to create students on-deck/predeck/postdeck with roster
        ourGUI = InstructorInterface(self.rosterStringList)       # Create the cold-call GUI
        ourGUI.insertDeck(self.ourClassroom.getDeck(),            # feed the GUI with the deck and needed classroom methods and start the program
                          self.ourClassroom.moveToPost,
                          self.ourClassroom.markAbsent,
                          self.rosterModified,
                          resetSystem)

    def _exitAndSave(self):
        save = self.ourClassroom.mergeDecksToList()   # save the current student info on the post-deck/pre-deck/on-deck
        writeToSavedBootRoster(save)                  # Write the Saved/Boot roster file
        writeToLogFile(save)                          # Write the log file
        updatePerforanceFile(save)                    # Upadte the Performance file

if __name__ == "__main__":
    ColdCall = ColdCallSystem()
    ColdCall.run()
