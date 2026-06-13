class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def _init_(self, name, age, roll_number):
        super()._init_(name, age)
        self.roll_number = roll_number

s = Student("Pradhyumn", 20, 101)

print("Name:", s.name)
print("Age:", s.age)
print("Roll No:", s.roll_number)
