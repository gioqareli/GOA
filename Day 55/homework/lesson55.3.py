#დაწერე ფუნქცია, რომელიც იღებს length და width პარამეტრებს და ითვლის მართკუთხედის ფართობს. მაგალითად, გამოიყენე არგუმენტები 4 და 6. (გამოიტანა: 24)

length = int(input("enter triangle length:"))
width = int(input("enter triangle width:"))
sum = length * width
def triangle_are(length , width):
    return "მართკუთხედის ფართობია" + "  " + str(sum)
print(triangle_are(length , width))
