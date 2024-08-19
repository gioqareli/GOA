#Create a script that uses a function with keyword arguments. 

name = input("Enter Your Name:")
surname = input("Enter Your Surname:")
age = int(input("Enter Your Age:"))
adress = input("Enter Your Adress:")
def user(name , surname , age , adress):
    return "Heloo" + " " + name + "  "  + surname + " " + " " +"Your Age Is" + " " +str(age) + " " + " " + "Your Adress Is" + " " + adress
print(user(name , surname , age , adress))
