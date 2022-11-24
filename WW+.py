import numpy as np
import random


# Максимальное число для генерации вектора
RANDOM_RANGE = 255


# Создание псевдообратной матрицы
def pseudo_inverse(matrix):
  return np.linalg.pinv(matrix)


# Генерация произвольного вертикального вектора данного ранга
def generate_vector(leng: int):
    g = list()
    for i in range(leng):
        g.append([random.randrange(RANDOM_RANGE)])
    return g


# Проверка условия сходимости (формула 2)
def check_match_condition(W, Wp, g):
    a = np.dot(W, Wp)
    a = np.dot(a, g)
    for _ in range(len(a)):
        if int(a[_]) != g[_][0]:
            return False
    return True


# Создание единичной матрицы данного ранга
def generate_single_matrix(leng: int):
    a = list()
    for i in range(leng):
        a.append([])
        for j in range(leng):
            a[i].append(0)
        a[i][i] = 1
    return a


# Поиск функции (3)
def find_f(W, Wp, g):

    # Если условие совместности не выполняется, он выкидывает пустой массив вместо функции
    if not check_match_condition(W, Wp, g):
        return []

    # Нахождение "левой" части суммы функции
    Wpg = np.dot(Wp, g)

    # Нахождение "правой" части суммы функции
    WpW = np.dot(Wp, W)
    WpW = np.subtract(generate_single_matrix(len(WpW)), WpW)
    z = generate_vector(len(WpW))
    WpW = np.dot(WpW, z)

    # Нахождение самой функции (встроенная функция выдаёт ошибку, так что считаю вручную)
    f = Wpg
    for i in range(len(f)):
        for j in range(len(f[i])):
            f[i][j] += WpW[i][j]
    return f

