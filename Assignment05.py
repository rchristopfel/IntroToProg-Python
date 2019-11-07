# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created starter script
# Rebecca Christopfel, 11/6/19, Added code to complete module 05
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python Dictionary.
open(objFile, "a")
objFile = open(objFile, "r")
for row in objFile:
    strData = row.split()
    dicRow = {"Task": strData[0], "Priority": strData[1]}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        if not lstTable: # checks if lstTable has data
            print("There is no data in your list.")
        else:
            for row in lstTable:
                print(row["Task"] + ", " + row["Priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strTask = str(input("Enter a new Task: "))
        strPriority = str(input("How does " + strTask + " rank in priority?: "))
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        # print(lstTable)
        continue

    # Step 5 - Remove a new item to the list/Table
    elif strChoice.strip() == '3':
        print("These are your current Tasks:\n")  # display current tasks
        for row in lstTable:
            print(row["Task"])

        strRemoveTask = input("\nWhich task would you like to remove from the list above? ")
        for row in lstTable:
            if strRemoveTask in row["Task"]:
                print()
                lstTable.remove({"Task": row["Task"], "Priority": row["Priority"]})
                print("If you entered a Task from above, it has been deleted.\n"
                      "\n (You can check by entering '1' below.)")
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(row["Task"] + " " + row["Priority"] + '\n')
        objFile.close()
        print("Data was saved!")
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Thanks for playing!")
        break