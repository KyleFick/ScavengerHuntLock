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
print("Question 1")
print("""Solve and find the right date \nIt is in your heart,
-18/04/2005 No Items are correct
-14/02/2019 One Item is correct and in the right place
-11/11/2021 Two Items are correct and in the right place \n""")

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
print("Question 2")
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
print("Question 3")
print("""Where was our first Mini Vacation,
choose for below""")

q3 = "B"

c = input("""A.Crystal Blyde Resort,
B.Eagles Nest,
C.4th Avenue Place,\n
Answer: """)

if q3 == c:
    print("Well Done ")
else:
    print("Better luck next time")
    sleep(3)
    exit

sleep(1)
clear()

# Question 4
print("Question 4")
print("""Next Will Be Our Dream Destination,
It is multiple choice\n""")
q4 = "B"
d = input("""A. Los angeles,
B. Italy,
C. London,
D. Canada\n
Answer: """)

if q4 == d:
    print("Your Remembered My Love You so Sweet")
else:
    print("Well that was not expected")
    sleep(3)
    exit()

clear()
# Question 5
print("Question 5")
print("""What is the One Thing Ive always wanted us to do,
It is multiple choice\n""")
q5 = "C"
e = input("""A. Travel Oversea,
B. Have a Vacation,
C. Stargaze and Day break,
D. Go Hiking\n
Answer: """)

if q5 == e:
    print("Your Remembered My Love You so Sweet")
else:
    print("Well that was not expected")
    sleep(3)
    exit()    

sleep(1)
clear()


print("This is only the beginning Lets start the fun My Queen ❤️")
sleep(5)
clear()

print("You will receive the password to TheKey.py \n Once you reach your Destination ")

print("Please Enter this link into your Browser:\n\n https://grabify.link/91AM2L ")
# Grabify code 12UZAR
sleep(30)



# Windows use
#import os
#os.system("start \"\" https://example.com")

# linux use
#import os
#os.system("xdg-open \"\" https://example.com")