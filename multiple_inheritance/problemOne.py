# Create multiple inheritance on teacher,student and youtuber.
# Q. if we have created teacher and now one student joins master degree with becoming teacher then what??
#
# Ans :  just make subclass from  teacher so that student will become teacher

class Teacher:
    def teacher_action(self):
        print("This is teacher action")


class Youtube:
    def youtube_action(self):
        print("This is Youtube action")


class Engineer:
    def engineer_action(self):
        print("This is Engineer")


class Student(Teacher, Youtube, Engineer):
    def student_action(self):
        print("This is student")


std = Student()
std.student_action()
std.teacher_action()
std.youtube_action()
std.student_action()
