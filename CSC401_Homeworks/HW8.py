### Homework 8 ###

# 5.42

def primeFac(n):
    for i in range(2,n):
        if n%i == 0:
            return [i] + primeFac(n//i)
            
    return [n]
'''
>>> primeFac(9)
[3, 3]
>>> primeFac(72)
[2, 2, 2, 3, 3]
>>> primeFac(164)
[2, 2, 41]
>>> primeFac(144)
[2, 2, 2, 2, 3, 3]
>>> primeFac(89)
[89]
>>> primeFac(91)
[7, 13]
>>> primeFac(99)
[3, 3, 11]
>>> primeFac(17)
[17]
'''

#10.23

def f(indent, row):
    if row == 0:
        pass
    else:
        f(indent,row//2)
        print(' '*indent,'*'*row)
        f(indent+row//2,row//2)
'''
>>> f(0,1)
 *
>>> f(0,2)
 *
 **
  *
>>> f(3,6)
    *
    ***
     *
    ******
       *
       ***
        *
>>> f(3,4)
    *
    **
     *
    ****
      *
      **
       *
>>> f(0,16)
 *
 **
  *
 ****
   *
   **
    *
 ********
     *
     **
      *
     ****
       *
       **
        *
 ****************
         *
         **
          *
         ****
           *
           **
            *
         ********
             *
             **
              *
             ****
               *
               **
                *
'''
#10.24

def permutations(lst):
    if len(lst) == 0:
        return [[]]
    else:
        lstPerms = [ ]
        for subPerm in permutations(lst[1:]):
            for i in range(len(subPerm)+1):
                lstPerms += [subPerm[:i] + [lst[0]] + subPerm[i:]]
        return lstPerms
'''
>>> permutations([1,2])
[[1, 2], [2, 1]]
>>> permutations([1,2,4,9])
[[1, 2, 4, 9], [2, 1, 4, 9], [2, 4, 1, 9], [2, 4, 9, 1], [1, 4, 2, 9], [4, 1, 2, 9], [4, 2, 1, 9], [4, 2, 9, 1], [1, 4, 9, 2], [4, 1, 9, 2], [4, 9, 1, 2], [4, 9, 2, 1], [1, 2, 9, 4], [2, 1, 9, 4], [2, 9, 1, 4], [2, 9, 4, 1], [1, 9, 2, 4], [9, 1, 2, 4], [9, 2, 1, 4], [9, 2, 4, 1], [1, 9, 4, 2], [9, 1, 4, 2], [9, 4, 1, 2], [9, 4, 2, 1]]
>>> permutations([1,2,3])
[[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
'''



#10.29
import os
def traverse(path, indent):
    print(path)
    try:
        for branch in os.listdir(path):
            fullpath = os.path.join(path, branch)
            traverse(fullpath, indent)
        print(path)
    except:
        pass
#I was unable to figure out how to implement the indentations
#into the function. Help!
'''
>>> traverse('test',0)
test
test\fileA.txt
test\folder1
test\folder1\fileB.txt
test\folder1\fileC.txt
test\folder1\folder11
test\folder1\folder11\fileD.txt
test\folder1\folder11
test\folder1
test\folder2
test\folder2\fileD.txt
test\folder2\fileE.txt
test\folder2
test
'''


