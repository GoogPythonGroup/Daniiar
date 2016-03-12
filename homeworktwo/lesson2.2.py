w = raw_input(' enter any string: ')
e = w.split(';')
maxword = 0
for o in e:
    if len(o) > maxword:
        maxword = len(o)
for o in e:
    if len(o) == maxword:
        print o
