import tkinter as tk

#Func for when buttons are pressed
def openFile():
    print("Temp Val") #Temporarily do nothing

#Set-up Window
window = tk.Tk()
window.title("kbiSys")
window.geometry('350x225')

#Fill Window
attrLbl = tk.Label(window, text = "Attributes:") #Attribute Label
hardLbl = tk.Label(window, text = "Hard Constraints:") #Hard Constraints Label
prefLbl = tk.Label(window, text = "Preferences") #Preferences Label
penLbl = tk.Label(window, text = "Penalty Logic:") #Penalty Logic Label
possLbl = tk.Label(window, text = "Possibilistic Logic:") #Possibilistic Logic Label
quaLbl = tk.Label(window, text = "Qualitative Choice Logic:") #Qualitative Choice Logic Label

attrTxt = tk.Entry(window, width = 10) #Attribute Textbox
hardTxt = tk.Entry(window, width = 10) #Hard Constraints Textbox
penTxt = tk.Entry(window, width = 10) #Penalty Logic Textbox
possTxt = tk.Entry(window, width = 10) #Possibilistic Logic Textbox
quaTxt = tk.Entry(window, width = 10) #Qualitative Choice Logic Textbox

attrBtn = tk.Button(window, text = "Import File", command = openFile) #Attribute Button
hardBtn = tk.Button(window, text = "Import File", command = openFile) #Hard Constraints Button
penBtn = tk.Button(window, text = "Import File", command = openFile) #Penalty Logic Button
possBtn = tk.Button(window, text = "Import File", command = openFile) #Possibilistic Logic Button
quaBtn = tk.Button(window, text = "Import File", command = openFile) #Qualitative Choice Logic Button

attrLbl.grid(column = 0, row = 0, padx=5, pady=5)
attrTxt.grid(column = 1, row = 0, padx=5, pady=5)
attrBtn.grid(column = 2, row = 0, padx=5, pady=5)

hardLbl.grid(column = 0, row = 1, padx=5, pady=5)
hardTxt.grid(column = 1, row = 1, padx=5, pady=5)
hardBtn.grid(column = 2, row = 1, padx=5, pady=5)

prefLbl.grid(column = 0, row = 2, padx=5, pady=5)

penLbl.grid(column = 0, row = 3, padx=5, pady=5)
penTxt.grid(column = 1, row = 3, padx=5, pady=5)
penBtn.grid(column = 2, row = 3, padx=5, pady=5)

possLbl.grid(column = 0, row = 4, padx=5, pady=5)
possTxt.grid(column = 1, row = 4, padx=5, pady=5)
possBtn.grid(column = 2, row = 4, padx=5, pady=5)

quaLbl.grid(column = 0, row = 5, padx=5, pady=5)
quaTxt.grid(column = 1, row = 5, padx=5, pady=5)
quaBtn.grid(column = 2, row = 5, padx=5, pady=5)

window.mainloop()