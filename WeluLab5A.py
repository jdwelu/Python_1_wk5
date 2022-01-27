# Created a function to write an input to a file. 
def writeToFile():
    filepath = input("Please enter the filepath: ")
    info = input("Please enter the info you wish to append: ")
    fileObject = open(filepath, 'a')
    fileObject.write("\n" + info)
    fileObject.close()
    print()
    print("operation completed successfully")
    

# Created a function to read the contents of a text file.
def readToTextFile():
    filepath = input("Please enter the filepath: ")
    fileObject = open(filepath, 'r')
    text = fileObject.read()
    fileObject.close()
    print(text)
    print()
    print("operation completed successfully")


# created a feunction to read line by line the contents of a text file.
def readTextFileAsList():
    filepath = input("Please enter the filepath: ")
    fileObject = open(filepath, 'r')
    line = fileObject.readline()
    while(line != ""):
        print(line)
        line = fileObject.readline()
    fileObject.close()
    print()
    print("operation completed successfully")


# Start of the main program
print()
print("**********************************")
print("Welcome to the Python text editor!")
print("**********************************")
print()

# Defining the loop condition
condition = 'y'

while condition == "y":
    print("Please choose one of the following options: ")
    print()
    print(" 1.) Append lines to a file.")
    print(" 2.) Read a text file.")
    print(" 3.) Read a text file, line by line.")
    print()
    choice = input("Choice: ")
    if choice == "1":
        print()
        writeToFile()
        print()
    elif choice == "2":
        print()
        readToTextFile()
        print()
    elif choice == "3":
        print()
        readTextFileAsList()
        print()
    else:
        print()
        print("invalid entry")
        print()

    print()
    condition = input("Press 'y' to continue, anything else will exit?: ")
    











    


    
    
