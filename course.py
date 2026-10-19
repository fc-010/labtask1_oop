
# i got stuck in file handling so i use microsoft copilot


class InvalidMarksError(Exception):
    """create custom error for invalid marks"""
    pass

class Course:


    def __init__(self, name: str):
        self.name = name
        self.marks = {}   # student -> marks

    def add_student(self, student: str, marks: int):
        if not 0 <= marks <= 100:
            raise InvalidMarksError(f"Invalid marks for {student}: {marks}")
        self.marks[student] = marks

    def average(self) -> float:
        return sum(self.marks.values()) / len(self.marks)

    def top_student(self) -> str:
        return max(self.marks, key=self.marks.get)

    def __len__(self) -> int:
        return len(self.marks)

    def __str__(self) -> str:
        return f"{self.name}: {len(self)} students, average {self.average():.1f}"

def load_course(name: str, filename: str) -> Course:
    course = Course(name)
    try:
        with open(filename) as f:
            for line in f:
                try:
                    student, mark = line.strip().split(",")
                    course.add_student(student.strip(), int(mark.strip()))
                except ValueError:
                    print(f"Skipping {student.strip()}: marks is not a number")
                except InvalidMarksError as e:
                    print("Skipping:", e)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    return course

if __name__ == "__main__":
    test = Course("Test")
    test.add_student("A", 50)
    print(test)