import os
class Library:
    def __init__(self):
        self.booksCollectoin = []
        self.booksAvailable = []
        self.lendingDic = {}

    def displayBooks(self, s : int) -> str:
        os.system('cls')
        if s:
            print("These are the books available : ")
            for i in self.booksAvailable:
                return i
        else:
            print("These are the collection of books : ")
            for i in self.booksCollectoin:
                return i

    def lendBook(self) -> str:
        os.system('cls')
        bookName = str(input("Enter the name of book : "))
        for i in self.booksAvailable:
            if i == bookName:
                print("Book is available to lend!")
                personName = str(input("Enter Your Full Name : "))
                self.lendingDic[str(i)] = str(personName)
                self.booksAvailable.remove(i)
                return f"The book {i} is lent to {personName}"
        return "Book is either not available in the library or someone already else lent it, you can use 'who lent the book' function to find out more...."

    def addBook(self) -> str:
        os.system('cls')
        bookName = str(input("Enter the name of book you want to add : "))
        self.booksAvailable.append(bookName)
        self.booksCollectoin.append(bookName)
        return f"Book '{bookName}' has been added to the library"

    def bookLenderFinder(self) -> str:
        os.system('cls')
        BookName = str(input("Enter the name of book : "))
        for i, v in self.lendingDic.items():
            if i == BookName:
                return f"The book '{i}' has been lent to {v}"
            else:
                return f"No records found for the book '{BookName}'"

    def returBook(self) -> str:
        os.system('cls')
        bookName = str(input("Enter the name of book you want to return : "))
        for items, values in self.lendingDic:
            if bookName == items:
                self.lendingDic.pop(items)
                self.booksAvailable.append(items)
                return f"The book '{bookName}'has been returned and added to collection succesfully!"
            else:
                return f"Error, No records found for the book named '{bookName}', mabye there's a typo? Try again!"
libraryList = []
currentLibrary = ""
objDic = {}
while(1):
    print("\t\t\t\t\t\t\t\t\t\tWelcome to The Library manager v1.0!")
    mainMenu = int(input("\t1 -- create a new library\n\t2 -- Enter an existing library\n\t"))
    if mainMenu == 1:
        os.system('cls')
        libraryList.append(input("Enter the name of the library : "))
        objDic[str(libraryList[len(libraryList)-1])] = Library()
        print("Library created succesfully!")
        continue
    elif mainMenu == 2:
        os.system('cls')
        mainMenu = int(input("\t1 -- Enter Library name manually\n\t2 -- Show list of libraries available\n\t"))
        if mainMenu == 1:
            currentLibrary = input("Enter the name of library : ")
            for items in libraryList:
                if items == currentLibrary:
                    print("library found!\nEntering the library")
                else:
                    os.system('cls')
                    print("Library not Found! try show list of libraries function instead")
                    currentLibrary = ""
                    continue
        elif mainMenu == 2:
            os.system('cls')
            print("Here's the list of libraries available : ")
            for i in range(len(libraryList)):
                print(f"{i+1} -- {libraryList[i]}")
            currentLibrary = libraryList[int(input("select a library from above list "))-1]
            print(currentLibrary)
        else:
            os.system('cls')
            print("Error! you have entered a wrong input")
            continue
    print(f"\t\t\t\t\t\t\t\t\t\tWelcome to {currentLibrary} Library")
    libraryMenu = int(input("\t1 -- Display Books\n\t2 -- Lend a Book\n\t3 -- Who lent the Book?\n\t4 -- Add a Book in the Collection\n\t5 -- Return a Book\n\t"))
    if libraryMenu == 1:
        os.system('cls')
        print(objDic[currentLibrary].displayBooks(int(input("\t0 -- Display all Books\n\t1 -- Display books available to lend\n\t"))))
    elif libraryMenu == 2:
        os.system('cls')
        print(objDic[currentLibrary].lendBook())
    elif libraryMenu == 3:
        os.system('cls')
        print(objDic[currentLibrary].bookLenderFinder())
    elif libraryMenu == 4:
        os.system('cls')
        print(objDic[currentLibrary].addBook())
    elif libraryMenu == 5:
        os.system('cls')
        print(objDic[currentLibrary].returBook())
    else:
        os.system('cls')
        print("Error, you entered a wrong input. Please try again. ")
