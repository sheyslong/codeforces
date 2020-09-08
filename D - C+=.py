size = int(input())

mult = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 
433494437, 701408733]

def recursive(a, b, n, index):
    res = 0
    if index == 0:
        res = b+a
    else:
        res = b*mult[index]+a*mult[index-1]
    if res > n:
        return index+1
    return recursive(a, b, n, index+1)


for i in range(size):
    list_ = input().split()
    a = int(list_[0])
    b = int(list_[1])
    n = int(list_[2])
    if a > n or b > n:
        print("0")
    else:
        print(recursive(a, b, n, 0))
