 #ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცვს და დააბრუნებს "მაგარია!", თუ რიცხვი 10-ზე მეტია.

def cool():
    num = int(input("enter random number :"))
    if num >= 10:
        return("wow cool")
    else:
        return("try again")
print(cool())