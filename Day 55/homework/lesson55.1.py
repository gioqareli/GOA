#დაწერე ფუნქცია, რომელიც იღებს x და y პარამეტრებს და აბრუნებს მათ სხვაობას. მაგალითად, გამოიყენე არგუმენტები 10 და 5. (გამოიტანა: 5)
x = int(input("enter random number:"))
y = int(input("enter second randomnumber:"))
sum = x - y
def deduction(x , y):
    return str(x) + " " + " გამოკლებული " + " " + str(y) + " უდრის" + "  " + str(sum)

print(deduction(x,y))