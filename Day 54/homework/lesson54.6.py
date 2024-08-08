# შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს და თუ ის დადებითი იქნება, დააბრუნებს "დადებითი", და თუ უარყოფითი იქნება, "უარყოფითი".

def type():
    num = int(input("enter number:"))
    if num <= 0:
        print("this number is negative")
    else:
        print("this number is positive")
    
type()