def particao(A, esquerda, direita):
    # 1. Seleção do pivô. O pivô será o elemento A[esquerda].
    pivo = A[esquerda]
    # Particionamento do arranjo.
    i = esquerda
    j = direita
    while i <= j:
        # Encontra elemento maior que o pivo.
        while A[i] <= pivo:
            i += 1
            if i == direita:
                break

        # Encontra elemento menor que o pivo.
        while pivo <= A[j]:
            j -= 1
            if j == esquerda:
                break

        # Ponteiros i e j se cruzaram.
        if i >= j:
            break

        # Troca elementos encontrados acima de lugar.
        A[i], A[j] = A[j], A[i]

    # Coloca o pivo no lugar certo.
    pivo, A[j] = A[j], pivo

    # j é o índice em que o pivo agora está.
    return j

def quicksort(A):
    if len(A) == 0: return A
    pivot = A[0]
    frente = quicksort([menor for menor in A[1:] if menor <= pivot])
    tras   = quicksort([maior for maior in A[1:] if maior > pivot])
    return frente + [pivot] + tras

inp = input().split()
mid = len(inp)//2
inp = quicksort(inp)
print(inp)