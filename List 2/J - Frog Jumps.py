n_tc = int(input())

def fin(string, position):
    return position >= len(string)

def isRight(string, position):
    return string[position] == "R"
        
def jump(string):
    d = 1
    jump = -1
    while True:
        if fin(string, jump):
            return d
        if jump == -1:
            jump+=d
        else:
            if isRight(string, jump):
                jump-=d
            else:
                jump+=d
            



for i in range(n_tc):
    string =input()
    print(jump(string))
