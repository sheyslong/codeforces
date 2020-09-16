def isNotPrime(x):
    if x < 4:
        return False
    if x % 2 == 0:
        return True
    for div in range(2, x):
        if x % div == 0:
            return True
    return False

def findM(n, m):
    prime = n * m + 1
    if isNotPrime(prime):
        return m
    return findM(n, m+1)

n = int(input())
print(findM(n, 1))