# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Alex Frain,02/13/21,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
objFile = open(objFile, "r")
for strData in objFile:
    lstRow = strData.split(",")  # Returns a list!
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
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
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        for row in lstTable:
            print(row["Task"] + " | " + row["Priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        print("Enter your new Task and its Priority.")
        strTask = input("Enter Task: ")
        strPriority = input("Enter its Priority ('Low','Medium', or 'High': ")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print(f"{strTask} added to your To Do List with a priority of {strPriority}")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strTask = input("Enter the Task to remove: ")
        boolTaskFound = False
        for row in lstTable:
            if str(row["Task"]).lower() == strTask.lower():
                boolTaskFound = True
                lstTable.remove(row)
                print(f"{strTask} removed from your To Do List!")
        if not boolTaskFound:
            print(f"{strTask} not found in your To Do List")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt","w")
        for row in lstTable:
            strData = f"{row['Task']},{row['Priority']}\n"
            objFile.write(strData)
        objFile.close()
        print("Tasks written to your To Do List File")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("Exiting ToDoList script")
        break  # and Exit the program
