#ARRAYS

class friends:
    def __init__(self, valor : int) :
        self.valor = valor 

amigos = []

bingo = [3, 17, 21, 45, 2, 4, 89, 65]

objetos =[friends(10), friends(6)]

tamanho = len(bingo)
print(tamanho) 

compras = ["uva", "pao", "feijao", "omo", "frango"]

cpr = len(compras)
print(cpr)
#8

#adicionar = .append
#remover = pop

bingo.append(87)
bingo.pop()
print(bingo)

#adicionar no início = .insert
#remover do início = .pop(0)

bingo.pop(0)
bingo.insert(1, 3)
print(bingo)

#adicionar em uma posição específica = .insert(indice,numero/string)
#remover de uma posição específica = .pop(indice)

bingo.insert(5,77)
bingo.pop(4)

#utilizando o join = junta elementos de uma lista de STRINGS

cores = ["amarelo", "vermelhor", "azul", "verde"]
print(", ".join(cores))

#criar um array de uma sequencia de numeros = range()

amarelinha = list(range(11))

#criar array com valores aleatórios = random
import random

sorteio = [random.randint(1,50) for _ in range(3)]

#acessar elemento por índice 
#[0] = primeiro
#[-1] = último

#percorrer elementos usando for range

for i in range(len(bingo)):
    print(f"Indice {i} : {bingo[i]}")


#percorrer elemtos usando for direto

for n in bingo:
    print(n)

#procurar um elemento X usando laço

#criar um novo array com elementos filtrados (pares)

pares = [n for n in bingo if n% 2 == 0]

#criar um novo array com elementos transformados (ao quadrado)4

elevado = [n**2 for n in bingo]

#buscar e remover um elemento em específico :
x = 80
if x in bingo:
    bingo.remove(x)

#remover todos os elementos com um valor em específico

y = 17

buscar = [n for n in bingo if n != x]

#organizar a lista em ordem crescente

idades = [7, 87, 20, 4, 35, 12, 13, 24]

idades.sort()
print(idades)

#organizar a lista em ordem decrescente

idades.sort(reverse = True)
print(idades)

# o sort manipula a lista original

#cria uam nova lista ordenada sem modificar a lista original
nova_lista = sorted(bingo)
print(nova_lista)

lista = bingo.sort(reverse = True)
new = sorted(bingo, reverse = True)
print(lista)

#embaralhar os elementos da lista aleatoriamente / modifica a lista original

random.shuffle(idades)

baralho = ["Ás de Ouros", "Rei de Copas", "Rainha de Espadas", "Valete de Paus"]
random.shuffle(baralho)

cartas = baralho

random.shuffle(cartas)

kazu = [7, 1, 17, 13, 21, 25, 30, 4, 10]

posicao = kazu.index(17)
print(posicao)

#se o valor nao existir ele gera um erro de ValueError
#pra isso é necessario usar um if/ else

if 17 in kazu:
    print(kazu.index(17))
else:
    print("Valor não encontrado")

#remover todos os elementos de uma lista/ esvazia

another_kazu =[1, 2, 3 , 4 , 5]
another_kazu.clear()
print(another_kazu)

another_kazu.sort()
print("Ordenada:", another_kazu.sort())


#append - insere um elemento no array (final)
#.pop - remove um elemento do array / abre parenteses para retirar de uma posição em específica
#.index() - referente ao conteudo do elemento
#.clear - removetodos os elementos do arrays
#.join /STRING - adiciona um elemento no array (final)
#random.randint() - cria um novo array de elementos em sequencia
#.sort - organiza os elementos do array em ordem crescente
#.sort(reverse = True) - organiza os elementos em ordem descrescente
#sorted() - cria um novo array com os elementos organizados em forma crescente
#sorted(nomeDoArray, reverse = True) - cria um novo array com os elementos organizados em forma decrescente
#random.shuffle - modifica o array original e organiza os elementos de forma aleatória






