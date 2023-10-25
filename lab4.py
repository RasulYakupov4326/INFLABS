from main import major

condition = True
while condition:
    print("Введите строку")
    inputLine = input()
    if len(inputLine.split()) != 0:
        major(inputLine)
        condition = False
    else:
        print("Введенная строка пустая")
