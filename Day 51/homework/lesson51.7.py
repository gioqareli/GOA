sum = 0
num = [1,2,3,4,5,6,7,8,9,10]
half = 0
for i in range (len(num)):
    sum += num[i]
half = sum / len(num)
print(half)