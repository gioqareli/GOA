#შექმენით დროში მოგზაურობის ფუნქცია რომელიც მომხმარებელს შეეკითხება მის ახლანდელ ასაკს და ამჟამინდელ წელს, ასევე რამდენი ხანით სურს დროშ მოგზაურობა შემდეგ კი ფუნქციამ უნდა დააბრუნოს დაბეჭდოს დროში მოგზაურობის შემდეგ რომელი წელი იქნება და რამდენი წლის იქნება მომხმარებელი, ასევე დაამატეთ რომ მომხმარებელმა მიიღოს გადაწყვეტილება წარსულში სურს დრში მოგზაურობა თუ მომავალში

def time_travel():
    age= int(input("enter your age:"))
    current_year = int(input("enter current year:"))
    years_to_travel = int(input("enter how many year do you want travel in time:"))
    direction = int(input("where do you want to travel: 1 (past) or 2 (future ):") )

    if direction == 1:
        new_yer = current_year - years_to_travel 
        new_age = age - years_to_travel
        
    elif direction == 2 :
        new_yer = current_year + years_to_travel 
        new_age = age + years_to_travel
       
    else:
        print("please try again")


    print("თვენ დროში მოგზაურობის შემდეგ იმყოფებით:" ,new_yer ,"წელს")
    print("თვენ დროში მოგზაურობის შემდეგ ხართ:" , new_age , "წლის")


time_travel()