
aux = ["a", "e", "i", "o", "u", "1", "3", "5", "7", "9"]
def func(string):
    count = 0
    for el in string:
        if el in aux:
            count+=1
    return count
   
string = str(input())
print(func(string))

