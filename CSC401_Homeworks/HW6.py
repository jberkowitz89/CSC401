#Homework 6

#5.49
def heron(n, error):
    prev = 1.0
    new = 0.5*(prev + (n/prev))

    while abs(new-prev) > error:
        prev, new = new, 0.5*(new + (n/new))

    return new

'''
>>> heron(4.0, 0.5)
2.05
>>> heron(4.0, 0.1)
2.000609756097561
>>> heron(5.0, 0.2)
2.238095238095238
'''

#6.22
def mirror(s):
    '''create the dictionary with the mirrors for each of letters of the
    alphabet that has a mirror. Then check each character in string s to
    see if they all have a mirror. If one of the characters doesn't have a
    mirror, then return INVALID. If they all do, return the mirror image
    based on the dictionary.'''

    mirdict = {'b': 'd', 'd': 'b', 'o': 'o', 'p': 'q',
           'q': 'p', 'v': 'v', 'w': 'w', 'x': 'x'}
    newS = ''
    for char in s:
        if char in mirdict:
            newS += mirdict[char]
        else:
            return 'INVALID'
    return newS[::-1]
'''
>>> mirror('vow')
'wov'
>>> mirror('bed')
'INVALID'
>>> mirror('dob')
'dob'
>>> mirror('bod')
'bod'
>>> mirror('dox')
'xob'
'''

#6.30
import random
def rps(p1,p2):
    #tie
    if (p1==p2):
        return 0
    # player 1 wins    
    elif p1+p2 in ['PR','RS','SP']:
        return -1
    else:
        return 1
    # player 2 wins

def simul(n):
    score = 0
    rpsLst = ['R', 'P', 'S']
    for i in range(n):
        p1 = random.choice(rpsLst)
        p2 = random.choice(rpsLst)
        result = rps(p1,p2)
        score += result
    if score < 0:
        print('Player 1')
    elif score == 0:
        print('Tie')
    else:
        print('Player 2')

'''
>>> simul(12)
Player 2
>>> simul(35)
Player 2
>>> simul(23)
Player 2
>>> simul(14)
Player 1
>>> simul(108)
Player 1
>>> simul(2)
Tie
'''

#6.31
#a
import random
def craps():
    total = random.randrange(1,7) + random.randrange(1,7)
    if total in (7,11):
        return 1
    elif total in (2,3,12):
        return 0
    newRoll = random.randrange(1,7) + random.randrange(1,7)
    while newRoll not in (7, total):
        newRoll = random.randrange(1,7) + random.randrange(1,7)
    if newRoll == total:
        return 1
    else:
        return 0
'''
>>> craps()
0
>>> craps()
0
>>> craps()
0
>>> craps()
0
>>> craps()
0
>>> craps()
1
>>> craps()
1
>>> craps()
1
>>> craps()
1
>>> craps()
0
>>> craps()
1
'''
#b
import random
def testCraps(n):
    countW = 0
    for i in range(n):
        if craps() == 1:
            countW+=1
        else:
            pass
    return countW/n
'''
>>> testCraps(10000)
0.4908
>>> testCraps(10000)
0.4944
>>> testCraps(10000)
0.4991
>>> testCraps(1000)
0.502
>>> testCraps(10000)
0.4997
>>> testCraps(1000)
0.491
>>> testCraps(100)
0.52
>>> testCraps(100)
0.45
>>> testCraps(100)
0.5
>>> testCraps(100000)
0.49487
'''

# 6.34
import random
def game(n):
    total = 1
    count = 0
    while total <= n:
        x = random.randrange(0,10)
        y = random.randrange(0,10)
        numbers = x + y
        print(x, '+', y, '=')
        guess = eval(input('Enter answer: '))
        if guess == numbers:
            count += 1
            total += 1
            print('Correct.')
        else:
            print('Incorrect.')
            total += 1
    print('You got', count, 'correct answers out of', n)

'''
>>> game(2)
5 + 8 =
Enter answer: 13
Correct.
5 + 6 =
Enter answer: 10
Incorrect.
You got 1 correct answers out of 2
>>> game(4)
4 + 3 =
Enter answer: 7
Correct.
8 + 1 =
Enter answer: 9
Correct.
4 + 0 =
Enter answer: 4
Correct.
9 + 7 =
Enter answer: 16
Correct.
You got 4 correct answers out of 4
'''
    

    
    
