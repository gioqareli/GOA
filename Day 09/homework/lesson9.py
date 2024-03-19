#მომხმარებელს შემოატანინეთ ორი რიცხვი, მისი ასაკი და მშობლის ასაკი, შემდეგ კი შეადარეთ ისინი ერთმანეთს

my_age = int( input("how old are you ?:  ") )
parent_age = int (input("what is your mom age ?: ") )
bulion = my_age < parent_age
print(bulion)
print(type(bulion))