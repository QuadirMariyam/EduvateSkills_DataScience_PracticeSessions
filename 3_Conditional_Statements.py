# conditionals - decision making
# # user-input / user-defined variable

# n = input("Enter a number") #keywords in python
# print("The number is:", n) #can take value in any data type

# age = int(input("Enter a age: ")) #keywords in python int(34)

# if age >= 18:
#     print("You are an adult, Congrats")
# else:
#     print("You are a child")

# use if-else to print "Even" if a user-defined is even and vice versa "The number is odd"


# wap if marks & grades
# 90 - 100, A 
# 80 - 90, B
# 70 - 80, C
# 60 - 70, D
# below 60, E

# multiple ifs

# marks = int(input("Enter your marks: "))

# if (marks > 90) and (marks <= 100):
#     print("A")
# if (marks > 80) and (marks <= 90):
#     print("B")
# if (marks > 70) and (marks <= 80):
#     print("C")
# if (marks > 60) and (marks <= 70):
#     print("D")
# # if (marks <= 60):
# else:
#     print("E")
# print("Thank you")

# 1. every if condition is executed 2. else is connected only to the last if

# nested if
# if (marks > 90) and (marks <= 100):
#     print("A")
#     if (marks > 80):
#         print("B")
#         if (marks > 70):
#             print("C")
#             if (marks > 60):
#                 print("D")
# # if (marks <= 60):
#             else:
#                 print("E")
# print("Thank you")


# all the ifs are true

# age < 18 child, age > 18 adult, age > senior citizen

# age = int(input("Enter your age: "))

# if age >= 18:
#     if age < 60:
#         print("Adult")
#     else: 
#         print("Senior Citizen")
# else:
#     print("Child")
# print("Thanks")

# elif ladder
# marks = int(input("Enter your marks: "))

# if (marks > 90) and (marks <= 100):
#     print("A")
# elif (marks > 80):
#     print("B")
# elif (marks > 70):
#     print("C")
# elif (marks > 60):
#     print("D")
# else:
#     print("E")
# print("Thank you")

# all if-else and elif are connected
# if the mark is higher so, all the ifs are not tried 
# only if mark is lower, all ifs are tried


# if (marks > 90) and (marks <= 100):
#     print("A")
#     if (marks > 80):
#         print("B")
#         if (marks > 70):
#             print("C")
#             if (marks > 60):
#                 print("D")
# # if (marks <= 60):
#             else:
#                 print("E")
# print("Thank you")


# grading system 
# 90+ - A
# 75 - 89 - B
# 40 - 74 - C
# below 40 - Fail


# Discount Calculator
# purchase > 1000 - 10% discount
# purchase > 500 - 5% discount
# else no discount


# login check 
# user id & password
# if correct - "Welcome"
# else - "Invalid password"


# if-else Comprehension

# if_condition:
# true_value (statements execute)
# else: 
# false_value (statements execute)

# true_value if condition else false_value # ex, age >= 18 print eligible else print eligible
# if mark <= 40 then fail, else pass
# if number %= 2 then even else odd
# if year is leap year or not

# age = 7
# print("eligible") if age >= 18 else print("Ineligible") # one-liner previous questions redo in this syntax

# a = 5, b = 2 find out the minimum in if-else comprehension

# a = 5
# b = 2

# mini = a if a < b else b
# print(mini)




