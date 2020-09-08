def repeat(index, s, aux):
    if index < len(s):
        if index == len(s)-1:
            if not s[index] in aux:  
                aux.append(s[index])
        else:
            if s[index] == s[index+1]:
                repeat(index+2, s, aux)
            else:
                if not s[index] in aux:
                    aux.append(s[index])
                repeat(index+1, s, aux)



def order(s):
    sort = sorted(s)
    join = ""
    for el in sort:
        join+= el

    return join
n = int(input())

for i in range(n):
    s = str(input())
    aux = []
    repeat(0, s, aux)
    join = order(aux)
    print(join)