#შექმნი ფუნქცია, რომელიც იღებს a და b პარამეტრებს და აბრუნებს მათ ჯამს. მაგალითად, გამოიყენე არგუმენტები 7 და 3. (გამოიტანა: 10)

a = int(input("enter random numberr:"))
b = int(input("enter second random number:"))
sum = a + b
def sum_number( a , b ):
    return str(a) + "  " + " დამატებული" + "  " + str(b) + "  " + " უდრის " + "  " + str(sum)

print(sum_number( a , b ))