#Write a script to perform arithmetic operations.
num_1 = int(input("enter first number:"))
num_2 = int(input("enter second number:"))  
math = int(input("არჩიეთ მოქმედება: 1 (მიმატება), 2 (გამოკლება), 3 (გამრავლება), 4 (გაყოფა)") )

if math == 1:
    print(num_1 + num_2)
elif math == 2:
    print(num_1 - num_2)

elif math == 3:
    print(num_1 * num_2)
else:
    print(num_1 // num_2)