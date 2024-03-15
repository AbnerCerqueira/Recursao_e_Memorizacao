# recursao de cauda ocorre quando a ultima operação feita pela função é a chamada recursiva
# consumindo bastante espaço na memória

# contagem regressiva
def cr(n):
    if n == 0: return
    print(n)
    cr(n - 1)

# contagem progressiva
def cp(n):
    if n == 0: return
    cr(n - 1)
    print(n)
    
# vai e volta (primeiro mostra a contagem regressiva e dps progressiva)
def vv(n):
    if n == 0:
        print('base')
        return
    print(n)
    vv(n - 1)
    print(n)

# resto da divisao
def resto(a, b):
    if a < b: return a
    else: return resto(a-b, b)