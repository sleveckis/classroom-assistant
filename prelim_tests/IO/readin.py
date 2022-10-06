"""Author: Nick"""
"""
This is just testing to make sure data is readable using tabs and the format
provided in the handout
"""
import students


def main():
    student_dict = dict()
    student_file = open("sample.txt", "r")
    for student in student_file:
        student_info = student.split("\t")
        student_dict.update({students.Student(student_info[0], student_info[1],
            student_info[2], student_info[3], student_info[4]) : "PLACE_HOLDER"})

    for element in student_dict:
        print(element)
        print(student_dict[element])


if __name__ == "__main__":
    main()

