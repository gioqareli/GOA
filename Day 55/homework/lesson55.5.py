# ფუნქცია, რომელიც იღებს number პარამეტრს და აბრუნებს "დიდია" თუ number 10-ზე მეტია და "პატარა" თუ ნაკლებია. მაგალითად, გამოიყენე არგუმენტი 9. (გამოიტანა: "პატარა")

number = int(input("enter random number:"))
def size(number):
    if number > 10:
        return("დიდია")
    else:
        return("პატარაა")
print(size(number))
    

