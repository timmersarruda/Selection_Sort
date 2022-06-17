import random

def selection_sort(vet):
    i = 0
    # Percorre a lista até o penúltimo índice
    while i < len(vet) - 1:
        menorPos = i
        j = i + 1
    # Percorre a lista até o último índice, buscando o menor elemento
        while j < len(vet):
            if vet[j] < vet[menorPos]:
                menorPos = j
            j += 1
        if menorPos != i:
            aux = vet[i]
            vet[i] = vet[menorPos]
            vet[menorPos] = aux
        i += 1



