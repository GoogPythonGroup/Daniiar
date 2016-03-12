j = raw_input('enter any word ')
s = j.split()
g = []
for b in s:
    g.append(len(b))
min = min(g)
for b in s:
    if min == len(b):
        print b
