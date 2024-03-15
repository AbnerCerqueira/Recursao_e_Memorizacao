# sequencia de fibonacci
def fibo(n):
    if n < 3: return 1
    else: return fibo(n - 1) + fibo(n - 2)

# sequencia de fibonacci usando memorização
def fiboMem(n, dicionario={}):
    if n < 3: return 1
    if n not in dicionario:
        dicionario[n] = fiboMem(n - 1) + fiboMem(n - 2)
    return dicionario[n]