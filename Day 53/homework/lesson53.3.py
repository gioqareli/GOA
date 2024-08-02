# შექმენით ფუნქცია რომელშიც დააბრუნებს სიაში არსებული რიცხვების საშუალო არითმეტიკულკს

def average():
    sum = 0
    lst = [2,4,6,8,10,11,12,13,19]
    aver = 0
    for i in range (len(lst)):
        sum += lst[i]
        aver = sum / len(lst)
    print(aver)

average()