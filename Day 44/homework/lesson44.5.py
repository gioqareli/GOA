# Write a while loop that repeatedly asks the user to enter a password until the correct password "password123" is entered.

coreect_password = "password123"
guess = input("enter correct password:")
while guess != coreect_password:
    print("try again")
    guess = input("enter correct password:")
else:
    print("congrats")
   
  

