size = int(input())
array = input().split()

index = 0
while index < len(array):
    if array[index] in array[index+1:len(array)]:
        array.pop(index)
    else:
        index+=1

print(len(array))

string=""
for j in range(0, len(array)):
    string+= str(array[j])+" "

print(string)
