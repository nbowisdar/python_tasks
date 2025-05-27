class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name: str, age: int, course: str):
        pass


# Create an instance
student = Student("Den", 22, "math")
print(student.name)   
print(student.age)  
print(student.course) 
