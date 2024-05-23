# Appending File Challenge

def f_append():
    with open("users.txt", "a") as file:
        file.write("\nFor the challenge!")


def f_read():
    with open("users.txt") as file:
        for x in file:
            print(x)


f_append()
f_read()
