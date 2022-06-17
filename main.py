import selection
import random

qualquerNumero = random.sample(range(1, 10), 4)

listaOrdenada = [1, 2, 3, 4, 5, 6, 9, 20, 22, 25]

inversa = [120, 111, 100, 98, 97, 92, 85, 82, 81, 77, 75, 73, 70]

repetida = [7, 7, 1, 5, 6, 9, 1, 1, 5, 3, 6, 9]


#vetor = list(range(0,200))
#random.shuffle(vetor)
#vetor = qualquerNumero
#vetor = listaOrdenada
#vetor = inversa
vetor = repetida

print("Lista a ser ordenada: ", vetor)
selection.selection_sort(vetor)
print("Elementos ordenados: ", vetor)


