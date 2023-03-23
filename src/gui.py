import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk

# TO-DO
    # can there be multiple comma/number values in single preference line
    # How much error checking do we need 


#Set-up Window
window = tk.Tk()
window.title("kbiSys")
window.geometry('565x505')

frame_1 = tk.Frame(window)

menubar = tk.Menu(window)
helpMenu = tk.Menu(menubar, tearoff=0)

#Values for checkboxes
exisVal = tk.IntVar()
exemVal = tk.IntVar()
optiVal = tk.IntVar()
omniVal = tk.IntVar()

#Func for when buttons are pressed
def openFile():
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

def generate():
    print('Generation Started...')
    attrStr = attrTxt.get('1.0', tk.END)
    hardStr = hardTxt.get('1.0', tk.END)
    penStr = penTxt.get('1.0', tk.END)
    possStr = possTxt.get('1.0', tk.END)
    quaStr = quaTxt.get('1.0', tk.END)

    #print(attrStr)
    #print(hardStr)
    #print(penStr)
    #print(possStr)
    #print(quaStr)

    #print(hardStr, type(hardStr))

    #attributes dict creation (key is left, items are right)
    attrStr = attrStr.split('\n')
    attrDict = {}
    for strs in attrStr:
        if strs:     # add error checking later
            strs = strs.replace(" ", "")
            strs = strs.split(':')
            #print(strs)
            strs[1] = strs[1].split(',')
            attrDict[strs[0]] = strs[1]
    print(attrDict)
        # do binary encoding

    #hard constraints dict creation
    hardStr = hardStr.split('\n')
    hardDict = {}
    for key, strs in enumerate(hardStr):
        if strs:
            hardDict[key] = strs
    print(hardDict)

    #penalty dict creation (delim on commma)
    penStr = penStr.split('\n')
    penDict = {}
    for key, strs in enumerate(penStr):
        if strs:
            strs = strs.split(",")     # add error checking later
            strs[1] = strs[1].replace(" ", "")
            penDict[key] = strs
    print(penDict)

    #possibilistic dict creation (delim on comma)
    possStr = possStr.split('\n')
    possDict = {}
    for key, strs in enumerate(possStr):
        if strs:
            strs = strs.split(",")  # add error checking later
            strs[1] = strs[1].replace(" ", "")
            possDict[key] = strs
    print(possDict)

    #Qualitative choice logic dict creation
    quaStr = quaStr.split('\n')
    quaDict = {}
    for key, strs in enumerate(quaStr):
        if strs:     # add error checking later
            quaDict[key] = strs
    print(quaDict)


def clear():
    print('Cancelled...')

#Can Delete?
def handleChecks():
    print("Handle Checks called:", exisVal.get(), exemVal.get(), optiVal.get(), omniVal.get())

def helpIndex():
    print("Help Index Selected")

def about():
    print("About Selected")

helpMenu.add_command(label="Help Index", command=helpIndex)
helpMenu.add_command(label="About...", command=about)

#Fill Window
attrLbl = tk.Label(window, text = "Attributes:") #Attribute Label
hardLbl = tk.Label(window, text = "Hard Constraints:") #Hard Constraints Label
prefLbl = tk.Label(window, text = "Preferences") #Preferences Label
penLbl = tk.Label(window, text = "Penalty Logic:") #Penalty Logic Label
possLbl = tk.Label(window, text = "Possibilistic Logic:") #Possibilistic Logic Label
quaLbl = tk.Label(window, text = "Qualitative Choice Logic:") #Qualitative Choice Logic Label
tasksLbl = tk.Label(window, text = "Reasoning Tasks:") #Reasoning Tasks Label

attrTxt = scrolledtext.ScrolledText(window, wrap = tk.WORD, width = 30, height = 3) #Attribute Textbox
hardTxt = scrolledtext.ScrolledText(window, wrap = tk.WORD, width = 30, height = 3) #Hard Constraints Textbox
penTxt = scrolledtext.ScrolledText(window, wrap = tk.WORD, width = 30, height = 3) #Penalty Logic Textbox
possTxt = scrolledtext.ScrolledText(window, wrap = tk.WORD, width = 30, height = 3) #Possibilistic Logic Textbox
quaTxt = scrolledtext.ScrolledText(window, wrap = tk.WORD, width = 30, height = 3) #Qualitative Choice Logic Textbox

attrBtn = tk.Button(window, text = "Import File", command = openFile) #Attribute Button
hardBtn = tk.Button(window, text = "Import File", command = openFile) #Hard Constraints Button
penBtn = tk.Button(window, text = "Import File", command = openFile) #Penalty Logic Button
possBtn = tk.Button(window, text = "Import File", command = openFile) #Possibilistic Logic Button
quaBtn = tk.Button(window, text = "Import File", command = openFile) #Qualitative Choice Logic Button

genBtn = tk.Button(frame_1, text = "Generate", command = generate)
clrBtn = tk.Button(frame_1, text = "Clear", command = clear)

exisCheck = tk.Checkbutton(window, text = "Existence of feasible objects", variable = exisVal, onvalue = 1, offvalue = 0)
exemCheck = tk.Checkbutton(window, text = "Exemplification", variable = exemVal, onvalue = 1, offvalue = 0)
optiCheck = tk.Checkbutton(window, text = "Optimization", variable = optiVal, onvalue = 1, offvalue = 0)
omniCheck = tk.Checkbutton(window, text = "Omni-optimization", variable = omniVal, onvalue = 1, offvalue = 0)

sep1 = ttk.Separator(window, orient='horizontal')
sep2 = ttk.Separator(window, orient='horizontal')
sep3 = ttk.Separator(window, orient='horizontal')

attrLbl.grid(column = 0, row = 0, padx=5, pady=5, sticky='nw')
attrTxt.grid(column = 1, row = 0, padx=5, pady=5)
attrBtn.grid(column = 2, row = 0, padx=5, pady=5)

hardLbl.grid(column = 0, row = 1, padx=5, pady=5, sticky='nw')
hardTxt.grid(column = 1, row = 1, padx=5, pady=5)
hardBtn.grid(column = 2, row = 1, padx=5, pady=5)

sep1.grid(row = 2, column=0, columnspan = 3, ipadx=250, padx = 10, pady=5)

prefLbl.grid(column = 0, row = 3, padx=5, pady=5, sticky='nw')

penLbl.grid(column = 0, row = 4, padx=20, pady=5, sticky='nw')
penTxt.grid(column = 1, row = 4, padx=5, pady=5)
penBtn.grid(column = 2, row = 4, padx=5, pady=5)

possLbl.grid(column = 0, row = 5, padx=20, pady=5, sticky='nw')
possTxt.grid(column = 1, row = 5, padx=5, pady=5)
possBtn.grid(column = 2, row = 5, padx=5, pady=5)

quaLbl.grid(column = 0, row = 6, padx=20, pady=5, sticky='nw')
quaTxt.grid(column = 1, row = 6, padx=5, pady=5)
quaBtn.grid(column = 2, row = 6, padx=5, pady=5)

sep2.grid(row = 7, column=0, columnspan = 3, ipadx=250, padx = 10, pady=5)

tasksLbl.grid(column = 0, row = 8, padx = 5, pady = 0, sticky='nw')

exisCheck.grid(column = 1, row = 8, padx = 0, pady = 0, sticky='nw')
exemCheck.grid(column = 1, row = 9, padx = 0, pady = 0, sticky='nw')
optiCheck.grid(column = 1, row = 10, padx = 0, pady = 0, sticky='nw')
omniCheck.grid(column = 1, row = 11, padx = 0, pady = 0, sticky='nw')

frame_1.grid(column = 2, row = 12, padx = 0, pady = 0, sticky = 'nsew')

genBtn.pack(side='left')
clrBtn.pack(side='right')

menubar.add_cascade(label="Help", menu=helpMenu)
window.config(menu=menubar)
window.mainloop()
