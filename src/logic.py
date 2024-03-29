import random
from numpy import binary_repr

objects = {}
attrValsDict = {}  # Dictionary for only attribute values
feasible = {}

attrDict = {}  # Dicitionary for attributes and values
hardDict = {}  # Dictionary for hard constraints
penDict = {}  # Dicitonary for penalty logic
possDict = {}  # Dictionary for possibility logic
quaDict = {}  # Dicitonary for qualitative choice logic

# filling dictionaries from text files
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
    # print("attrValsDict", attrValsDict)

    # return
    genObjects(i + 1)

# doing binary encoding
def genObjects(numOfAtts):
#    global objects
#    global attrValsDict
#    loopcnt = (2 ** numOfAtts)
#    for i in range(loopcnt):
#        tempList = list(binary_repr(i, numOfAtts))  #
#        valList = list(range(numOfAtts))
#        for j in range(numOfAtts):
#            tempArr = attrValsDict[(numOfAtts - (j + 1))]
#            if (tempList[(numOfAtts - (j + 1))] == '0'):
#                valList[j] = tempArr[1]
#            elif (tempList[(numOfAtts - (j + 1))] == '1'):
#                valList[j] = tempArr[0]
#        keyStr = 'o' + str(i)
#        objects[keyStr] = valList
    global objects
    global attrValsDict
    loopcnt = (2 ** numOfAtts)
    for i in range(loopcnt):
        tempList = list(binary_repr(i, numOfAtts))
        valList = list(range(numOfAtts))
        for j in range(numOfAtts):
            tempArr = attrValsDict[j]
            if (tempList[j] == '0'):
                valList[j] = tempArr[0]
            elif (tempList[j] == '1'):
                valList[j] = tempArr[1]
        keyStr = 'o' + str(i)
        objects[keyStr] = valList

def printObjs():
    global objects
    return objects

# determines which objects are feasible
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
            feasible['o' + str(key)] = items
        flag = 1
        succ = 0

    #print(feasible)
    return feasible

# picks 2 random feasible objects and shows preference
def exemplify():
    penOutDict = {}
    possOutDict = {}
    quaOutList = []

    penOutDict = penalty()
    possOutDict = possibilistic()
    quaOutList = qualitative()

    num1 = 0
    num2 = 0
    while num1 == num2:
        num1 = random.randint(0, (len(feasible) - 1))
        num2 = random.randint(0, (len(feasible) - 1))

    tempList = list(feasible.items())  # convert the view object to a list
    obj1 = tempList[num1][0]
    obj2 = tempList[num2][0]

    # 0 for obj1 is preferred 1 for obj2 is preferred, -1 for tie
    penPref = 0
    possPref = 0
    quaPref = 1

    obj1Pen = penOutDict[obj1]
    obj2Pen = penOutDict[obj2]
    obj1Poss = possOutDict[obj1]
    obj2Poss = possOutDict[obj2]

    obj1Qua = 0
    obj2Qua = 0
    if obj1 in quaOutList:
        obj1Qua = 1
    if obj2 in quaOutList:
        obj2Qua = 1

    returnStr = ""

    # checking for penalty preference
    if obj1Pen > obj2Pen:
        penPref = 1
    elif obj1Pen == obj2Pen:
        penPref = -1

    # checking for poss preference
    if obj1Poss < obj2Poss:
        possPref = 1
    elif obj1Poss == obj2Poss:
        possPref = -1

    # checking for choice preference
    if obj1Qua > obj2Qua:
        quaPref = 0
    elif obj1Qua == obj2Qua:
        quaPref = -1

    returnStr = "Using objects " + str(obj1) + " and " + str(obj2) + ":\n"

    # equivalent: equal in all
    if penPref == -1 and possPref == -1 and quaPref == -1:
        returnStr = returnStr + "Object " + str(obj1) + " and " + str(obj2) + " are equivalent."
        return returnStr

    # strictly preferred: better in all conditions
    if penPref == 1 and possPref == 1 and quaPref == 1:
        returnStr = returnStr + "Object " + str(obj2) + " is strictly preferred over " + str(obj1) + "."
        return returnStr

    if penPref == 0 and possPref == 0 and quaPref == 0:
        returnStr = returnStr + "Object " + str(obj1) + " is strictly preferred over " + str(obj2) + "."
        return returnStr

    # incomp: catchall
    returnStr = returnStr + "Objects " + str(obj1) + " and " + str(obj2) + " are incomparable."
    return returnStr


# this should call penalty, possibilistic, qualitative, find one optimal value (if there is a tie, just pick one,
# and return the object, penalty, and choice
def optimize():
    penOutDict = {}
    possOutDict = {}
    quaOutList = []

    penOutDict = penalty()
    possOutDict = possibilistic()
    quaOutList = qualitative()

    values = [int(v) for v in penOutDict.values()]
    minPen = min(values)
    minPenKey = []
    for i in penOutDict:
        if int(penOutDict[i]) == minPen:
            minPenKey.append(i)

    # this is getting the maximum possibilistic keys (correct)
    values = [float(v) for v in possOutDict.values()]
    maxPoss = max(values)
    maxPossKey = []

    for i in possOutDict:
        if float(possOutDict[i]) == maxPoss:
            maxPossKey.append(i)

    #print("Optimal Penalty key:")
    #print(minPenKey[0], "with", penOutDict[minPenKey[0]], "penalty")
    #print("Optimal Possibility key:")
    #print(maxPossKey[0], "with", possOutDict[maxPossKey[0]], "tolerance")
    #print("Optimal Qualitative Choice:")
    #print(quaOutList[0])

    return [[minPenKey[0], penOutDict[minPenKey[0]]], [maxPossKey[0], possOutDict[maxPossKey[0]]], [quaOutList[0]]]

# this should call penalty, possibilistic, qualitative, find all optimal values (if there is a tie, return all)
def omni():
    penOutDict = {}
    possOutDict = {}
    quaOutList = []

    penOutDict = penalty()
    possOutDict = possibilistic()
    quaOutList = qualitative()

    values = [int(v) for v in penOutDict.values()]
    minPen = min(values)
    minPenKey = []
    for i in penOutDict:
        if int(penOutDict[i]) == minPen:
            minPenKey.append(i)

    # this is getting the maximum possibilistic keys (correct)
    values = [float(v) for v in possOutDict.values()]
    maxPoss = max(values)
    maxPossKey = []

    for i in possOutDict:
        if float(possOutDict[i]) == maxPoss:
            maxPossKey.append(i)

    #print("OMNI Penalty key:")
    #print(*minPenKey)
    #print("OMNI Possibility key:")
    #print(*maxPossKey)
    #print("OMNI Qualitative Choice:")
    #print(*quaOutList)

    penOut = []
    possOut = []
    quaOut = []

    for keyVal in minPenKey:
        penOut.append(keyVal)
        penOut.append(penOutDict[keyVal])

    for keyVal in maxPossKey:
        possOut.append(keyVal)
        possOut.append(possOutDict[keyVal])

    return [penOut, possOut, quaOutList]

# caluclates total penalty for each object and returns
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
                    tempList = []
                else:
                    currWord = currPen[i]
                    if 'NOT' in currWord:
                        currWord = notForPen(currWord)
                    conjuncts.append(currWord)
        penList.append([conjuncts, currPenVal])

    penalty = 0
    flag = 0
    ortrack = []
    #print("PENLIST:", penList)
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
                        ortrack.append(flag)
            if 1 in ortrack:
                penalty += int(values[1])
                ortrack = []
                continue
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
        ortrack = []

    return outDict

# caluclates total possibilistic for each object and returns
def possibilistic():
    global attrDict
    global possDict
    global objects
    global feasible

    outDict = {}
    possList = []
    for index, consts in enumerate(possDict.values()):
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
                    tempList = []
                else:
                    currWord = currPen[i]
                    if 'NOT' in currWord:
                        currWord = notForPen(currWord)
                    conjuncts.append(currWord)
        possList.append([conjuncts, currPenVal])

    possibilistic = 1
    flag = 0
    ortrack = []
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
                        ortrack.append(flag)
            if 1 in ortrack:
                if values[1] < possibilistic:
                    possibilistic = values[1]
                    ortrack = []
                    continue
            # this is for AND
            for condition in values[0]:
                if isinstance(condition, list):
                    continue
                if condition not in feasible[index]:
                    if values[1] < possibilistic:
                        possibilistic = values[1]
                    break
        outDict[index] = str(round(possibilistic, 1))
        possibilistic = 1
        flag = 0
        ortrack = []

    return outDict

# determines choice preference for each object, finds optimal objects and returns
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
                # quaRules.append(tempList)
            for i in quaList[id]:
                if isinstance(quals, list):
                    for j in quals:
                        i.append(j)
                else:
                    i.append(quals)
    # print(quaList)
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
                    num = index + 1
                    break
                orflag = 0
                flag = 0
            quaVals.append(num)
            flag = 0
            orflag = 0
            num = 0
        finalVals.append(quaVals)
        quaVals = []

    # inf = 999
    for i in range(len(finalVals)):
        for j in range(len(finalVals[i])):
            if finalVals[i][j] == 0:
                finalVals[i][j] = 999

    predom = finalVals
    dominated = []
    weakpref = False

    # if obj1 is weakly preferred over obj2, obj1 dominates obj2
    # obj1 must not be dominated by any other object

    for index, obj1 in enumerate(finalVals):
        #print(obj1)
        for id, obj2 in enumerate(finalVals):
            weakpref = False
            # if both objects are eachother, or if obj1 has been dominated
            if index == id or obj1 in dominated:
                continue
            for i in range(len(obj1)):
                if obj1[i] < obj2[i]:
                    weakpref = True
                if obj1[i] > obj2[i]:
                    weakpref = False
                    break
            if weakpref:
                if obj2 not in dominated:
                    dominated.append(obj2)

    finalVals = [val for val in finalVals if val not in dominated]
    quaValsList = []
    templist = []
    for id, index in enumerate(predom):
        if index in finalVals:
            templist.append(id)

    for id, index in enumerate(feasible.keys()):
        if id in templist:
            quaValsList.append(index)

    return quaValsList

# removes not value
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
