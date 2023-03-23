from numpy import binary_repr

objects = {}
attrValsDict = {} #Dictionary for only attribute values

attrDict = {} #Dicitionary for attributes and values
hardDict = {} #Dictionary for hard constraints
penDict = {} #Dicitonary for penalty logic
possDict = {} #Dictionary for possibility logic
quaDict = {} #Dicitonary for qualitative choice logic

def fillDicts(attrDictTemp, hardDictTemp, penDictTemp, possDictTemp, quaDictTemp):
    attrDict = attrDictTemp
    hardDict = hardDictTemp
    penDict = penDictTemp
    possDict = possDictTemp
    quaDict = quaDictTemp

    for i, key in enumerate(attrDict):
        attrValsDict[i] = attrDict[key]
    print(attrValsDict)

    genObjects(i + 1)

def genObjects(numOfAtts):
    loopcnt = (2 ** numOfAtts)
    for i in range(loopcnt):
        tempList = list(binary_repr(i, numOfAtts))#
        valList = list(range(numOfAtts))
        for j in range(numOfAtts):
            tempArr = attrValsDict[(numOfAtts - (j + 1))]
            if(tempList[(numOfAtts - (j + 1))] == '0'):
                valList[j] = tempArr[1]
            elif(tempList[(numOfAtts - (j + 1))] == '1'):
                valList[j] = tempArr[0]
        keyStr = 'o' + str(i)
        objects[keyStr] = valList

def existence():
    print()

def exemplify():
    print()

def optimize():
    print()

def omni():
    print()
