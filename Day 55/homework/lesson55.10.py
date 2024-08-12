#დაწერე ფუნქცია, რომელიც იღებს number პარამეტრს და აბრუნებს "კენტი" ან "ლუწი". მაგალითად, გამოიყენე არგუმენტი 8. (გამოიტანა: "ლუწი")```

number = int(input("enter randomm number:"))
def even_odd(number):
    if number % 2 == 0:
        return("thease number is even")
    else:
        return("thease number is odd")
    
print(even_odd(number))