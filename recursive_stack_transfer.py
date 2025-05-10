
def trans(s, t):
    while s:
        t.append(s.pop())

s = [1, 2, 3]
t = []
trans(s, t)
print(t)
