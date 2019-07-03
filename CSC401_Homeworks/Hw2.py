#Homework 2#
#Problem 3.21 part f#
def forloops(start, stop, step):
    for i in range(start, stop, step):
        print(i)

'''
>>> forloops(5,22,4)
5
9
13
17
21
'''
#Problem 3.32#
def pay(wage, hours):
    if hours <= 40:
        return (wage*hours)
    else:
        return (wage*40) + ((hours-40)*(wage*1.5))

''' 
>>> pay(10,40)
400
>>> pay(10,45)
475.0
>>> pay(10,50)
550.0
'''


#Problem 3.36#
def abbreviation(Day):
    return(Day[0:2])

'''
>>> abbreviation('Friday')
'Fr'
>>> abbreviation('Tuesday')
'Tu'
>>> abbreviation('Monday')
'Mo'
'''

#Problem 3.37

import math
def collision(x1, y1, r1, x2, y2, r2):
    distx = x1 - x2
    disty = y1 - y2
    totalr = r1 + r2
    dist = math.sqrt((x2-x1)**2) + math.sqrt((y2-y1)**2)
    return(dist <= totalr)

'''
>>> collision(0,0,3,0,5,3)
True
>>> collision(1,1,4,0,2,2)
True
>>> collision(0,0,3,4,2,3)
True
>>> collision(0,0,3,4,4,1)
False
>>> collision(1,1,1,4,4,2)
False
'''
#Problem 3.38


def partition(l):
    for i in range(0,len(l)):
        if l[i][0].lower() in 'abcdefghijklm':
            print (l[i])
'''            
>>> partition(['Evelyn', 'Eleanor', 'Sammy', 'Owen', 'Gabby'])
Evelyn
Eleanor
Gabby
'''

#Problem 3.42

def ion2e(s):
    if (s[-3:] == 'ion'):
        s = s[:-3] + 'e'
        return(s)
    else:
        return(s)
'''    
>>> ion2e('congratulation')
'congratulate'
>>> ion2e('ionization')
'ionizate'
>>> ion2e('python')
'python'
>>> ion2e('ionic')
'ionic'
'''

    
    
