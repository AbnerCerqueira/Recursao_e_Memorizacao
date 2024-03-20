# recursao redundante ocorre quando a decomposição recursiva do problema produz varios subproblemas repetidamente
# fatorial
def fat(n):
    if n == 0: return 1
    else: return n * fat(n- 1)

# potencia
def pot(base, expoente):
    if expoente == 0: return 1
    else: return base * pot(base, expoente - 1)
    
# termial
def term(n):
    if n == 0: return 0
    else: return n + term(n - 1) 

# sequencia de fibonacci
def fibo(n):
    if n < 3: return 1
    else: return fibo(n - 1) + fibo(n - 2)

# triangulo de pascal
def pascal(i, j):
    if i <= j: return 1
    if i == 1 or j == 1: return 1
    else: return pascal(i - 1, j) + pascal(i - 1, j - 1)