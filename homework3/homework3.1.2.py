x = int(raw_input(" enter numbers from 1 to 9 "))

def do_multiply(a, b):
    return a * b

def do_power(x, y):
    return x ** y

def do_range(x):
    return [x for x in range(x, x + 10, 1)]
if 1 <= x <= 3:
    s = raw_input( " enter any string ")
    n = int(raw_input(" enter multiply "))
    res = do_multiply(s, n)
    print res
elif 4 <= x <= 6:
    m = int(raw_input(" enter power number "))
    result = do_power(x, m)
    print result
elif 7 <= x <= 9:
    res = do_range(x)
    print res    
else:
    print 'input error'


    


