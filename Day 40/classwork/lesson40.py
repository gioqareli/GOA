even = []
odd= []
list = []

for i in range(5):
    num = int(input("enter number:"))
    list.append(num) 


for i in range(len(list)):
    if list[i] % 2 == 0:
        even.append(list[i])
    else:
        odd.append(list[i])

print(even)
print(odd)       