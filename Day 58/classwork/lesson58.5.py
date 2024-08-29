# მომხმარებელს შემოატანინეთ 1 დან 7-ის ჩათვლით რომელიმე რიცხვი ამის შემდეგ კი გამოიყენეთ if elif else რომ შეუსაბამოდ კვირის დღე 1 ორშაბათისთვის 2 სამშაბათისთვის 3 ოთხშაბათისთვის და ასე შემდეგ

number = int(input("enter random number between 1 - 7:"))
if number ==1:
    print("ორშაბათი")
elif number ==2:
    print("სამშაბათი")
elif number ==3:
    print("სამშაბათი")
elif number ==4:
    print("ოთხშაბათი")
elif number ==5:
    print("ხუთშაბათი")
elif number ==6:
    print("პარასკევი")
elif number ==7:
    print("შაბათი")
else:
    print("კვირა")
