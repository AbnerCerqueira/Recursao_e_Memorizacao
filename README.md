# Recursão e Memorização
## Recursão
* É um método que permite obter a solução de um problema a partir de outros problemas menores
* Uma função recursiva deve ter:
* **Base**: O **caso trivial** do problema (o caso mais fácil de todos).
* **Passo**: "Formula" que resolve o **caso geral** do problema. <br>
* **Exemplo**: olhe a função recursiva fatorial que está no arquivo <link>

## Recursão degenerada
Uma forma de recursão que pode tornar a função recursiva ineficiente
### Recursão de cauda
* Ocorre quando a ultima operação feita pela função é a chamada recursiva, fazendo um "empilhamento de funções" consumindo **espaço**. Ex: função da contagem regressiva.<link>
### Recursão redundante
* Quando a decomposição recursiva produz varios subproblemas **repetidos** consome **tempo** o programa fica lento. Ex: função da sequência de fibonacci. <link>

## Soluções
### Otimização
* O espaço desnecessário consumido pela função de causa pode ser eliminado transformando a função **recursiva** em uma função **iterativa**. Ex: função contagem regressiva <link>

### Memorização
* O tempo consumido pela função redundante pode ser eliminado por meio da técnica "Dynamic Programming", onde as soluções de subproblemas vão ser guardados para que não precisarem serem resolvidos novamente. Ex: função sequência de fibonacci <link>
