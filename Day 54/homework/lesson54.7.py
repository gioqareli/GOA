# შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცხვს და დააბრუნებს True, თუ ის ლუწია  და False, თუ არა.

def number():
    num = int(input("enter number:"))
    if num % 2 == 1:
        print("False")
    else:
        print("True")

number()