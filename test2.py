print 'Nation in XX century'
age = int(raw_input( 'Your age: ' ))
if 0 <= age <= 7:
    print 'go to kinder garden'
elif 7 <= age <=18:
    print 'go to school'
elif 18 <= age <= 25:
    print 'go to PTU'
elif 25 <= age <= 60:
    print 'go to work'
elif 60 <= age <= 120:
    print 'choose your destiny'
else:
    d = 'ERROR, THIS PROGRAMM FOR HUMANBEING \n'
    print d * 5

