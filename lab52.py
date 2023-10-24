def check(symbol):
    try:
        symbol = int(symbol)
        result = symbol
    except ValueError:
        result = "error"
    return result

def func(enteredMatrix, size):
    maximum = enteredMatrix[0][0]
    serialNumber = [0, 0]
    for x in range(size):
        if enteredMatrix[x][x] > maximum:
            maximum = enteredMatrix[x][x]
            serialNumber[0] = x
            serialNumber[1] = x
        if enteredMatrix[x][size - 1 - x] > maximum:
            maximum = enteredMatrix[x][size - 1 - x]
            serialNumber[0] = x
            serialNumber[1] = size - 1 - x
    halfSize = (size - 1)//2
    target = enteredMatrix[halfSize][halfSize]
    enteredMatrix[halfSize][halfSize] = maximum
    enteredMatrix[serialNumber[0]][serialNumber[1]] = target
    return enteredMatrix



print("Введите порядок матрицы")
condition = True
matrix = []

while condition:
    N = input()
    if check(N) != "error":
        if check(N) > 0 and check(N) % 2 != 0:
            condition = False
            N = int(N)
        else:
            print("Неправильный размер матрицы")
    else:
        print("Incorrect input")

for rows in range(N):
    condition = True
    while condition:
        counter = 0
        line = list(map(int, input().split()))
        for number in line:
            if check(number) == "error":
                print("Incorrect input")
                counter += 1
                break
        if counter == 0:
            if len(line) == N:
                matrix.append(line)
                condition = False
            else:
                print("Длина строчки не соответствует матрице")
matrix = func(matrix, N)
for line in matrix:
    print(line)
