import math

condition = True
while condition:
    line = input()
    generalSize = 0
    if line != '':
        line = line.split()
        for word in line:
            wordSize = len(word)
            generalSize += len(word)
        rightSize = math.ceil(generalSize/len(line))
        condition = True
        minDif = rightSize
        for word in line:
            minDif = min(abs(len(word) - rightSize), minDif)
        for word in line:
            if abs(len(word) - rightSize) == minDif:
                print(word)
        condition = False
    else:
        print("Введенная строка пустая")