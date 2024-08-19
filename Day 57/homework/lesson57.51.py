#Write a script that uses a while loop with a continue statement.

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1