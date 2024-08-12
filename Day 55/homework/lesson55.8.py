#დაწერე ფუნქცია, რომელიც იღებს number პარამეტრს და აბრუნებს number-ის კუბს. მაგალითად, გამოიყენე არგუმენტი 3. (გამოიტანა: 27)

number = int(input("enter random number:"))
cub = number ** number
def cub_number(number):
    return str(number) + "  " + " კუბია " + "  " + str(cub)
print(cub_number(number))
