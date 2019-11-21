#   https://github.com/hendersonreed19/Week12-utility.git 
#   Reed Henderson
#  ​ CSCI 102 – Section E
#   Week 11 - Part B

def PrintOutput(output):
    print('OUTPUT', output)
def LoadFile(file):
    lines = []
    with open(file) as file1:
        for line in file1:
            lines.append(line)
            
    return lines
    
def UpdateString(string, let, num):
    string2 = ''
    for i in range(len(string)):
        if i != num:
            string2 += string[i]
        else:
            string2 += let
            
    PrintOutput(string2)  
    
def FindWordCount(list1, word):
    count = 0
    for i in list1:
        if i == word:
            count +=1
    return count
            
def ScoreFinder(players, scores, name):
    name = name.lower()
    score = 0
    for i in range(len(players)):
        player = players[i]
        player = player.lower()
        if player == name:
            score = scores[i]
    if score == 0:
        return 'OUTPUT Player not found'
    else:    
        return1 = str('OUTPUT',name,'got a score of',int(score))
            
        return return1  
    
def Union(lista, listb):
    for item in lista:
        if item in listb:
            listb.remove(item)
    listc = lista + listb
    
    return listc
    
def Intersection(lista, listb):
    listc = []
    for item in lista:
        if item in listb:
            listc.append(item)
    
    return listc

def NotIn(lista,listb):
    for item in lista:
        if item in listb:
            lista.remove(item)
    
    return lista
