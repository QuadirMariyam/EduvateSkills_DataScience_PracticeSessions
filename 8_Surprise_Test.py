# 📝 1. Mini Assignments (Concept Practice)
# 🔹 Number Problems (not functions)
# Palindrome Number → Check if a number reads the same backward (121, 1331).
# Armstrong Number → Check if sum of cubes of digits = number itself (153, 370).
# Perfect Number → Sum of divisors/ factors = number (28 = 1+2+4+7+14).
# Special Number → Sum of factorial of digits = number (145 = 1!+4!+5!).
# Strong Number → Like special, but only for factorial-based numbers. X
# Prime Number Check → Also extend to generating primes in a range.
# Fibonacci Series → First n numbers. 1 1 2 3 5 8 13 21 ....

import numpy

arr = numpy.array([1,2,3,4])
print(arr)

# add two lists and print their sum. ex, taking phy, chem, and bio marks of 5 students and finding avg as science
import time
start = time.time()
phy = [33, 45, 67, 80, 94]
chem = [45, 45, 56, 78, 60]
bio = [70, 72, 72.5, 73, 50]

sci = []
# sci= phy + chem + bio
# for i in range(5):
#     print(phy[i])

for i in range(5):
    sci.append((phy[i] + chem[i] + bio[i])/3)


print("List time:", time.time() - start)