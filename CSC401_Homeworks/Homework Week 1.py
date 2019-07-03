Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Homework Week 1#
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
>>> (s2 + (s1*2))**2
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    (s2 + (s1*2))**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
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
>>> s[1] == 'g'
False
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
>>> s[-1] == 'x'
False
>>> #e#
>>> len(s)/2
3.5
>>> s[3] = 'd'
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s[3] = 'd'
TypeError: 'str' object does not support item assignment
>>> s
'goodbye'
>>> s[3] == 'd'
True
>>> #d#
>>> s[-2] == 'x'
False
>>> #f#
>>> s[0] == s[-1]
False
>>> #g#
>>> s[-4]
'd'
>>> s[-4:]
'dbye'
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
>>> middle = 'Fitzgerald
SyntaxError: EOL while scanning string literal
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
>>> 
>>> #c#
>>> thorny = flowers[:3]
>>> thorny
['rose', 'bougainvillea', 'yucca']
>>> poisonous = flowers[-1]
>>> poisonous
'lilly of the valley'
>>> #d
>>> poisonous = flowers[-1]
>>> poisonous
'lilly of the valley'
>>> dangerous = thorny + poisonous
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    dangerous = thorny + poisonous
TypeError: can only concatenate list (not "str") to list
>>> dangerous = [thorny + poisonous]
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    dangerous = [thorny + poisonous]
TypeError: can only concatenate list (not "str") to list
>>> thorny
['rose', 'bougainvillea', 'yucca']
>>> poisonous
'lilly of the valley'
>>> lst(thorny) + lst(dangerous)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    lst(thorny) + lst(dangerous)
NameError: name 'lst' is not defined
>>> thorny + dangerous
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    thorny + dangerous
NameError: name 'dangerous' is not defined
>>> lst(thorny) + lst(poisonous)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    lst(thorny) + lst(poisonous)
NameError: name 'lst' is not defined
>>> thorny + poisonous
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    thorny + poisonous
TypeError: can only concatenate list (not "str") to list
>>> [thorny + poisonous]
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    [thorny + poisonous]
TypeError: can only concatenate list (not "str") to list
>>> dangerous = thorny + poisonous
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    dangerous = thorny + poisonous
TypeError: can only concatenate list (not "str") to list
>>> poisonous = flowers[-1:]
>>> poisonous
['lilly of the valley']
>>> dangerous = thorny + poisonous
>>> dangerous
['rose', 'bougainvillea', 'yucca', 'lilly of the valley']
>>> #problem 2.19#


