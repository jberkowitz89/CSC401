def cheer(TeamName):
    print('How do you spell winner?\nI know, I know!')
    for char in TeamName:
        print(char.upper(), end=' ')
    print('!\nAnd that\'s how you spell winner!\nGo',TeamName+'!')
 
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

    
