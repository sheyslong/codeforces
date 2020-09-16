el = int(input())
def element(x):
    for a in range(2, x+1):
        for b in range(a, 0, -1): 
            if a % b == 0 and a*b > x and a/b < x:
                return str(a) + " " + str(b)
    return "-1"

print(element(el))
