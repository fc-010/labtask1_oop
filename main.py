
from course import Course, InvalidMarksError, load_course


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def passed(self):
        return self.marks >= 50

    def __str__(self):
        return f"{self.name} ({self.marks}): {'Pass' if self.passed() else 'Fail'}"

students = [Student("Saad", 72), Student("Sara Niaz", 45), Student("Omar Akmal", 50)]
for s in students:
    print(s)




c = Course("Programming for AI")
c.add_student("Saad ", 88)
c.add_student("Sara Niaz", 92)
c.add_student("Omar Akmal", 75)
print(len(c))
print(c.average())
print(c.top_student())


try:
    c.add_student("Bilal Saeed", 120)
except InvalidMarksError as e:
    print("Error:", e)
print(c)



c = Course("X"); c.add_student("Ali",88)
c.remove_student("Ali")
print(len(c))
try:
    c.remove_student("Zara")
except KeyError as e:
    print("KeyError:" ,e)


course = load_course("Programming for AI", "marks.txt")
print(course)
print("Top student:", course.top_student())