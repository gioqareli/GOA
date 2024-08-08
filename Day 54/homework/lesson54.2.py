 #ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცვს და დააბრუნებს "მაგარია!", თუ რიცხვი 10-ზე მეტია.

def cool():
    num = int(input("enter random number :"))
    if num >= 10:
        print("wow cool")
    else:
        print("try again")

cool()