#შექმენით ფუნქცია რომელშიც იქნება რიცხვებით სავსე სია და ფუნქცია დააბრუნებს ამ რიცხვების ჯამს

def sumnumbers():
    sum = 0
    num = [2,3,4,5,6,7,8,9,]
    for i in range(len(num)):
        sum += num[i]
    print(sum)

sumnumbers()