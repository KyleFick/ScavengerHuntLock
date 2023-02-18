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

print("""Welcome To the Hunt Lock,
Lets begin with the First question.""")
sleep(2)

print("Figure out the Puzzle below. ")
sleep(3)
clear()

# Question 1
print("""Solve and find the right date \nIt is in your heart,
-18/04/2005 No Items are correct
-14/02/2019 One Item is correct
-11/11/2021 Two Items are correct\n""")

q1 = input("What is the correct Date? ")
a = "14/11/2021"
if  q1 == a:
    print("Yes you got it !!! ")
else:
    print("Try again Next Time")
    sleep(3)
    exit()


sleep(1)
clear()
# Question 2
print("""Now that you figured it out,
Lets see whats next,
On this day what happen,
It is multiple choice\n""")
q2 = "E"
b = input("""A. Did we have a picnic,
B. Did we Go to a club,
C. Did we have a mini-vacation,
D. Did we meet up at Clearwater
E. The day I Asked You To Be MINE\n
Answer: """)

if q2 == b:
    print("Your Remembered My Love You so Sweet")
else:
    print("Well that was not expected")
    sleep(3)
    exit()

sleep(1)
clear()
# Question 3
print("""Where was our first Mini Vacation,
choose for below""")

q3 = "B"

c = input("""A.Crystal Blyde Resort,
B.Eagles Next,
C.4th Avenue Place,\n
Answer: """)

if q3 == c:
    print("Well Done thats the Final Question")
else:
    print("Better luck next time")
    sleep(3)
    exit

sleep(1)

# Question 4
print("""Now that you figured it out,
Lets see whats next,
On this day what happen,
It is multiple choice\n""")
q4 = "E"
b = input("""A. Did we have a picnic,
B. Did we Go to a club,
C. Did we have a mini-vacation,
D. Did we meet up at Clearwater
E. The day I Asked You To Be MINE\n
Answer: """)

if q4 == b:
    print("Your Remembered My Love You so Sweet")
else:
    print("Well that was not expected")
    sleep(3)
    exit()

sleep(1)
clear()
print("This is only the beginning Lets start the fun My Queen ❤️")

print("Please Enter this link into your Browser: \n\nwww.google.com")

sleep(60)



# Windows use
#import os
#os.system("start \"\" https://example.com")

# linux use
#import os
#os.system("xdg-open \"\" https://example.com")