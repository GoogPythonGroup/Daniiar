# coding=utf-8
print 'Общество в начале XXI века'
age = int(raw_input( 'Ваш возраст: ' ))
if 0 <= age <= 7:
    print 'Вам в детский сад'
elif 7 <= age <=18:
    print 'Вам в школу'
elif 18 <= age <= 25:
    print 'Вам в профессиональное учебное заведение'
elif 25 <= age <= 60:
    print 'Вам на работу'
elif 60 <= age <= 120:
    print 'ам предоставляется выбор'
else:
    d = 'Ошибка! Это программа для людей! \n'
    print d * 5

