from numpy import binary_repr

objects = {}
attrValsDict = {} #Dictionary for only attribute values

attrDict = {} #Dicitionary for attributes and values
hardDict = {} #Dictionary for hard constraints
penDict = {} #Dicitonary for penalty logic
possDict = {} #Dictionary for possibility logic
quaDict = {} #Dicitonary for qualitative choice logic

def fillDicts(attrDictTemp, hardDictTemp, penDictTemp, possDictTemp, quaDictTemp):
    global attrDict
    attrDict = attrDictTemp
    global hardDict
    hardDict = hardDictTemp
    global penDict
    penDict = penDictTemp
    global possDict
    possDict = possDictTemp
    global quaDict
    quaDict = quaDictTemp

    for i, key in enumerate(attrDict):
        attrValsDict[i] = attrDict[key]
    print(attrValsDict)

    #return
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
    #print(objects)
    #return objects

def existence():

    # get all constraints and remove all keywords (NOT fish becomes beef, remove OR, etc)
    # store each constraint line in its own item because of the AND conjunction
    feasible = {}
    conjunctDict = {}
    for index, consts in enumerate(hardDict.values()):
        constraints = []
        consts = consts.split("OR")
        for i in range(len(consts)):
            currConst = consts[i].strip()
            if 'NOT' in currConst:
                currConst = currConst.replace("NOT ", "")
                for atts in attrDict.values():
                    if currConst == atts[0]:
                        currConst = atts[1]
                        break
                    elif currConst == atts[1]:
                        currConst = atts[0]
                        break
            constraints.append(currConst)
        conjunctDict[index] = constraints

    # for each object, check that it meets constraints(contains at least one item per line). If not, remove object
    flag = 1
    succ = 0
    for key, items in enumerate(objects.values()):
        for constraints in conjunctDict.values():
            for value in constraints:
                if value in items:
                    flag = 0
                    break
            succ += flag
            flag = 1

        if succ == 0:
            feasible['o'+str(key)] = items
        flag = 1
        succ = 0

    print(feasible)

def exemplify():
    print()

def optimize():
    print()

def omni():
    print()
