#Q1
a="Twinkle,twinkle,little star,\n\tHow I wonder what you are!\n\t\tupabove the world so high,\n\t\tLike a diamond in the sky.\nTwinkle,twinkle,little star,\n\tHow I wonder what you are"
print(a)

#Q2 write a program to get the python version you are using

import sys
print("Python version " ,sys.version)

#Q3 Write a python program to display the current date and time
#Sample output:
#Current Date and Time:
#2014-07-05 14:34:14


import datetime
now=(datetime.datetime.now())
print("Current Date and Time :")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

#Q4 Write a program which accepts the radius of circle from the user and compute the area.
#sample output:
#r=1.1
#Area=3.8013271108436504

r=float(input("Radius of circle :"))
area=(3.14159*(r**2))
print("Area :",area)

#Q5 Write a python program which accepts the first and lastname from user and print them in reverse order with a space between them
FirstName=input()
LastName=input()
print(LastName, " ", FirstName)

#Q6 Write a python program which accepts a sequence of comma-seperated numbers from user and generate a list and tuple with those numbers

st=input()
st=st.split(',')
print(st)
tuple=tuple(st)
print(tuple)

#Q10 Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
#Sample numbers list :

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
for n in numbers:
    if n % 2 == 0:
        print(n)
    if n == 237:
        break