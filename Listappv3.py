import random

myList = []

def mainProgram():
    #build our while loop
    while True: 
        print("Hello, there! Let's work with lists!")
        print("Please choose front the following options. Type the number of the choice")
        choice = input("""1. Add to a list,
2. Return a value in a list,
3. Random search
4. Quit    """)
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            break

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!    ")
    myList.append(int(newItem))
    #we need to think about errors!

def randomSearch():
    print("oH, iM sO rAnDom!!!")
    myList[random.randint(0, len(myList) -1)]


def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index position here:    ")
    print(myList[int(indexPost)])


if__name__ == "__main__":
    mainProgram()
