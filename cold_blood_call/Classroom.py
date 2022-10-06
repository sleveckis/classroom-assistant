"""
File: Classroom.py
Description: contains Classroom class definition for populating and maintaining the internal structures of the CCS
Local Dependencies:
        Student.py  -   Used for the Student class definition, used to hold student information passed to the constructor
Imports/Modules:
        random.randint  -   Used for random integer generation in
                            createDeck() and _moveToDeck()
        Student.Student -   Used for Student class definition (see Student.py)
Author(s):
        Mert Yapucuoglu (MY)
        Jaeger Jochimsen (JJ)
Credit:
Modifications:
    1/11/22     MY      Initial class creation and method dev
    1/13/22     JJ      Integration with Student.py functionality
    1/15/22     JJ      Privatization of members and methods, documentation
    1/17/22     JJ      Documentation
    1/19/22     JJ      Added absent list and functionality
    1/20/22     JJ      Added prev absence handling and flag as int handling
    1/24/22     JJ      Added documentation for absence functions and added absent member list
"""

# used for random integer generation in createDeck() and _moveToDeck()
from random import randint

# used for Student class definition
from Student import Student

class Classroom():
    """
    Create and maintain the 3 CCS internal data structures used for tracking the state of the class room

    Used By:
        ColdCall.py

    Members:
        Member Name:    : Type          : Default Val  -> Description
        ------------------------------------------------------------------------------------------------------------------------------------------
        self.roster     : list[Student] : -            -> a list of Student objects representing the class

        self.preDeck    : list[Student] : -            -> a list of Student objects that represent students who haven't spoken yet (student.spoken
                                                          == False)

        self.postDeck   : list[Student] : -            -> a list of Student objects that represent students who have spoken (student.spoken == True)

        self.deck       : list[Student] : -            -> a list of Student objects that represent students "On Deck"; these
                                                          are randomly chosen from the self.preDeck

        self.absent     : list[Student] : -            -> a list of Student objects that represent students who are absent; these will not be
                                                          selected for self.deck
 
        self.deckSize   : int           : 4            -> the number of students "On Deck" over the course of the run

    Methods:

        Private:                                                                     Return:
        ----------------------------------------------------------------------------|-------------------------------------------------
        Declaration:    _buildRoster(self, roster : list[list[str]] )               |   ->  list[Student]
                                                                                    |
        Usage:          self._buildRoster(roster)                                   |   ->  [Student(), Student(), ...]
                                                                                    |
        Description:    Create a list of Student objects from the lists of lists of |
                        string representing student data                            |
        ----------------------------------------------------------------------------|-------------------------------------------------
        Declaration:    _buildPrePostDeck(self, roster : list[list[Student]])       |   ->  list[Student] , list[Student]
                                                                                    |
        Usage:          self._buildPrePostDeck(roster)                              |   ->  preDeck:[Student()] , postDeck:[Student()]
                                                                                    |
        Description:    Create a tuple of Student lists, sorting the input roster   |
                        of Students based on their spoken fields. The first         |
                        list is the preDeck (all Student objects with spoken=False),|
                        the second is the postDeck (all Student objects with        |
                        spoken=True)                                                |
        ----------------------------------------------------------------------------|-------------------------------------------------
        Declaration:    _createDeck(self)                                           |   ->  list[Student]
                                                                                    |
        Usage:          self._createDeck(self)                                      |   ->  deck:list[Student]
                                                                                    |
                                                                                    |
        Description:    Create the deck of size self.deckSize by adding random      |
                        Student objects from self.preDeck to self.deck              |
        ----------------------------------------------------------------------------|-------------------------------------------------
        Declaration:    _moveToDeck(self)                                           |   ->  None
                                                                                    |
        Usage:          instance._moveToDeck()                                      |
                                                                                    |
        Description:    Move a random Student object from self.preDeck to           |
                        self.deck                                                   |
        ----------------------------------------------------------------------------|-------------------------------------------------
        Declaration:    _refresh(self)                                              |   ->  None
                                                                                    |
        Usage:          self._refresh()                                             |   ->  None
                                                                                    |
        Description:    Move all Students in the postDeck to the preDeck, resetting |
                        their spoken fields to be False.                            | 
        ----------------------------------------------------------------------------|-------------------------------------------------

        Public:                                                                      Return:
        ----------------------------------------------------------------------------|-------------------------------------------------
        Declaration:    markAbsent(self, index:int)                                 |   -> list[Student]
                                                                                    |
        Usage:          instance.markAbsent(2)                                      |
                                                                                    |
        Description:    Move specified Student to absent list and repopulates Deck  |
        ----------------------------------------------------------------------------|-------------------------------------------------
        Declaration:    moveToPost(self, index:int, flag:bool = False)              |   ->  list[Student]
                                                                                    |
        Usage:          instance.moveToPost(1, False)                               |   ->  updated deck:list[Student]
                                                                                    |
        Description:    Move the Student object at index to the self.postDeck,      |
                        setting that Student's flagged field to flag                |
        ----------------------------------------------------------------------------|-------------------------------------------------
        Declaration:    getDeck(self)                                               |   ->  list[Student]
                                                                                    |
        Usage:          instance.getDeck()                                          |   ->  deck:list[Student]
                                                                                    |
        Description:    Return the current deck (self.deck)                         |
        ----------------------------------------------------------------------------|-------------------------------------------------
        Declaration:    mergeDecksToList(self)                                      |   -> list[list[str]]
                                                                                    |
        Usage:          instance.mergeDecksToList()                                 |   -> list[list[str]]
                                                                                    |
        Description:    Add string representation of each Student object to a list, |
                        this is the current state of the class                      |
        ----------------------------------------------------------------------------|-------------------------------------------------
    """

    def __init__(self, roster, deckSize:int = 4):
        """
        Parameter:
            roster:     list of list of str where each list contains
                        a single Student object's information (to be
                        passed to constructor)
            deckSize:   the number of Student objects On-Deck at any
                        given point, this defualts to 4 as per the SRS

        Called By:
            ColdCall.py     -   called when Classroom is initialized

        Calls:
            _buildRoster()
            _buildPrePostDeck()
            _createDeck()

        Modifies: N/A

        Return:
            Instance of Classroom object

        Description:
            - Builds the initial roster of Student objects from the
              list of list of strings containing student information
            - Builds the initial preDeck and postDeck from the roster
                -> students who spoke at the end of last class are
                   placed in the postDeck
                -> students who were in the deck (i.e. "On-Deck") or
                   in the preDeck last class are loaded back into
                   preDeck
            - Loads deck with the appropriate number of Student
              objects (defined by deckSize member)
        """
        # wait on GUI input for adding to absent
        self.absent = list()

        # build the roster of Student objects from list of
        self.roster = self._buildRoster(roster)

        # build the pre and post deck structures
        self.preDeck, self.postDeck = self._buildPrePostDeck(self.roster)

        # number of students On Deck
        self.deckSize = deckSize

        # create deck with respect to self.preDeck
        self.deck = self._createDeck()


    def _buildRoster(self, studentList):
        """ 
        Parameter: 
            studentList     -   A list of list of str where each inner list
                                contains the info for a single student 
                                object

        Called By: 
            __init__()

        Calls: 
            Student.py   -   Student.__init__()

        Modifies/Side Effects: N/A

        Return: A new list of Student objects 

        Description: 
            Create a list of Student objects from the passed in roster 
        """
        # init new list
        roster = list()

        # for each list containing student info
        for student in studentList:

            # init present field to True
            present = True

            # init the spoken field to False
            spoken = False

            # if the student's info has spoken explicitly set to 
            # "True" then set it to the boolean True
            if student[5] == "True": spoken = True

            # add a new Student object containing this student's info 
            # to the output roster
            roster.append(Student(student[0], student[1], student[2],
                student[3], student[4], present, spoken, int(student[6]), int(student[7]), int(student[8]))) # FIXME: documenation for previous flags

        # reutrn the roster of Student objects
        return roster

    def _buildPrePostDeck(self, roster):
        """ 
        Parameter: 
            roster  -   a list of Student objects

        Called By:
            __init__()

        Calls:
            Student.py  -   Student.getSpoken()

        Modifies/Side Effects: N/A

        Return: A tuple of two lists of Student objects 

        Description:
            Sort the input roster into two lists:
                1)  preDeck, which contains only Student objects with 
                    their spoken field set to False
                2)  postDeck, which contains only Student objects with
                    their spoken field set to True
        """
        # initialize the two lists
        preDeck = list()
        postDeck = list()

        # for each Student object in the list <roster>
        for student in roster:

            # if the student has spoken, add them to the postDeck
            if student.getSpoken():
                postDeck.append(student)
            else:
                # if the student has not spoken, add them to the preDeck
                preDeck.append(student)

        # return both lists as a tuple
        return preDeck, postDeck


    def _createDeck(self):
        """ 
        Parameter: N/A

        Called By:
            __init__()

        Calls:
            random  -   randint()

        Modifies/Side Effects: self.preDeck

        Return: list of Student objects of length deckSize

        Description:
            Add deckSize number of randomly selected Student objects
            from self.preDeck to the list which will be used to fill
            self.deck. Remove those Student objects from self.preDeck.
        """
        # init temp deck
        tempDeck = list()

        # add self.deckSize number of students
        for i in range(self.deckSize):

            # generate the random index into self.preDeck
            index = randint(0,len(self.preDeck)-1)

            # add the random Student to the temporary deck
            tempDeck.append(self.preDeck[index])

            # remove that random Student from self.preDeck
            self.preDeck.remove(self.preDeck[index])

        # return the temp deck
        return tempDeck


    def _moveToDeck(self):
        """ 
        Parameter: N/A

        Called By: 
            Classroom.py    -   moveToPost()

        Calls:
            random  -   randint()
            Classroom.py    -   _refresh()

        Modifies:
           self.deck
           self.preDeck

        Return: None

        Description:
            Add a random Student from the self.preDeck list to the
            self.deck; if self.preDeck is empty then it refills it
            via the _refresh() call.
        """
        # check if self.preDeck is empty, if it is call _refresh() to
        # refill it
        if (len(self.preDeck) == 0):
            self._refresh()

        # get index of random Student in preDeck
        index = randint(0,len(self.preDeck)-1)

        # add the random Student to the deck
        self.deck.append(self.preDeck[index])

        # remove the random Student from the preDeck
        self.preDeck.remove(self.preDeck[index])

        return None


    def _refresh(self):
        """ 
        Parameter: N/A

        Called By:
            Classroom.py    -   _moveToDeck()
        
        Calls:
            Student.py  -   setSpoken()

        Modifies:
            self.preDeck
            self.postDeck
            Student objects in self.postDeck

        Return: None
        Description:
            Move all Student objects in self.postDeck to self.preDeck 
            and reset their spoken fields to False. Called when the
            self.preDeck is empty and a new Student is to be moved to
            self.deck.
        """
        # for each Student object in postDeck
        for student in self.postDeck:

            # remove student from postDeck
            self.postDeck.remove(student)

            # reset spoken field of Student
            student.setSpoken(False)

            # re-add Student to preDeck
            self.preDeck.append(student)

            return None


    def markAbsent(self, index:int):
        """ 
        Parameter: 
            index   -   index of student in self.deck to be marked absent 

        Called By:
            InstructorInterface.py  -   Absent() 

        Calls:
            Classroom.py    -   _moveToDeck()
            Student.py      -   setPresent()
            Student.py      -   incrementAbsences()

        Modifies: 
            self.deck
            self.absent
        
        Return: 
            updated self.deck list[Student]

        Description:
            When called removes Student at index from the deck, marks 
            them as absent, adds them to the absent list, and then
            repopulates self.deck with a new student.
        """
        # grab absent Student reference
        student = self.deck[index]

        # set their present status to False
        student.setPresent(False)

        # add them to the absent list
        self.absent.append(student)

        # remove them from the deck so they don't come up again
        self.deck.remove(student)

        # repopulate deck
        self._moveToDeck()
        
        # return updated deck
        return self.deck

    def moveToPost(self, index:int, flag:bool=False):
        """ 
        Parameter: 
            index   -   index of student to be moved from self.deck
                        self.postDeck.
            flag    -   a bool for whether the Student was flagged or
                        not.
        Called By:
            InstructorInterface.py  -   UpArrowKey()            
            InstructorInterface.py  -   DownArrowKey()            

        Calls: 
            Student.py  -   setSpoken()
            Student.py  -   incrementContributions()
            Student.py  -   incrementFlag()
            Classroom.py    -   _moveToDeck()

        Modifies:
            Classroom.py    -   self.deck
            Classroom.py    -   self.postDeck

        Return: self.deck (post modification)

        Description:
            Remove Student at index from self.deck and to self.postDeck, 
            set that Student's spoken, current_contributions and flag
            fields, then add a new Student to the self.deck via
            self._moveToDeck().
        """

        # Student speaks in order to be removed from the deck so set
        # spoken field to True
        self.deck[index].setSpoken(True)

        # Student has spoken so increment contributions field
        self.deck[index].incrementContributions()

        # increment flag field
        if flag: 
            self.deck[index].incrementFlag()

        # add Student to the self.postDeck
        self.postDeck.append(self.deck[index])

        # remove the Student from the self.deck
        self.deck.remove(self.deck[index])

        # move a new Student to the deck
        self._moveToDeck()

        # return the updated self.deck
        return self.deck


    def getDeck(self):
        """
        Parameter: N/A
        Called By:
            ColdCall.py     -   called in instantiation of
                            InstructorInterface object to give
                            initial state of deck.
        Calls: N/A
        Modifes: N/A
        Return: self.deck (list of Student)
        Description:
            Allows quick access to current state of the deck
        """
        return self.deck


    def mergeDecksToList(self):
        """
        Parameter: N/A

        Called By:
            ColdCall.py     -   called to save the current state of the
                            program for writing to files

        Calls: 
            Student.py  -   toStrList()

        Modifies: N/A

        Return: 
            list of list of str, where each list in the outer list is
            a comprised of a Student object's information as strings.

        Description:
            Compile a list of all Student objects' string
            representations (as lists of strings) across self.deck,
            self.preDeck, and self.postDeck. This will be used to
            write to files.
        """
        # compile list of ALL Student objects
        masterList = self.postDeck + self.preDeck + self.deck + self.absent

        # init list for holding Student info lists
        studentList = list()

        # for each of the Student objects
        for student in masterList:

            # add the current Student object's information as a list
            # of strings to the return list
            studentList.append(student.toStrList())

        return studentList





