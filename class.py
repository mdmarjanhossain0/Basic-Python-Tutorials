class Student:

    # class variable
    totalStudent = 0

    def classMethod(cls):
        print("Total Student ", cls.totalStudent)

    # Constractor
    def __init__(self,name, age):
        # Instance variable
        self.studentName = name
        self.age = age
        Student.totalStudent = Student.totalStudent + 1
        print("Constractor calling with ", name)

    # Instance method
    def details(self):
        print("My name is ", self.studentName)
        print("My age is ", self.age)

    # Static funtion
    def studentNameUppercae(name):
        print("Name is ",name)

# Object/ Inastance creation, only this information and class information
st1 = Student("Marjan", 21)
st1.details()
st1.classMethod()

st2 = Student("Abir", 23)
st2.details()
st2.classMethod()

st3 = Student("Hossain", 23)
st3.details()
st3.classMethod()

Student.classMethod()



