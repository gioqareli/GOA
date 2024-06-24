more = []
less = []

for i in range(10):

    number = int(input("enter numbers:"))
    if number > 100:
        more.append(number)
    else:
        less.append(number)

print(more)
print(less)