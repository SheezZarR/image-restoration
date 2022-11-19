from copy import deepcopy

'''def sum_strings(s1, s2) -> list:
    for _ in range(len(s1)):
        s1[_] += s2[_]
    return s1

'''


def transposion(matrix) -> list:
    matrix = deepcopy(matrix)
    # Создаём новую матрицу
    T = list()
    for i in range(len(matrix[0])):
        T.append(list())
        for j in range(len(matrix)):
            # Заполняем её значениями исходной матрицы, меняя столбцы и строки местами
            T[i].append(matrix[j][i])
    return T


# Рекурсивная функция нахождения определителя
# Аргумент start отвечает за начало матрицы, нужен, чтобы вручную не создавать миноры
def determinant(matrix, start=0) -> int:
    matrix = deepcopy(matrix)
    # Выход из рекурсии
    if len(matrix) == start + 1:
        return matrix[start][start]

    # Адаптация матрицы к последующему алгоритму
    if matrix[start][start] == 0:
        for _ in range(start + 1, len(matrix)):
            matrix[start], matrix[_] = matrix[_], matrix[start]
            if matrix[start][0] != 0:
                break
        # Проверка на то нулевой определитель
        if matrix[start][0] == 0:
            return 0

    # Доводим все числа, кроме самого первого, в первом столбце до нуля
    for _ in range(start + 1, len(matrix)):
        mult = -matrix[_][start] / matrix[start][start]
        for i in range(start + 1, len(matrix[start])):
            matrix[_][i] += matrix[start][i] * mult

    # Возвращаем первое число матрицы, помноженное на минор
    return matrix[start][start] * determinant(matrix, start + 1)


def opposite(matrix) -> list:
    matrix = deepcopy(matrix)
    # Умножаем определитель^-1 матрицы на транспонированную матрицу

    det = determinant(matrix)
    if det == 0:
        return []
    add_matrix = algebra_adds_matrix(matrix)
    #print(add_matrix)
    return number_multiply(1/det, transposion(add_matrix))


def algebra_adds_matrix(matrix) -> list:
    matrix = deepcopy(matrix)
    A = list()
    for _ in range(len(matrix)):
        A.append(list())
        for i in range(len(matrix)):
            A[_].append(0)

    for _ in range(len(A) * len(A)):
        M = list()
        i = _ // len(A)
        j = _ % len(A)
        for k in range(len(A) * len(A)):
            if k // len(A) != i and k % len(A) == 0:
                M.append(list())
            if k // len(A) != i and k % len(A) != j:
                M[k // len(A) - (k // len(A) > i)].append(matrix[k//len(A)][k % len(A)])
        A[i][j] = determinant(M)
        if (i + j) % 2 == 1:
            A[i][j] *= -1
    return A


def matrix_multiply(A, B) -> list:
    # Создаём и заполняем нулями новую матрицу для удобства дальнейшего вычисления
    C = list()
    for i in range(len(A)):
        C.append(list())
        for _ in range(len(A)):
            C[i].append(0)

    # Перемножаем матрицы
    # Выделяем единый массив для индексов С
    for _ in range(len(A) * len(A)):

        # Делаем засчёт общего индекса i и j
        i = _ // len(A)
        j = _ % len(A)

        # Итоговое значение в ячейке C[i][j]
        ij = 0

        # Проходимся по столбцам А и строкам В, считаем ij
        for k in range(len(A[0])):
            ij += A[i][k] * B[k][j]
        C[i][j] = ij
    return C


# Перемножаем матрицу на число
def number_multiply(a, A) -> list:
    A = deepcopy(A)
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] *= a
    return A




A = [[2, 5], [6, 3], [5, -2]]

