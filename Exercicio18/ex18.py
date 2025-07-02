lista= [1,2,3,4]
print(lista)
#mostra os elementos da lista

lista.append(5)
print(lista)
# adiciona o elemento 5 no final da lista

lista.insert(0,9)
print(lista)
# adiciona o elemento 9 na posicao 0 da lista

lista.remove(2)
print(lista)
# remove o elemento 2 da lista

lista.sort()
print(lista)
# ordena a lista em ordem crescente

lista.reverse()
print(lista)
# inverte a ordem dos elementos da lista

print(lista.count(3))
# conta quantas vezes o elemento 3 aparece na lista

print(lista.pop())
# remove o ultimo elemento da lista e informa o elemento removido

print(lista)
# mostra a lista apos a remoção do ultimo elemento

del lista[2]
print(lista)
# remove o elemento na posicao 2 da lista

del lista[0:2]
print(lista)
# remove os elementos da posicao 0 ate a posicao 2 

lista.clear()
print(lista)
# remove todos os elementos da lista
