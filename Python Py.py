import random

myList = []
unique_list = []

def mainProgram():
    #build our while loop
    while True: 
        print("Hello, there! Let's work with lists!")
        print("Please choose front the following options. Type the number of the choice")
        choice = input("""1. Add to a list,
2. Return a value in a list,
3. Add a bunch of numbers! 
4. Random search
5. Linear Search
6. sort List
7. Print lists 
8. Quit    """)
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            addABunch()
        elif choice == "4":
            randomSearch()
        elif choice == "5":
            linearSearch()
        elif choice == "6":
            sortList(myList)
        elif choice == "7":
            printLists()
        elif choice == "8":
            searchItem = input("What are you looking for?  ")
            recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(searchItem))
        else:
            break
            
            

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!    ")
    myList.append(int(newItem))
    #we need to think about errors!

def addABunch():
    print("we're gonna add a bunch of number to your list!")
    numToAdd = input("How many new integers would you like to add?   ")
    numRange = input("And how high would you like these numbers to go   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is complete!")

def sortList(myList):
    #"myList" is the ARGUMENT this function takes.
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new, sorted list?  Y/N")
    if showMe.lower() =="y":
        print(unique_list)
     


    

def randomSearch():
    print("oH, iM sO rAnDom!!!")
    myList[random.randint(0, len(myList) -1)]

def linearSearch():
    print("We're going to go through this list one item at a time!")
    searchValue = input("What are you looking for?"    )
    for x in range(len(myList)):
        if myList[x] == int(searchValue):
             print("Your item is at index position ()".format(x))


def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if unique_list[mid] == x:
            print("Your number is at index psoition{}".format(mid))
            return mid
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid, mid-1, x)
        else:
            return recursiveBinarySearch(unique_list, mid +1, high, x)
    else:
        print("Your number isn't here!")

def literativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique _list)-1
    mid = 0

    while low <= high:
        mid = (high + low) //2

        if unique_list[mid] < x:
            low = mid + 1
        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index position here:    ")
    print(myList[int(indexPost)])


def printLists():
    if len(unique_list) ==0:
        print(myList)
    else:
        whichOne = input("Which list do you want to see? Sorted or un-sorted?   ")
        if whichOne.lower() == "sorted":
            print(unique_list)
                        

if __name__ == "__main__":
    mainProgram()
