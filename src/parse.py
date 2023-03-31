from logic import fillDicts

def parseInput(attrStr, hardStr, penStr, possStr, quaStr):
    attrDict = {}  # Dicitionary for attributes and values
    hardDict = {}  # Dictionary for hard constraints
    penDict = {}  # Dicitonary for penalty logic
    possDict = {}  # Dictionary for possibility logic
    quaDict = {}  # Dicitonary for qualitative choice logic

    # attributes dict creation (key is left, items are right)
    attrStr = attrStr.split('\n')
    for strs in attrStr:
        if strs:  # add error checking later
            strs = strs.replace(" ", "")
            strs = strs.split(':')
            # print(strs)
            strs[1] = strs[1].split(',')
            attrDict[strs[0]] = strs[1]
    # do binary encoding

    # hard constraints dict creation
    hardStr = hardStr.split('\n')
    for key, strs in enumerate(hardStr):
        if strs:
            hardDict[key] = strs

    # penalty dict creation (delim on commma)
    penStr = penStr.split('\n')
    for key, strs in enumerate(penStr):
        if strs:
            strs = strs.split(",")  # add error checking later
            strs[1] = strs[1].replace(" ", "")
            penDict[key] = strs

    # possibilistic dict creation (delim on comma)
    possStr = possStr.split('\n')
    for key, strs in enumerate(possStr):
        if strs:
            strs = strs.split(",")  # add error checking later
            strs[1] = strs[1].replace(" ", "")
            possDict[key] = strs

    # Qualitative choice logic dict creation
    quaStr = quaStr.split('\n')
    for key, strs in enumerate(quaStr):
        if strs:  # add error checking later
            quaDict[key] = strs

    fillDicts(attrDict, hardDict, penDict, possDict, quaDict)

def parseOutput(type, data):
    string = ""

    if(type == 'obj'):
        string = "Objects -\n"
        for i, key in enumerate(data):
            tempArr = data[key]
            string = string + str(key) + ":"
            for j, vals in enumerate(tempArr):
                string = string + " " + tempArr[j]
            string = string + '\n'
        string = string + '\n'

    if(type == 'exis'):
        string = "Feasible -\n"
        for i, key in enumerate(data):
            tempArr = data[key]
            string = string + str(key) + ":"
            for j, vals in enumerate(tempArr):
                string = string + " " + tempArr[j]
            string = string + '\n'
        string = string + '\n'

    if (type == 'exem'):
        string = "Exemplification -\n" + str(data) + '\n'
        string = string + '\n'

    if (type == 'opti'):
        string = "Optimal -\n"
        for i, val in enumerate(data):
            if(i == 0):
                string = string + "Penalty Optimal:\n" + data[0][0] + " with " + data[0][1] + " penalty.\n\n"
            elif(i == 1):
                string = string + "Possibilistic Optimal:\n" + data[1][0] + " with " + data[1][1] + " tolerance.\n\n"
            elif(i == 2):
                string = string + "Choice Optimal:\n" + data[2][0] + "\n"
        string = string + '\n'

    if (type == 'omni'):
        string = "Omni-Optimal -\n"
        for i, val in enumerate(data):
            if (i == 0):
                tempArr = data[0]
                string = string + "Penalty Optimal:\n"
                for j, vals in enumerate(tempArr):
                    if(j % 2 == 0):
                        string = string + tempArr[j] + " with " + tempArr[j + 1] + " penalty.\n"
                    else:
                        pass
            elif (i == 1):
                tempArr = data[1]
                string = string + "Possibilistic Optimal:\n"
                for j, vals in enumerate(tempArr):
                    if (j % 2 == 0):
                        string = string + tempArr[j] + " with " + tempArr[j + 1] + " tolerance.\n"
                    else:
                        pass
            elif (i == 2):
                tempArr = data[2]
                string = string + "Qualitative Optimal:\n"
                for j, vals in enumerate(tempArr):
                    if(j == (int(len(tempArr)) - 1)):
                       string = string + str(tempArr[j])
                    else:
                        string = string + str(tempArr[j]) + ", "
        string = string + '\n'

    return string
