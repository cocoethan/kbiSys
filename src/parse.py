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
    print(attrDict)
    # do binary encoding

    # hard constraints dict creation
    hardStr = hardStr.split('\n')
    for key, strs in enumerate(hardStr):
        if strs:
            hardDict[key] = strs
    print(hardDict)

    # penalty dict creation (delim on commma)
    penStr = penStr.split('\n')
    for key, strs in enumerate(penStr):
        if strs:
            strs = strs.split(",")  # add error checking later
            strs[1] = strs[1].replace(" ", "")
            penDict[key] = strs
    print(penDict)

    # possibilistic dict creation (delim on comma)
    possStr = possStr.split('\n')
    for key, strs in enumerate(possStr):
        if strs:
            strs = strs.split(",")  # add error checking later
            strs[1] = strs[1].replace(" ", "")
            possDict[key] = strs
    print(possDict)

    # Qualitative choice logic dict creation
    quaStr = quaStr.split('\n')
    for key, strs in enumerate(quaStr):
        if strs:  # add error checking later
            quaDict[key] = strs
    print(quaDict)

    fillDicts(attrDict, hardDict, penDict, possDict, quaDict)

def parseOutput(type, data):
    string = ""

    if(type == 'exis'):
        string = "Feasible:\n"
        for i, key in enumerate(data):
            print("HERE:", data[key])
            tempArr = data[key]
            string = string + str(key) + ":"
            for j, vals in enumerate(tempArr):
                string = string + " " + tempArr[j]
            string = string + '\n'

    if (type == 'exem'):
        string = "\nExemplification:\n" + str(data) + '\n'

    if (type == 'opti'):
        print("parseOutput Called:",data)
    if (type == 'omni'):
        print("parseOutput Called:",data)
    return string
