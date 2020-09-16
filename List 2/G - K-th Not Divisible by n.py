n_tc = int(input())

def notDivible(n, k):
    if k <= 1:
        return 1
        
    index = k//(n-1) 

    res = (n*index)-index
    if k%(n-1) == 0:
        return (n*index)+(k-res)-1
    else:
        return (n*index)+(k-res)


for i in range(n_tc):
    test_case = input().split()
    n = int(test_case[0])
    k = int(test_case[1])
    print(notDivible(n, k))
