x = int(raw_input(" enter numbers from 1 to 9 "))
if 1 <= x <= 3:
    s = raw_input( " enter any string ")
    n = int(raw_input(" enter multiply "))
    result = s * n 
    print result
elif 4 <= x <= 6:
    m = int(raw_input(" enter power number "))
    print x ** m
elif 7 <= x <= 9:
    for n in range(10):
        x += 1
        print x
else:
    print 'input error'


    


