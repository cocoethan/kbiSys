import random
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

# pick 2 rand feas and show preference (no clue wtf strict equivalent or incomp means)
def exemplify():
    # so the thing ab this is we dont need to be calling these fnctns again, but because all options can
    # be done independently im just going to do it like this for now. can always change if we feel like optimizing
    penOutDict = {}
    possOutDict = {}
    quaOutDict = {}

    penOutDict = penalty()
    possOutDict = possibilistic()
    quaOutDict = qualitative()

    # throwing errors
    #keys = random.sample(feasible.keys(), 2)



    #print(keys)

# this should call penalty, possibilistic, qualitative, find one optimal value (if there is a tie, just pick one,
# and return the object, penalty, and choice
def optimize():
    penOutDict = {}
    possOutDict = {}
    quaOutDict = {}

    penOutDict = penalty()
    possOutDict = possibilistic()
    quaOutDict = qualitative()

    # this is getting the minimum penalty key(s) (correct)
    minPen = min(penOutDict.values())
    minPenKey = []

    for i in penOutDict:
        if penOutDict[i] == minPen:
            minPenKey.append(i)

    # this is getting the maximum possibilistic keys (i dont know if this is correct)
    maxPoss = max(possOutDict.values())
    maxPossKey = []

    for i in possOutDict:
        if possOutDict[i] == maxPoss:
            maxPossKey.append(i)

    # this is getting the minimum qualitative choice keys (i think this is correct??????)
    minQua = min(quaOutDict.values())
    minQuaKey = []

    for i in quaOutDict:
        if quaOutDict[i] == minQua:
            minQuaKey.append(i)
    
    print("Optimal Penalty key:")
    print(minPenKey[0])
    print("Optimal Possibility key:")
    print(maxPossKey[0])
    print("Optimal Qualitative Choice:")
    print(minQuaKey[0])

# this should call penalty, possibilistic, qualitative, find all optimal values (if there is a tie, return those
def omni():
    penOutDict = {}
    possOutDict = {}
    quaOutDict = {}

    penOutDict = penalty()
    possOutDict = possibilistic()
    quaOutDict = qualitative()

    # this is getting the minimum penalty key(s) (correct)
    minPen = min(penOutDict.values())
    minPenKey = []

    for i in penOutDict:
        if penOutDict[i] == minPen:
            minPenKey.append(i)

    # this is getting the maximum possibilistic keys (i dont know if this is correct)
    maxPoss = max(possOutDict.values())
    maxPossKey = []

    for i in possOutDict:
        if possOutDict[i] == maxPoss:
            maxPossKey.append(i)

    # this is getting the minimum qualitative choice keys (i think this is correct??????)
    minQua = min(quaOutDict.values())
    minQuaKey = []

    for i in quaOutDict:
        if quaOutDict[i] == minQua:
            minQuaKey.append(i)

    print("OMNI Penalty key:")
    print(minPenKey)
    print("OMNI Possibility key:")
    print(maxPossKey)
    print("OMNI Qualitative Choice:")
    print(minQuaKey)

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
        if 'AND' in currPen or 'OR' in currPen:
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
    #print(outDict)
    return outDict

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
        if 'AND' in currPen or 'OR' in currPen:
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
    #print(outDict)
    return outDict

def qualitative():
    global quaDict
    global feasible

    anotherTempList = []
    tempList = []
    quaRules = []
    quaList = []
    quaVals = []
    finalVals = []
    orflag = 0
    num = 0
    flag = 0
    for quals in quaDict.values():
        if 'BT' in quals:
            quaRules = []
            quals = quals.split('BT')
            # for each split on BT
            for num, part in enumerate(quals):
                tempList = []
                anotherTempList = []
                num += 1
                part = part.strip()
                if 'IF' in part:
                    part = part.split('IF')[0].strip()
                if 'NOT' in part:
                    part = notForPen(part)
                    part = part.strip()
                if 'AND' in part or 'OR' in part:
                    part = part.split("AND")
                    for i in range(len(part)):
                        part[i] = part[i].strip()
                        if 'OR' in part[i]:
                            part[i] = part[i].split("OR")
                            for j in range(len(part[i])):
                                currWord = part[i][j].strip()
                                anotherTempList.append(currWord)
                            tempList.append(anotherTempList)
                        else:
                            currWord = part[i]
                            tempList.append(part[i])

                    quaRules.append(tempList)
                else:
                    quaRules.append([part])
            quaList.append(quaRules)
        else:
            if 'IF' in quals:
                quals = quals.split('IF')[0].strip()
            quaList.append([[quals]])

    tempList = []
    anotherTempList = []

    for id, quals in enumerate(quaDict.values()):

        if quals[-2:] != 'IF':
            quals = quals.split('IF')[1].strip()
            # need to add a check to see if AND or OR are on RHS
            if 'AND' in quals or 'OR' in quals:
                tempList = []
                anotherTempList = []
                quals = quals.split("AND")
                for i in range(len(quals)):
                    quals[i] = quals[i].strip()
                    if 'OR' in quals[i]:
                        quals[i] = quals[i].split("OR")
                        for j in range(len(quals[i])):
                            currWord = quals[i][j].strip()
                            anotherTempList.append(currWord)
                        tempList.append(anotherTempList)
                    else:
                        currWord = quals[i]
                        tempList.append(quals[i])
                quals = tempList
                #quaRules.append(tempList)
            for i in quaList[id]:
                if isinstance(quals, list):
                    for j in quals:
                        i.append(j)
                else:
                    i.append(quals)
    #print(quaList)
    flag = 0
    num = 0
    for id, feas in enumerate(feasible.values()):
        for elem in quaList:
            for index, pref in enumerate(elem):
                for elements in pref:
                    if isinstance(elements, list):
                        if orflag != 1:
                            for orvalues in elements:
                                if orvalues in feas:
                                    orflag = 1
                                    break
                            if orflag != 1:
                                flag = 1
                                break
                    else:
                        if elements not in feas:
                            flag = 1
                            break
                if flag == 0:
                    num = index+1
                    break
                orflag = 0
                flag = 0
            quaVals.append(num)
            flag = 0
            orflag = 0
            num = 0
        finalVals.append(quaVals)
        quaVals = []

    sum = 0
    quaValsDict = {}
    quaList = []
    for tot in finalVals:
        for num in tot:
            sum += num
            #print(sum)
        quaList.append(sum)
        sum = 0

    for id, index in enumerate(feasible):
        quaValsDict[index] = quaList[id]

    #print(finalVals, quaValsDict)
    return quaValsDict

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
