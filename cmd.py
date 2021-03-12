import time
print("Microsoft Windows [Version 10.0.10.2.40]")
print("<c> 2015 Microsoft Corporation. All rights reserved.")
print()
answer = input("C:\Users\User>")
if answer == "help":
    print("CD                 ENTER IN FILES!")
    print("MKDIR              THIS COMMAND MAKE FOLDER!")
    print("EXIT               EXIT COMMAND PROMPT!")
    print("PAUSE              PAUSE COMMAND PROMPT!")
    print("WHOAMI             SHOW WHAT USER ARE YOU!")
    print("LS                 SHOW WHAT FILES ARE IN FILE THAT YOU ARE THERE!")
elif answer == "whoami":
    print("User")
elif answer == "mkdir":
    answer2 = input("C:\Users\User>")
    if answer2 == "ls":
        print("Folder")
    elif answer2 == "cd File":
        answer3 = input("C:\Users\User\Folder>")
        if answer3 == "ls":
            print("README.txt")
        elif answer3 == "cd":
            print("C:\Users\User\Folder\")
        elif answer3 == "exit":
            quit()
        elif answer3 == "whoami":
            print("User")
        elif answer3 == "pause":
            input("press enter to continue . . .")
        elif answer3 == "mkdir":
            print("you can make only one folder")
        elif answer3 == "help":
            print("CD                 ENTER IN FILES!")
            print("MKDIR              THIS COMMAND MAKE FOLDER!")
            print("EXIT               EXIT COMMAND PROMPT!")
            print("PAUSE              PAUSE COMMAND PROMPT!")
            print("WHOAMI             SHOW WHAT USER ARE YOU!")
            print("LS                 SHOW WHAT FILES ARE IN FILE THAT YOU ARE THERE!")
        else:
            print("no command found!")
    elif answer2 == "cd":
        print("C:\Users\User\")
    elif answer2 == "mkdir":
        print("you can make only one folder")
    elif answer2 == "pause":
        input("press enter to continue . . .")
    elif answer2 == "exit":
        quit()
    elif answer2 == "help":
        print("CD                 ENTER IN FILES!")
        print("MKDIR              THIS COMMAND MAKE FOLDER!")
        print("EXIT               EXIT COMMAND PROMPT!")
        print("PAUSE              PAUSE COMMAND PROMPT!")
        print("WHOAMI             SHOW WHAT USER ARE YOU!")
        print("LS                 SHOW WHAT FILES ARE IN FILE THAT YOU ARE THERE!")
elif answer == "exit":
    quit()
elif answer == "cd":
    print("C:\Users\User\")
elif answer == "ls":
    print("there is nothing :(")
elif answer == "pause":
    input("press enter to continue . . .")
else:
    print("command is not found!")