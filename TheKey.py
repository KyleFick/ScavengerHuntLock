# import web browser

import webbrowser
import os

# import only system from os

from os import system, name

# import sleep to show for some time period 

from time import sleep

# define our clear function 

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux (here, os.name is possible posix)
    else:

        _ = system('clear')

clear()


print (" Enter the password to Get the Scavenger Hunt Key")

password = "Shnukums@Sadie"

passw = input("Enter the Password to reveal the Key!!!")

if passw == password:
    print("You Have Unlocked the Key To Start the Hunt")

else:
    print("Please try again")


print("You Have Completed the First Challenge\n Now use the Key the Start\n Key: https://9734-102-39-205-25.in.ngrok.io ")

sleep(30)