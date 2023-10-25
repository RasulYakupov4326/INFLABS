def major(line):
    objects = line.split()
    length = len(objects)
    library = []
    for i in range(length):
        library.append([])
    for x in range(length):
        for y in range(length):
            if len(library[y]) == 0:
                library[y].append(objects[x])
                library[y].append(1)
                break
            elif library[y][0] == objects[x]:
                library[y][1] += 1
                break
    for a in range(length):
        if len(library[a]) == 0:
            break
        elif library[a][1] > length//2:
            print(library[a][0])


condition = True
while condition:
    print("Введите строку")
    inputLine = input()
    if len(inputLine.split()) != 0:
        major(inputLine)
        condition = False
    else:
        print("Введенная строка пустая")
