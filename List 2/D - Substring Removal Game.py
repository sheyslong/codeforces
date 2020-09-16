n_tc = int(input())

def countOne(array):
    aux = []
    count = 0
    for el in array:
        if int(el) == 1:
            count+=1
        if int(el) == 0 and count>0:
            aux.append(count)
            count=0
    if count>0:
        aux.append(count)
    return aux

def countAnna(array):
    count=0
    for i in range(0, len(array), 2):
        count+=array[i]
    return count
    
for i in range(n_tc):
    string = input()
    aux = countOne(string)
    print(countAnna(aux))
