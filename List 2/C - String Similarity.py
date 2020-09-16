num_tc = int(input())
def string(array, size):
    string_ = ""
    for i in range(0, len(array), 2):
        string_+=str(array[i])
    return string_

for i in range(num_tc):
    size = int(input())
    strin = input()
    print(string(strin, size))
    
