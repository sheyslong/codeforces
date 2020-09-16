from collections import Counter

def password(p, h):
    size_h = len(h)
    size_p = len(p)
    passwd = Counter(p)

    if size_h == size_p:
        verify = Counter(h)
        if verify == passwd:
            return "YES"
        return "NO"

    init = (size_h - size_p)//2
    for i in range(init, size_h):
        if (i + size_p) > size_h:
            return "NO"
        else:
            verify = Counter(h[i:i+size_p])
            if verify == passwd:
                return "YES"

    return "NO"

t = int(input())
for i in range(t):
    p = str(input())
    h = str(input())
    print(password(p, h))