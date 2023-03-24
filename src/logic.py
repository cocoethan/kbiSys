from numpy import binary_repr

objects = {}
attrValsDict = {} #Dictionary for only attribute values
feasible = {}

attrDict = {} #Dicitionary for attributes and values
hardDict = {} #Dictionary for hard constraints
penDict = {} #Dicitonary for penalty logic
possDict = {} #Dictionary for possibility logic
quaDict = {} #Dicitonary for qualitative choice logic

def fillDicts(attrDictTemp, hardDictTemp, penDictTemp, possDictTemp, quaDictTemp):
    global attrDict
    global hardDict
    global penDict
    global possDict
    global quaDict
    global objects
    global attrValsDict
    global feasible
    attrDict = attrDictTemp
    hardDict = hardDictTemp
    penDict = penDictTemp
    possDict = possDictTemp
    quaDict = quaDictTemp
    objects = {}
    attrValsDict = {}
    feasible = {}

    for i, key in enumerate(attrDict):
        attrValsDict[i] = attrDict[key]
    #print("attrValsDict", attrValsDict)

    #return
    genObjects(i + 1)

def genObjects(numOfAtts):
    global objects
    global attrValsDict
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
    global attrDict
    global hardDict
    global objects
    global feasible
    # get all constraints and remove all keywords (NOT fish becomes beef, remove OR, etc)
    # store each constraint line in its own item because of the AND conjunction
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
    return feasible

def exemplify():
    print()

def optimize():
    penalty()
    possibilistic()

def omni():
    print()

def penalty():
    global attrDict
    global penDict
    global objects
    global feasible

    outDict = {}
    penList = []
    for index, consts in enumerate(penDict.values()):
        # print(consts)
        tempList = []
        conjuncts = []
        currPen = consts[0]
        currPenVal = consts[1]
        if 'AND' or 'OR' in currPen:
            currPen = currPen.split("AND")
            for i in range(len(currPen)):
                currPen[i] = currPen[i].strip()
                if 'OR' in currPen[i]:
                    currPen[i] = currPen[i].split("OR")
                    for j in range(len(currPen[i])):
                        currWord = currPen[i][j].strip()
                        if 'NOT' in currWord:
                            currWord = notForPen(currWord)
                        tempList.append(currWord)
                    conjuncts.append(tempList)
                else:
                    currWord = currPen[i]
                    if 'NOT' in currWord:
                        currWord = notForPen(currWord)
                    conjuncts.append(currWord)
        penList.append([conjuncts, currPenVal])

    penalty = 0
    flag = 0

    for index in feasible:
        for values in penList:
            # this is for OR
            if any(isinstance(item, list) for item in values[0]):
                for item in values[0]:
                    if isinstance(item, list):
                        for orVal in item:
                            if orVal in feasible[index]:
                                flag = 0
                                break
                            else:
                                flag = 1
            if flag == 1:
                penalty += int(values[1])
                break
            # this is for AND
            for condition in values[0]:
                if isinstance(condition, list):
                    continue
                if condition not in feasible[index]:
                    penalty += int(values[1])
                    break
        outDict[index] = str(penalty)
        penalty = 0
        flag = 0
    print(outDict)
    #return outDict

def possibilistic():
    global attrDict
    global possDict
    global objects
    global feasible

    outDict = {}
    possList = []
    for index, consts in enumerate(possDict.values()):
        # print(consts)
        tempList = []
        conjuncts = []
        currPen = consts[0]
        currPenVal = float(1 - float(consts[1]))
        if 'AND' or 'OR' in currPen:
            currPen = currPen.split("AND")
            for i in range(len(currPen)):
                currPen[i] = currPen[i].strip()
                if 'OR' in currPen[i]:
                    currPen[i] = currPen[i].split("OR")
                    for j in range(len(currPen[i])):
                        currWord = currPen[i][j].strip()
                        if 'NOT' in currWord:
                            currWord = notForPen(currWord)
                        tempList.append(currWord)
                    conjuncts.append(tempList)
                else:
                    currWord = currPen[i]
                    if 'NOT' in currWord:
                        currWord = notForPen(currWord)
                    conjuncts.append(currWord)
        possList.append([conjuncts, currPenVal])

    possibilistic = 1
    flag = 0

    for index in feasible:
        for values in possList:
            # this is for OR
            if any(isinstance(item, list) for item in values[0]):
                for item in values[0]:
                    if isinstance(item, list):
                        for orVal in item:
                            if orVal in feasible[index]:
                                flag = 0
                                break
                            else:
                                flag = 1
            if flag == 1:
                if values[1] < possibilistic:
                    possibilistic = values[1]
            # this is for AND
            for condition in values[0]:
                if isinstance(condition, list):
                    continue
                if condition not in feasible[index]:
                    if values[1] < possibilistic:
                        possibilistic = values[1]
                    break
        #print("possibilistic", round(possibilistic, 1))
        outDict[index] = str(round(possibilistic, 1))
        possibilistic = 1
        flag = 0
    print(outDict)
    #return outDict

def notForPen(currWord):
    currWord = currWord.replace("NOT ", "")
    for atts in attrDict.values():
        if currWord == atts[0]:
            currWord = atts[1]
            break
        elif currWord == atts[1]:
            currWord = atts[0]
            break

    return currWord
