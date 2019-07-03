#Homework 4#

#Problem 5.15
def vowels(s):
    '''Must go through each character in the statement, assign each
    character of the string an index, and if the character in that index is
    a vowel, print index that corresponds to the vowel'''
    for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
            print(i)
'''
>>> vowels('Hello WORLD')
1
4
7
>>> vowels('Take ME out to the ballgame')
1
3
6
8
9
13
17
20
24
26
'''

#Problem 5.16

def indexes(word, letter):
    '''Must take input word & letter, go through all characters in word
    and find the index at which letter appears, and return a list
    of the indexes'''
    indexlist = []
    for i in range(len(word)):
        if letter in word[i]:
            indexlist.append(i)

    return indexlist

'''
>>> indexes('Mississippi', 's')
[2, 3, 5, 6]
>>> indexes('Mississippi', 'i')
[1, 4, 7, 10]
>>> indexes('Deerfield', 'e')
[1, 2, 6]
'''

#Problem 5.18

def four_letter(lst):
    newlist = []
    for i in range(len(lst)):
        if len(lst[i]) == 4:
            newlist.append(lst[i])
    return newlist

'''
>>> four_letter(['read', 'write', 'play', 'run', 'jump', 'catch', 'field', 'yeah'])
['read', 'play', 'jump', 'yeah']
>>> four_letter(['dog', 'letter', 'stop', 'door', 'bus', 'dust'])
['stop', 'door', 'dust']
'''

#Problem 5.26

def rps(P1, P2):
    if P1 == P2:
        return 0
    elif P1 == 'R' and P2 == 'P':
        return 1
    elif P1 == 'R' and P2 == 'S':
        return -1
    elif P1 == 'S' and P2 == 'P':
        return -1
    elif P1 == 'S' and P2 == 'R':
        return 1
    elif P1 == 'P' and P2 == 'R':
        return -1
    elif P1 == 'P' and P2 == 'S':
        return 1

'''
>>> rps('R', 'P')
1
>>> rps('S', 'R')
1
>>> rps('R', 'S')
-1
>>> rps('R', 'R')
0
>>> rps('P', 'R')
-1
>>> rps('S', 'P')
-1
'''

#Problem 5.35

def pixels(l):
    poscount = 0
    for row in l:
        for item in row:
            #print(item)
            if item > 0:
                poscount += 1
    return poscount

'''
>>> l = [[0, 156, 0, 0], [34,0, 0, 0], [23, 123, 0, 34]]
>>> pixels(l)
5
>>> l = [[123, 56, 255], [34, 0, 0], [23, 123, 0], [3, 0, 0]]
>>> pixels(l)
7
>>> l = [[0, 0, 0], [0, 0, 0]]
>>> pixels(l)
0
>>> l = [[400, 2, 0, 0], [231, 189, 0, 1], [1, 0, 0, 0], [12, 15, 18]]
>>> pixels(l)
9
'''

#Problem 5.39

def exclamation(word):
    vowels='aeiouAEIOU'
    for c in vowels:
        word=word.replace(c,c*4)
    return word + '!'
'''
>>> exclamation('hello')
'heeeelloooo!'
>>> exclamation('argh')
'aaaargh!'
>>> exclamation('Alvin')
'AAAAlviiiin!'
'''
        
'''takes the string, sees if there are any vowels, and if there are vowels,
    replaces the vowel with four consecutive copies of itself and an exclamation
    mark is added at the end'''
         
    
