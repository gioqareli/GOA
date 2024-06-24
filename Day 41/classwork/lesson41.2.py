num = [4 ,  8 , 12 , 45 , 13 , 14 , 2 , 3 , 7 , 50 , 90 ]
sum = 0

for i in range(len(num)):
    if num [i]  % 5 == 0:
        sum += num[i]

print(sum)
