# Write a while loop that asks the user to guess a number between 1 and 10 until they get it right. The correct number is 7.
correct_number = 7
question = int(input("guess a number between 1 and 10:") )

while question != correct_number:
    print("try again")
    question = int(input("guess a number between 1 and 10:") )

else:
    print("congrats")

    



