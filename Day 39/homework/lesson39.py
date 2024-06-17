even = []
odd= []

for i in range(10):



    input_number = int(input("enter number:"))

if input_number %2 == 0:
    even.append(input_number) 
else:
    odd.append(input_number)

print(even)
print(odd)