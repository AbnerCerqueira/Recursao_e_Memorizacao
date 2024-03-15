#otimizada
# contagem regressiva
def cr(n):
    if n == 0: return
    print(n)
    cr(n - 1)
# contagem regressiva otimizada
# colocar um while True de primeira pq sempre vamos usalo para otimizar
# a base sempre é a mesma, precisamos pensar no passo
def crOtimizada(n):
    while True:
        if n == 0: return
        print(n)
        n -= 1

# resto da divisao
def resto(a, b):
    if a < b: return a
    else: return resto(a-b, b)
# resto da divisao otimizado
def resto(a, b):
    while True:
        if a < b: return a
        else: a -= b