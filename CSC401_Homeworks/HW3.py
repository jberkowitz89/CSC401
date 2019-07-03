#Homework 3#
#Problem 4.17
#a
message = 'The secret of this message is that it is secret.'
#b
length = len(message)
#c
count = message.count('secret')
#d
secret = message.replace('secret', 'xxxxxx')
'''
>>> message
'The secret of this message is that it is secret.'
>>> length
48
>>> count
2
>>> secret
'The xxxxxx of this message is that it is xxxxxx.'
>>> 
'''

#Problem 4.18
s = '''It was the best of times, it was the worst of times; it
was the age of wisdom, it was the age of foolishness; it was the
epoch of belief, it was the epoch of incredulity; it was...'''
#a
s1 = s.replace('.',' ')
s2 = s1.replace(',',' ')
s3 = s2.replace(';',' ')
newS = s3.replace('\n',' ')
'''
>>> s1
'It was the best of times, it was the worst of times;
it\nwas the age of wisdom, it was the age of
foolishness; it was the\nepoch of belief, it
was the epoch of incredulity; it was   '
>>> s2
'It was the best of times  it was
the worst of times; it\nwas the age of wisdom
it was the age of foolishness; it was the\nepoch
of belief  it was the epoch of incredulity; it was   '
>>> ================================ RESTART ================================
>>> 
>>> s3
'It was the best of times  it was the
worst of times  it\nwas the age of wisdom
it was the age of foolishness  it was the\nepoch
of belief  it was the epoch of incredulity  it was   '
>>> ================================ RESTART ================================
>>> 
>>> newS
'It was the best of times  it was the worst of
times  it was the age of wisdom  it was the age of
foolishness  it was the epoch of belief  it was the
epoch of incredulity  it was   '
'''
#b
newS = newS.strip(' ')
'''
>>> newS
'It was the best of times  it was the worst of times
it was the age of wisdom  it was the age of foolishness
it was the epoch of belief  it was the epoch of incredulity  it was'
'''
#c
newS = newS.lower()
'''
>>> newS
'it was the best of times  it was the worst of times
it was the age of wisdom  it was the age of foolishness
it was the epoch of belief  it was the epoch of incredulity  it was'
'''
#d
newS.count('it was')
7
#e
newS = newS.replace('was','is')
'''
'it is the best of times  it is the worst of times
it is the age of wisdom  it is the age of foolishness
it is the epoch of belief  it is the epoch of incredulity  it is'
'''
#f
listS = newS.split()
'''
>>> listS
['it', 'is', 'the', 'best', 'of', 'times',
'it', 'is', 'the', 'worst', 'of', 'times',
'it', 'is', 'the', 'age', 'of', 'wisdom',
'it', 'is', 'the', 'age', 'of', 'foolishness',
'it', 'is', 'the', 'epoch', 'of', 'belief', 'it',
'is', 'the', 'epoch', 'of', 'incredulity', 'it', 'is']
'''

#Problem 4.19
first = 'Marlena'
last = 'Sigel'
middle = 'Mae'

#a
'''print('{}, {} {}'.format(last, first, middle))'''
'''
>>> ================================ RESTART ================================
>>> 
Sigel, Marlena Mae
'''
#b
'''print('{}, {} {}.'.format(last, first, middle[0]))'''
'''
>>> ================================ RESTART ================================
>>> 
Sigel, Marlena M.
>>> 
'''
#c
'''print('{} {}. {}'.format(first, middle[0], last))'''
'''
>>> ================================ RESTART ================================
>>> 
Marlena M. Sigel
>>> 
'''
#d
'''print('{}. {}. {}'.format(first[0], middle[0], last))'''
'''
>>> ================================ RESTART ================================
>>> 
M. M. Sigel
>>> 
'''

#Problem 4.20

sender = 'tim@abc.com'
recipient = 'tom@xyz.org'
subject = 'Hello!'

'''print('From: {}\nTo: {}\nSubject: {}'.format(sender, recipient, subject))'''

'''
===========
>>> 
From: tim@abc.com
To: tom@xyz.org
Subject: Hello!
>>> 
'''

#Problem 4.24

def cheer(TeamName):
    print('How do you spell winner?\nI know, I know!')
    for char in TeamName:
        print(char.upper(), end=' ')
    print('!\nAnd that\'s how you spell winner!\nGo',TeamName+'!')
'''
>>> cheer('Huskies')
How do you spell winner?
I know, I know!
H U S K I E S !
And that's how you spell winner!
Go Huskies!
>>> cheer('Bears')
How do you spell winner?
I know, I know!
B E A R S !
And that's how you spell winner!
Go Bears!
'''

#Problem 4.25

def vowelCount(message):
    print('a, e, i, o and u appear, respectively, {}, {}, {}, {}, {} times.'.format(message.count('a'), message.count('e'), message.count('i'), message.count('o'), message.count('u')))
'''
>>> vowelCount('Le Tour de France')
a, e, i, o and u appear, respectively, 1, 3, 0, 1, 1 times.
>>> vowelCount('The rain in Spain falls on the plain')
a, e, i, o and u appear, respectively, 4, 2, 4, 1, 0 times.
>>> 
'''

#Problem 4.26

def crypto(filename):
    infile = open(filename, 'r')
    original = infile.read()
    new = original.replace('secret', 'xxxxxx')
    print(new)

    infile.close()

'''
>>> crypto('crypto.txt')
I will tell you my xxxxxx. But first, I have to explainwhy it is a xxxxxx.And that is all I will tell you about my xxxxxx.

>>> ================================ RESTART ================================
>>> 
>>> crypto('crypto.txt')
I will tell you my xxxxxx. But first, I have to explain
why it is a xxxxxx.

And that is all I will tell you about my xxxxxx.
'''

#Problem 4.28

def links(filename):
    infile = open(filename, 'r')
    reading = infile.read()
    return reading.count('</a>')

    infile.close()

'''    
>>> links('twolinks.html')
2
'''

#Problem 4.31

def duplicate(filename):
    infile = open(filename, 'r')
    readfile = infile.read()
    trans = readfile.maketrans('.',' ')
    newfile = readfile.translate(trans)
    lst = newfile.split()
    for word in lst:
        if lst.count(word) > 1:
            return True
    return False

'''
>>> duplicate('Duplicates.txt')
True
>>> duplicate('noDuplicates.txt')
False
'''
    
     
