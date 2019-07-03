#Joey Berkowitz Week 1 Homework#
>>> #Problem 2.12#
>>> #a#
>>> 1 + 2 + 3 + 4 + 5 + 6 + 7
28
>>> #b#
>>> (65 + 57 + 45) / 3
55.666666666666664
>>> #c#
>>> 2 ** 20
1048576
>>> #d#
>>> 4356 // 61
71
>>> #e#
>>> 4356 % 61
25
>>> #Problem 2.13#
>>> s1 = '-'
>>> s2 = '+'
>>> #a#
>>> s1 + s2
'-+'
>>> #c#
>>> s2 + (s1*2)
'+--'
>>> #d#
>>> (s2 + (s1*2))*2
'+--+--'
>>> #e#
>>> (s2 + (s1*2))*10
'+--+--+--+--+--+--+--+--+--+--'
>>> #f#
>>> (s2 + s1 + (s2*3)+ (s1*2))*5
'+-+++--+-+++--+-+++--+-+++--+-+++--'
>>> #Problem 2.15#
>>> s = 'goodbye'
>>> #a#
>>> s[0] == 'g'
True
>>> #b#
>>> s[6] == 'g'
False
>>> #c#
>>> s[0] == 'g' and s[1] == 'a'
False
>>> #d#
>>> s[-2] == 'x'
False
>>> #e#
>>> s[3] == 'd'
True
>>> #f#
>>> s[0] == s[-1]
False
>>> #g#
>>> s[-4:] == 'tion'
False
>>> #Problem 2.16#
>>> #a#
>>> a = 6
>>> b = 7
>>> #b#
>>> c = (6+7) / 2
>>> c
6.5
>>> #c#
>>> inventory = ['paper', 'staples', 'pencils']
>>> #d#
>>> first = 'John'
>>> middle = 'Fitzgerald'
>>> last = 'Kennedy'
>>> #e#
>>> fullname = first + ' ' + middle + ' ' + last
>>> fullname
'John Fitzgerald Kennedy'
>>> #Problem 2.18#
>>> #a#
>>> flowers = ['rose', 'bougainvillea', 'yucca', 'marigold', 'daylilly', 'lilly of the valley']
>>> #b#
>>> 'potato' in flowers
False
>>> #c#
>>> thorny = flowers[:3]
>>> thorny
['rose', 'bougainvillea', 'yucca']
>>> #d#
>>> poisonous = flowers[-1:]
>>> poisonous
['lilly of the valley']
>>> #e#
>>> dangerous = thorny + poisonous
>>> dangerous
['rose', 'bougainvillea', 'yucca', 'lilly of the valley']
>>> #problem 2.19#
>>> a = 0
>>> b = 0
>>> r = 10
>>> #a#
>>> x= 0
>>> y = 0
>>> (x-a)**2 + (y - b)**2 < r**2
True
>>> #b#
>>> x=10
>>> y=10
>>> (x-a)**2 + (y - b)**2 < r**2
False
>>> #c#
>>> x=6
>>> y=6
>>> (x-a)**2 + (y - b)**2 < r**2
True
>>> #d#
>>> x=7
>>> y=8
>>> (x-a)**2 + (y - b)**2 < r**2
False
>>> #problem 2.21#
>>> s = 'paz'
>>> s1 = s[::-1]
>>> s1
'zap'
