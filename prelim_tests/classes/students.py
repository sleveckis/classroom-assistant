"""Author: Nick"""
"""This will eventaully hold more attributes, this is just to test filling
the dictionary with basic student objects
"""


class Student(object):
    def __init__(self, first, last, id_num, email, phonetic):
        self.first = first
        self.last = last
        self.id_num = id_num
        self.email = email
        self.phonetic = phonetic

    def __str__(self):
        return f"First Name: {self.first}\n\
Last Name: {self.last}\n\
UO ID: {self.id_num}\n\
Email: {self.email}\n\
Phonetic: {self.phonetic}"


def main():
    pass


if __name__ == "__main__":
    main()

