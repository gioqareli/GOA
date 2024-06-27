list = [10 , - 5 , -15 , 15 , 7 , -3 , -33 , 35 , -87]
positive = []
negative = []

for i in range (len(list) ):
    if list[i] < 0:
        negative.append(list[i])
    else:
        positive.append(list[i])       
        
 


print(positive)
print(negative)