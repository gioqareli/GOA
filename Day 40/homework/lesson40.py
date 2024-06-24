numbers = [10, 15 , 20 , 3 , 5 , 1121 , 90 , 34 , 45 , 3 , 11,]
numbers_2 = []
counter = 0

for i in range(len(numbers)):
    if len(str(numbers[i]) ) == 2:
        counter += 1

print(counter)
