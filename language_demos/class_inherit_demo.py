class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 0

    def full_name(self):
        return self.first_name + " " + self.last_name

    # def __len__(self):
    #     return 23        


class Student(Person):

    def __init__(self, student_id, first_name, last_name):
        super().__init__(first_name, last_name)
        self.student_id = student_id

    def full_name(self):
        return "Override > " + super().full_name()

    def record_info(self):
        return f"{self.student_id} {self.last_name}, {self.first_name}"

    # def __len__(self):
    #     return 42        


student = Student(1, "Bob", "Smith")

# print(student.full_name())
# print(student.record_info())

# msg = "this is fun"

# nums = [1,2,3,4,5]

# print(len(msg))
# print(len(nums))
# print(len(student))

print(issubclass(Student, Person))
print(isinstance(student, (Student, Person)))

print(Student.__mro__)