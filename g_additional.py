import numpy as np

'''Функция которая получает на вход g, sigma и L, а на выход возвращает массив g_доп длинной L'''
def g_additional(g, sigma, L):

    g_dop = [0]*L

    for i in range(L):
        n_dop = np.random.normal(0, sigma, g[0].size)
        print(n_dop, g)
        g_dop[i] = g + n_dop

    return g_dop


'''Функция которая получает на вход f_вост и L, на выход возвращает f_ст'''
def f_stochastic(f, L):

    return np.sum(f)/L



