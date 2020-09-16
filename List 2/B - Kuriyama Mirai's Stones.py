def order(array):
    return sorted(array, key=int)

def summ(array):
    array[0] = int(array[0])
    for i in range(1, len(array)):
        array[i]=int(array[i])+array[i-1]
    
def questionRes(l, r, array):
    if l == 0:
        return array[r]
    return array[r]-array[l-1]

size = int(input())
costs_stones = input().split()
n_questions = int(input())
costs_stones_ord = order(costs_stones.copy())

summ(costs_stones)
summ(costs_stones_ord)

for i in range(n_questions):
    input_ = input().split()
    question = int(input_[0])
    l = int(input_[1])-1
    r = int(input_[2])-1
    if question == 1:
        print(questionRes(l, r, costs_stones))
    else:
        print(questionRes(l, r, costs_stones_ord))
         
         