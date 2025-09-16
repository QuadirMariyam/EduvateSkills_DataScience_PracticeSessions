# Classes, Functions, Modules, Packages and Imports
# class <classname> :
# Properties and Functions
# What is the class concept and why? >> reusability

# class student:
#     name = "Manideep"
#     roll = 3
#     subject = "Data Science"

# s3 = student() #object initialized and defined
# s4 = student() #object = <classname>()
# print(s3.name)
# print(s4.name)
# print(student.name)

# init -> keyword for initialization of objects 
# automatically runs on creation of objects
# below is all about attributes in a class

# class studentOfDataScience:
#     course = "Data Science" #class owned property/ attributes

#     def __init__(self, name="unknown", roll="0"): # object owned properties
#         print("Running")
#         self.name = name 
#         self.roll = roll

    


# s1 = studentOfDataScience() # the brackets do not belong to the class, but to the init of the class
# print(s1.roll)
# print(s1.course)
# print(s1.name)

# s2 = studentOfDataScience("Abinash", 45)
# s3 = studentOfDataScience("Sucharu", 46)

# below is all about functions

class student:
    course = "Data Science" 
    address = "DLF" 
    roll = 89 #less priority compared object/ instance owned attributes
    classname = "EduvateSkills"   # class owned property/attributes which is default for all objects

    def __init__(self, name="Unkown", roll=0, course="MERN"): # a function which allows objects to own properties/ attributes # the value passed here are called arguement or parameter
        self.name = name 
        self.roll = roll
        self.course = course

    # enter, study, doubts, exit >> functions are specific actions that are performed
    def greet(self):
        print("Welcome to the", self.course, "class")

    @classmethod
    def clsbegin(cls):
        print("Your class has already begun for the", cls.course, cls.roll)

    @classmethod
    def greet(cls):
        print("Welcome to the", cls.course, "class")

    @staticmethod
    def greet():
        print("Welcome to the class")

    @staticmethod
    def percentage(total, *args): #arguements
        numerator = sum(args)
        # denominator = len(m)*100
        percent = (numerator/total)*100
        print("Your percent is:", percent, "%")

    #func - user-input single integer to print "You entered the class at {time}"

# print(course)
s1 = student("Manideep", 34) # the brackets do not belong to the class, but to the init of the class
print(s1.name)
print(s1.roll)
print(s1.course)
print(s1.address)
s1.greet()
s1.clsbegin()
s1.percentage(300, 34, 67, 50) # parameters
s1.percentage(300, 56, 78, 89)
s1.percentage(200, 34, 56)
s1.percentage(300, 34, 67, 50)
s1.percentage(300, 34, 67, 50)

s2 = student("Abinash", 45) #object/ instance 2 created of class student
print(s2.name)
s2.percentage(300, 56, 78, 89)
s3 = student()
print(s3.name, s3.roll)
s4 = student("Ipshita", 7)
hre = student("Sneha", 9, 9)
hre.clsbegin()

# wap to create an animal class, define different animal as object which should have some similar functions ex, breathe, eat, poop
# wap to define a car company as class which should have attributes like model, color, wheels. these attributes should vary from object to object

# methods are commonly of 4 types
# 2nd classmethods - 1. methods should have a decorater - @classmethod, 2. cls is the arguement taken here, 3. checks in class attributes only
# 3rd instancemethods - 1. methods which take arguement as self, 2. gives priority to instance attribute first and then to class attributes
# 1st staticmethods - 1. neither take 'self' nor 'cls' for arguement, 2. gives priority to none, 3. can initialize without any arguement or as much as the user wants, 4. methods should have a decorater - @staticmethod
# special methods - dunder (Double UNDERscore) -(only init method defaultly exists even if the user has not created one)

print()
greeting()

