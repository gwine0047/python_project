names = ["Jane", "John"]

while True:
    name = input("Enter your name: ")

    if name not in names:
        names.append(name)
        print("You have been registered!")
        print(names)

    else:
        print("You are already registered")
        print(names)
        exit()
