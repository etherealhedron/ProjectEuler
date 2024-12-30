# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all multiples of 3 or 5 below 1000.

# Look to the sum of the first n integers formula for a closed form solution!

limit = 1000
# We use inclusion exclusion!

# A: The sum of all multiples of 3 below 1000.
A = 0
for i in range(3, limit, 3):
    A += i

# B: The sum of all multiples of 5 below 1000.
B = 0
for i in range(5, limit, 5):
    B += i

# C: The sum of all multiples of 15 below 1000.
C = 0
if limit > 15:
    for i in range(15, limit, 15):
        C += i

# Answer is A + B - C
Answer = A + B - C
print(Answer)