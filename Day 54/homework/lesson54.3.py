#შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს ორ ციფრს და დააბრუნებს მათ შორის უმცირესს.

def more():
    num_1 = int(input("enter random number:"))
    num_2 = int(input("enter random number:"))
    if num_1 < num_2 :
        print("num_1 is small")
    else:
        print("num_2 is small")
    
more()