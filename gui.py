import tkinter as tk
import main

bgCol = "#4B064B"

# Main Window
win = tk.Tk()
win.geometry('400x180')
win.title("Covid Tracker")
win.configure(bg=bgCol)

# Header
headerFrame = tk.Frame(win)
headerFrame.pack(fill=tk.X)

headText = tk.Label(headerFrame)
headText.configure(text='COVID TRACKER')
headText.pack()

# Input
inpFrame = tk.Frame(win)
inpFrame.configure(bg=bgCol)
inpFrame.pack(pady=20,fill=tk.X)

inpEntry = tk.Entry(inpFrame)
inpEntry.configure(width=40)
inpEntry.pack(pady=10)

stateHead = tk.Label(win,text='')


def onClick():

    inpFrame.pack(side='bottom')

    win.geometry('800x800')
    
    userInput = inpEntry.get()
    stateData = main.mainCall(userInput)

    stateHead.configure(text=stateData['state'])
    stateHead.configure(font=('Helvetica',20))
    stateHead.place(x=20,y=20)

    i = 0
    for key in stateData:
        
        keyLabel = tk.Label(win,text=key.upper(),bg=bgCol,fg='white')
        keyLabel.place(x=20,y=100 + i)

        valLabel = tk.Label(win,text=stateData[key],bg=bgCol,fg='white')
        valLabel.place(x=200,y=100 + i)


        i = i + 40

#Button
trackButton = tk.Button(inpFrame,text="Track",width=20)
trackButton.pack(pady=20,side='bottom')
trackButton.configure(command=onClick)



win.mainloop()