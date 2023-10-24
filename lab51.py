matrix = []
condition = True
while condition:
    print("Введите 1 строчку матрицы")
    firstLine = input().split()
    if len(firstLine) == 0:
        print("Введена пустая строчка")
    else:
        error = 0
        for symbol in firstLine:
            try:
                symbol = int(symbol)
            except ValueError:
                print("Incorrect input")
                error += 1
                break
        if error == 0:
            matrix.append(firstLine)
            condition = False
for i in range(len(matrix[0]) - 1):
    print("Введите", i + 2, "строчку матрицы")
    condition = True
    while condition:
        otherLines = input().split()
        if len(otherLines) == 0:
            print("Введена пустая строчка")
        elif len(otherLines) != len(matrix[0]):
            print("Строчка не соответствует данной матрице")
        else:
            error = 0
            for symbol in otherLines:
                try:
                    symbol = int(symbol)
                except ValueError:
                    print("Incorrect input")
                    error += 1
                    break
            if error == 0:
                matrix.append(otherLines)
                condition = False
middleValues = []
for a in range(len(matrix[0])):
    middleValues.append([0, 0])
for rows in range(len(matrix[0])):
    for columns in range(len(matrix[0])):
        middleValues[rows][0] += int(matrix[rows][columns]) / len(matrix)
        middleValues[columns][1] += int(matrix[rows][columns]) / len(matrix)
result = 0
for x in range(len(matrix)):
    result += middleValues[x][0] + middleValues[x][1]
print(result)
