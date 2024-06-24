list = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
reverse_list = []
for i in range(len(list)):
    reverse_list.append(list[-i - 1])
print(reverse_list)