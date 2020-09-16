name = input()
mapa = {}
cont = len(name)
for i in name:
    if(i not in mapa.keys()):
        mapa[i] = 1
    else:
        cont -= 1
if(cont % 2 == 0):
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')