def boyOrGirl(count):
    if count % 2 == 0:
        return "CHAT WITH HER!"
    return "IGNORE HIM!"

def collec(s):
    aux = [0]*26
    for el in s:
        aux[ord(el)-97]=1

    count = 0
    for num in aux:
        count+=num
    
    return boyOrGirl(count)
s = str(input())
print(collec(s))
