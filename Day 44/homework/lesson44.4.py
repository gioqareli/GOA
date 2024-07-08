# Write a while loop that processes a list of numbers, doubling each number, and prints the new list.

numbers = [2, 4 , 6 , 8 ,]
double = []
index = 0

while index <len(numbers):
    double.append(numbers [index] * 2)
    index += 1
print(double)