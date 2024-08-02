# შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს და შემდეგ კი დააბრუნებს დაბეჭდავს მომხმარებლის შემოტანილი რიცხვი კენტია თუ ლუწი
    
def type():
    num = int(input("enter random numbers:"))

    if num % 2 == 1:
        print("this number is odd")
    else:
        print("this number is even")
    
type()