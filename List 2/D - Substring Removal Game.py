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

def countAlice(array):
    count=0
    isAlice = True
    for i in range(len(array)):
        max_ = max(array)
        if isAlice:
            count+=max_
        isAlice=not(isAlice)
        array.remove(max_)
    return count

for i in range(n_tc):
    string = input()
    aux = countOne(string)
    print(countAlice(aux))
