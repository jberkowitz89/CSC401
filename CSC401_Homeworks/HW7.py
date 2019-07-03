#Homework 7#

#5.41

def poly(lstCoeffs,x):
    lenCoeffs = len(lstCoeffs) - 1
    countCoeffs = 0
    final = lstCoeffs[countCoeffs]
    while countCoeffs < lenCoeffs:
        countCoeffs += 1
        final += lstCoeffs[countCoeffs]*(x**countCoeffs)
    return final
'''
>>> poly([1,2,1],2)
9
>>> poly([1,0,1,0,1],3)
91
>>> poly([1,2,2,3],3)
106
>>> poly([1,0,1,0,1],2)
21
'''

#10.14

def combinations(n,k):
    if k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return combinations (n-1,k-1) + combinations(n-1,k)
'''
>>> combinations(2,1)
2
>>> combinations(1,2)
0
>>> combinations(5,2)
10
>>> combinations(12,2)
66
>>> combinations(2,5)
0
>>> combinations(10,3)
120
>>> combinations(10,5)
252
>>> combinations(8,4)
70
'''

#10.18

def num0nes(n):
    countOnes = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return num0nes(n//2) + num0nes(n%2)

'''
>>> num0nes(0)
0
>>> num0nes(1)
1
>>> num0nes(14)
3
>>> num0nes(15)
4
>>> num0nes(543)
6
>>> num0nes(5321)
6
>>> num0nes(1042318)
14
'''

#10.28
def pascalLine(n):
    if n == 0:
        return [1]
    elif n == 1:
       pascalStart = [1]
       pascalStart.append(1)
       return pascalStart
    else:
        pascalStart = [1]
        prev = pascalLine(n-1)
        for i in range(len(prev)-1):
            pascalStart.append(prev[i] + prev[i+1])
        pascalStart.append(1)
        return pascalStart
'''
>>> pascalLine(2)
[1, 2, 1]
>>> pascalLine(3)
[1, 3, 3, 1]
>>> pascalLine(4)
[1, 4, 6, 4, 1]
>>> pascalLine(7)
[1, 7, 21, 35, 35, 21, 7, 1]
>>> pascalLine(5)
[1, 5, 10, 10, 5, 1]
>>> pascalLine(6)
[1, 6, 15, 20, 15, 6, 1]
'''

#10.31 a
from turtle import Screen, Turtle
def levy(n):
    if n == 0:
        return 'F'
    else:
        step = levy(n-1)
        return 'L' + step + 'R' + step + 'L'
'''
>>> levy(4)
'LLLLFRFLRLFRFLLRLLFRFLRLFRFLLLRLLLFRFLRLFRFLLRLLFRFLRLFRFLLLL'
>>> levy(0)
'F'
>>> levy(1)
'LFRFL'
>>> levy(3)
'LLLFRFLRLFRFLLRLLFRFLRLFRFLLL'
>>> levy(5)
'LLLLLFRFLRLFRFLLRLLFRFLRLFRFLLLRLLLFRFLRLFRFLLRLLFRFLRLFRFLLLLRLLLLFRFLRLFRFLLRLLFRFLRLFRFLLLRLLLFRFLRLFRFLLRLLFRFLRLFRFLLLLL'
'''
           

def drawLevy(directions, length, angle, x, y):
    s= Screen()
    t = Turtle()
    t.up()
    t.setpos(x,y)
    t.down()
    for move in directions:
        if move == 'F':
            t.forward(length)
        elif move == 'L':
            t.lt(angle)
        elif move == 'R':
            t.rt(angle*2)
        else:
            print('bad move')
    s.exitonclick()
 
            
    
    

   
    
    
    
    
        

        
        
    
