def minn(cities):
    min_ = int(cities[0])
    if min_ < 0:
        for i in range(len(cities)):
            cities[i]=int(cities[i])+(min_*-1)

n = int(input())
cities = input().split()
minn(cities)
for i in range(len(cities)):
    if i == 0:
        min_ = int(cities[i+1])-int(cities[i])
    else:
        if i == len(cities)-1:
            min_ = int(cities[i])-int(cities[i-1])
        else:
            min_=min(int(cities[i])-int(cities[i-1]), int(cities[i+1])-int(cities[i])) 
    
    max_= max(int(cities[len(cities)-1])-int(cities[i]), int(cities[i])-int(cities[0]))
    print(str(min_) + " " + str(max_))

