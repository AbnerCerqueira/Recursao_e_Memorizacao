# sequencia de fibonacci
def fibo(n):
    if n < 3: return 1
    else: return fibo(n - 1) + fibo(n - 2)

# sequencia de fibonacci memorizado
def fiboMem(n, dicionario={}):
    if n < 3: return 1
    if n not in dicionario:
        dicionario[n] = fiboMem(n - 1) + fiboMem(n - 2)
    return dicionario[n]

#-------------------------------------------------------------------------------------------------

# triangulo de pascal
def pascal(i, j):
    if j == 1 or i == j: return 1
    else: return pascal(i - 1, j) + pascal(i - 1, j - 1)

# triangulo de pascal memorizado
def pascalMem(i, j, dicionario={}):
    if j == 1 or i == j: return 1
    if (i, j) not in dicionario: # quando temos duas entradas, usamos uma tupla
        dicionario[(i, j)] = pascalMem(i -1 , j) + pascalMem(i - 1, j - 1)
    return dicionario[(i, j)]