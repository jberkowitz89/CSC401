#### Homework 5 ####

#5.25
def leap(year): #finds out if year is leap year
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
'''
>>> leap(2008)
True
>>> leap(1900)
False
>>> leap(2000)
True
>>> leap(1600)
True
>>> leap(2012)
True
>>> leap(1800)
False
'''

#5.28
def geometric(lst):
    ratio = lst[1]/lst[0]
    for i in range(1,len(lst)):
        if lst[i]/lst[i-1] == ratio:
            pass
        else:
            return False
    return True
'''
>>> geometric([2,4,8,16,32,64,128,256])
True
>>> geometric([2,4,6,8])
False
'''

    


#5.36***

def prime(n):
    for i in range(3,n):
        if n % i == 0:
            return False
    return True

'''
>>> prime(2)
True
>>> prime(17)
True
>>> prime(21)
False
>>> prime(24)
False
>>> prime(11)
True            
'''

#5.38
def collatz(x):
    print(x)
    while x != 1:
        if x % 2 == 0:
            x = x//2
            print(x)
        elif x % 2 != 0:
            x = 3*x + 1
            print(x)
'''>>> collatz(10)
10
5
16
8
4
2
1
>>> collatz(16)
16
8
4
2
1
'''

#5.42**
def primeFac(n):
    lstPrimes = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            lstPrimes.append(d)
            n /= d
        d += 1
    if n > 1:
        lstPrimes.append(n)
    return lstPrimes
'''
>>> primeFac(72)
[2, 2, 2, 3, 3]
>>> primeFac(20)
[2, 2, 5.0]
>>> primeFac(113)
[113]
>>> primeFac(112)
[2, 2, 2, 2, 7.0]
'''

#5.48**
def sublist(lst1, lst2):
    i1 = 0
    i2 = 0

    while i1 < len(lst1) and i2 < len(lst2):
        if lst1[i1] == lst2[i2]:
            i1 += 1
            i2 += 1
        elif lst1[i1] != lst2[i2]:
            i2 += 1
    if i1 == len(lst1):
        return True
    else:
        return False
  
'''
>>> sublist([1,2,3], [1,99,2,99,99,3])
True
>>> sublist([1,2,3], [1,99,3,99,99,2])
False
>>> sublist([1,3,5,7], [1, 23, 33, 2, 3, 44, 38, 33, 5, 12, 19, 14, 7, 32])
True
>>> sublist([1,1,19,2], [12,1,23,1,22,421,19,23,2])
True
>>> sublist([1,1,19,2], [2,1,1,22,2,19])
False
'''


import random
def coin():
    lst = [0,1]
    val = random.choice(lst)
    print(val)
    if val == 0:
        return 'Heads'
    return 'Tails'

def combinations(n,k):
    if k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return combinations(n-1,k-1)+combinations(n-1,k)

