class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hobby(self):
        print('Loves playing football')

#  new object creation from class . This is not inheritance
person1 = Person('Hamid', 23)
print('New person \nName: {}\nAge: {}'.format(person1.name, person1.age))
person1.hobby()

# inheritance
#  passing attributes and methods from parent class to child class is called inheritance
class Student(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)

student1 = Student('Ratul', 22)
print('New Student.\nName: {}, Age: {}'.format(student1.name, student1.age))
student1.hobby()

# if we want to change any attribute/method in child class, then we have to overwrite it. Like as -
# class Student(Person):
#     def __init__(self, name, age):
#         Person.__init__(self, name, age)
#     def hobby(self):
#         print('Student likes to play cricket')

# student1 = Student('Rahim', 19)
# student1.hobby()
