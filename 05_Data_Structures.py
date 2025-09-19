# Built-in DS in Python - List - [], String -(), Tuple - (1,2), Set - {1, 2, 3}, Dictionary - {1 : "one", 2 : "Two", "noodles" : "200"}
# What are the differences among the data structures in python mentioned above
# diff in brackets
# print(1, end=",")
# print(2)

# for i in range(11):
#     print(i, end=",")

# 1. enhance communication, corporate skill - help for interview >> geeksforgeeks
# topic - repl/ vscode, working of components, theory/ backend, interesting facts
# >> array vs lists - mn
# >> slicing in list - sd
# >> OOPs in Python - ib

# wap that takes input of marks of 5 students in a list,
# print - highest mark, lowest mark, average marks of 5 students, cont of students who passed(>=40)


marks = []
for i in range(5):
    mark = int(input("Enter your mark: "))
    marks.append(mark)

c = 0
for m in marks:
    if m >= 40:
        c += 1

print("Number of students who have passed are:", c)

# same question using count ()


# you have studied, DS and Python programming - Leetcode/ Hackerrank/ Codechef (competetive Programming, Interview - Technical assessment)
# Kaggle