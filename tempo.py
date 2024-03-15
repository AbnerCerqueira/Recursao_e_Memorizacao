# função para calcular o tempo de alguma outra função e seus argumentos
from time import time
def tempo(f, *a):
    i = time()
    f(*a)
    return time() - i
# exemplo