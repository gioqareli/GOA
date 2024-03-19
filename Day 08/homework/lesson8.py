#მომხმარებელს შეეკითხეთ მისი ასაკი, ასევე შეეკითხეთ რამდენი წლით სურს დროში მოგზაურობა და დაპრინტეთ რამდენი წლის იქნება დროში მოგზაურობის შემდეგ
user_name = input("what is your name?:  ")
user_surname = input ("what is your surname?:  ")
user_age = input ("how old are you before travel?:  ")
time_travel = input ("do you want to travel in the past or in the future?:  ")
new_user_age = int(user_age) + 20
print( "my name is" + user_name + " my surname is " + user_surname + " Im  " + user_age  + " I want to travel in the future " + str(new_user_age) +  "  yers old after travel"  )
