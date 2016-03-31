# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

# Setting inital values
sum_squares = 0
square_sum = 0

for n in range(101):
    # Calculates the sum of the squares
    sum_squares += (n * n)
    # Gets the sum of the first 100 natural numbers
    square_sum += n

# Square the sum of the first 100 nat num
square_sum = (square_sum * square_sum)

print("Square of the sum = ", square_sum, " Sum of the squares = ", sum_squares)

# Get the differnce
diff = square_sum - sum_squares

print(diff)
