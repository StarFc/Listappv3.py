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

void printSomething();

int main(){

    printSomething();


    return 0;
}

void printSomething(){
    print("I'm a function"):
    return;

}

    
            
            

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!    ")
    myList.append(int(newItem))
    #we need to think about errors!

'' 

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
"""
Function explanation: we created a variable called 'indexPos', and stored
the result of an input function inside it.
We then force the value stored in indexPos into an integer (using the int() function)
and used the variable to call a value at a specific index position.
"""


def randomSearch():
    print("oH, iM sO rAnDom!!!")
    myList[random.randint(0, len(myList) -1)]

"""
The first line where it says "randomseach" it means adding a random vector, and vector has to do with the two random segments.
the second line shows that so the computer can understand the statment you are trying to give.
The 3rd line is to create a variable.
"""



def linearSearch():
    print("We're going to go through this list one item at a time!")
    searchValue = input("What are you looking for?"    )
    for x in range(len(myList)):
        if myList[x] == int(searchValue):
             print("Your item is at index position ()".format(x))

"""
Linearsearch is suppose to check the elements of this program.
Second line is the give a statment.
third line returns it back, so when if you were to run it it returns to where you code it to stop
For "x in range" I remember it having to do something like with an integer, to a loop.
5th line is ti create a variable.
The last line I think is to print what you want the computer to know.
"""



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

"""
BinarySeach is an algorthm, and with recursive it means looping around over and over.
The second line I think its so the computer can understand it, but I dont know what it does, same with the third line.
The fourth line It does everything step by step.
The 5th line, where it says "print"your making a statement, to show the computer.
return is the reurn the program.
elif is also makes a statement i think.
return is to return to where you want it to return when you run the program.
For else, I assume it will be the same as elif, like it being a statment.
"""

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

"""
The first line is like to obtain something.
for low, high, mid, I think they have something to do with the numbers, like for example 1 to 100, or something like that.
for unique list, is for so the computer can understand what we are trying to do.
where elif is, its to make a statment, but with the unique list, it can mean a different thing, or it can try to make a statment with that.
return, is to return to where you started.
"""

def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index position here:    ")
    print(myList[int(indexPost)])

"""
The IndexValue is a squence, for the program.
The second line is the statment your trying to make.
I think indexPos is sort like a key value.
the last line prints a lsit for the index thing.
"""

def printLists():
    if len(unique_list) ==0:
        print(myList)
    else:
        whichOne = input("Which list do you want to see? Sorted or un-sorted?   ")
        if whichOne.lower() == "sorted":
            print(unique_list)

"""
Def printLists is like changing the code.
The seoncd line, I think its like creating it so it wont mess with something.
Third line prints lsit for the index thing.
else is making a statment I think.
The fifth line I think its either making a statment for the code or updating something.
The sixth line is the sort the code, like when you run it.
The last line is so the computer can understand what you are trying to do.
"""



if __name__ == "__main__":
    mainProgram()

"""
That first part of the first line has something to do with modules, but I dont remeber what it was. "Main" is so you can run the file straight into it.
