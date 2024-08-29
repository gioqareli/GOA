#მომხმარებელს ჯერ შემოატანინეთ ბიუჯეტი, შემდეგ კი ის თანხა, რომელიც სასურველი ნივთის საყიდლად სჭირდება. დაბეჭდეთ შეუძლია ყიდვა თუ არა.

budget = int(input("enter your budget:"))
money = int(input("how much does it cost?:"))

if budget < money:
    print("you can buy it")
else:
    ("you cant buy it")