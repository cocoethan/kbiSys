import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk

#Set-up Window
window = tk.Tk()
window.title("kbiSys")
window.geometry('550x550')

#
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

#Can Delete?
def handleChecks():
    print("Handle Checks called:", exisVal.get(), exemVal.get(), optiVal.get(), omniVal.get())

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
genBtn = tk.Button(window, text = "Generate", command = generate)

exisCheck = tk.Checkbutton(window, text = "Existence of feasible objects", variable = exisVal, onvalue = 1, offvalue = 0)
exemCheck = tk.Checkbutton(window, text = "Exemplification:", variable = exemVal, onvalue = 1, offvalue = 0)
optiCheck = tk.Checkbutton(window, text = "Optimization", variable = optiVal, onvalue = 1, offvalue = 0)
omniCheck = tk.Checkbutton(window, text = "Omni-optimization", variable = omniVal, onvalue = 1, offvalue = 0)

sep1 = ttk.Separator(window, orient='horizontal')
sep2 = ttk.Separator(window, orient='horizontal')
sep3 = ttk.Separator(window, orient='horizontal')

attrLbl.grid(column = 0, row = 0, padx=5, pady=5)
attrTxt.grid(column = 1, row = 0, padx=5, pady=5)
attrBtn.grid(column = 2, row = 0, padx=5, pady=5)

hardLbl.grid(column = 0, row = 1, padx=5, pady=5)
hardTxt.grid(column = 1, row = 1, padx=5, pady=5)
hardBtn.grid(column = 2, row = 1, padx=5, pady=5)

prefLbl.grid(column = 0, row = 2, padx=5, pady=5)

#sep1.grid(row = 3)

penLbl.grid(column = 0, row = 3, padx=5, pady=5)
penTxt.grid(column = 1, row = 3, padx=5, pady=5)
penBtn.grid(column = 2, row = 3, padx=5, pady=5)

possLbl.grid(column = 0, row = 4, padx=5, pady=5)
possTxt.grid(column = 1, row = 4, padx=5, pady=5)
possBtn.grid(column = 2, row = 4, padx=5, pady=5)

quaLbl.grid(column = 0, row = 5, padx=5, pady=5)
quaTxt.grid(column = 1, row = 5, padx=5, pady=5)
quaBtn.grid(column = 2, row = 5, padx=5, pady=5)

tasksLbl.grid(column = 0, row = 6, padx = 5, pady = 0)

exisCheck.grid(column = 1, row = 6, padx = 0, pady = 0, sticky='w')
exemCheck.grid(column = 1, row = 7, padx = 0, pady = 0, sticky='w')
optiCheck.grid(column = 1, row = 8, padx = 0, pady = 0, sticky='w')
omniCheck.grid(column = 1, row = 9, padx = 0, pady = 0, sticky='w')

genBtn.grid(column = 1, row = 10, padx = 0, pady = 20)

sep1.grid(row = 11, sticky = "ew")

window.mainloop()
