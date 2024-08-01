import random

choices = ["ჭა","ქაღალდი","მაკრატელი"]

computer_choice = random.choice(choices)

user_choice = input("შეიყვანეთ თქვენი არჩევანი (ქვა,ქაღალდი,მაკრატელი):" )

while user_choice not in choices:
    print("სცადეთ თავიდან")
    user_choice = input("შეიყვანეთ თქვენი არჩევანი (ქვა,ქაღალდი,მაკრატელი):" )

print("თქვენ აირჩეთ",user_choice)
print("კომპიუტერმა აირჩია",computer_choice)

if user_choice == computer_choice:
    print("ფრეა")
elif (user_choice == "ჭა" and computer_choice == "მაკრატელი") or \
     (user_choice== "მაკრატელი" and computer_choice == "ჭა") or \
     (user_choice== "მაკრატელი" and computer_choice == "ქაღალდი") or \
     (user_choice == "ქაღალდი" and computer_choice == "ჭა"):
     print("თქვენ მოიგეთ")

else:
    print("კომპიუტერმა გაჯობა და მოგიგო")
