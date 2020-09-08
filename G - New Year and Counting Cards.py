from collections import Counter

aux = [49, 51, 53, 55, 57, 97, 101, 105, 111, 117]
def recursive(string):
    collect = Counter(string)
    count = 0
    for el in collect:
        num = ord(el)
        if num >= 49 and num <= 117:
            if num in aux:
                count+=collect[el]
    
    return count
   
string = str(input())
print(recursive(string))

