#Functions/ Methods - A block of reusable code which performs a specific task - which will be performed only when you call a function

# it should have a name
# while defining any function, it always starts with the keyword 'def'
# it helps you perform specific work or function
# only when you call a function, it gets executed
# you can call it and use it multiple times - promotes code reusability - helps to avoid code repetation
# can take parameters as values and return outputs

# types of functions - 4
# no params, no return
# a = 19

# def greet(): #staticmethod default
#     print("Hello, Welcome to Eduvate Skills")
#     return

# print(greet())
    
# no params, return

# a = 23 # value of a is updated from 19 to 23, just like that, value of greet() is updated
# def greet():
#     msg = "Hello, here at Eduvate Skills"
#     return msg

# message = greet()
# print(message)

# params, return

# add of 2 nos - param = 2 nos, return sum value

def add(a, b):
    return a + b
#     return s

# addvalue = add(2, 3)

# print(addvalue)

# params, no return value

# wap message with name

def greeting(name):
    '''
    This message should come when you hover over the greet()
    '''
    a = 10
    print("Hello", name, a)
    return

# greeting("Abinash")
# greeting("Manideep")

# n = input("Type your name:")
# greeting(n)




# print()

# Write a function is_even(num) → returns True if number is even.

# Write a function average(a, b, c) → returns average of 3 numbers.

# Write a function reverse_string(s) → returns reversed string.

# Write a function count_vowels(s) → counts vowels in a string.

# Write a function max_of_list(numbers) → finds maximum in a list.


# Write functions:

# add_student(students, name, marks) → add student (dict inside list).

# def add_student(students, name, marks):
#     pass

# add_student()

# find_topper(students) → return name of highest scorer.

# average_marks(students) → return average marks.