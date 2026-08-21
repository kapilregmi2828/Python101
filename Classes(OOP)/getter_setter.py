class Person:
    def __init__(self, name):
        self.name = name
        self.__grade = 0

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100.")

    def get_grade(self):
        return self.__grade

    def status(self):
        if self.__grade >= 60:
            return "Pass!"
        else:
            return "Fail!"

p1 = Person("Kapil")
p1.set_grade(99)
print(p1.get_grade())
print(p1.status()) 