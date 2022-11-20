import numpy as np

'''Функция которая получает на вход g и L, а на выход возвращает массив g_доп длинной L'''
def g_additional(g, L):
    g_dop = np.zeros(L)

    for i in range(L):
        n_dop = np.random.normal(0, 0.1, g[0].size)
        g.dop[i] = g + n_dop

    return g_dop


'''Функция которая получает на вход f_вост и L, на выход возвращает f_ст'''
def f_stochastic(f, L):

    return sum(f)/L
