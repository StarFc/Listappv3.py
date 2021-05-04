from tkinter import

top = Tk()
playList = []

def results():
    print(playList)
    
def addToList():
    newItem= E1.get()
    PlayList.append(newItem))


#This is a Label widget
L1 = Label(top, text= "Playlist Maker")
L1.grid(column= 0, row = 1)

#This is a Entry widget
E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)

#This is a Button widget
B1 = Button(text= "    Print List      ", bg="green", command= )
B1.grid(column+ 0, row= 3)

B2 = Button(text = "Add to List", bg = "green", command = addToList)
B2.grid(column = 1, row = 2)


top.mainloop()
