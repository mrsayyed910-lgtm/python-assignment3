class Student:
    def _init_(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

s1 = Student("Pradhyumn", 20, "Data Science")

print("Name:", s1.name)
print("Age:", s1.age)
print("Course:", s1.course)
