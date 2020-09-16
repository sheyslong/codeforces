cases = int(input())
for i in range(cases):
    string = input().split()
    a = int(string[0])
    b = int(string[1])
    n = int(string[2])
    min_ = a
    max_ = b
    if(a > b):
        min_ = b
        max_ = a
    aux = []
    aux.append(min_)
    aux.append(max_)
    while(aux[-1] <= n):
        aux.append(aux[-1] + aux[-2])
    print(len(aux) - 2)