class Employee:
    def _init_(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

e1 = Employee(101, "Rahul", 50000)

print("ID:", e1.employee_id)
print("Name:", e1.name)
print("Salary:", e1.salary)
