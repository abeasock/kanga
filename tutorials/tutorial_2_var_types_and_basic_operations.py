# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 13:42:51 2016

Author: Amber Zaratsian
"""


import feedback
import random
from kanga import textwrap


mainflag = 0
exitflag = 0

def intro():
    print
    print "================================================================================"
    print
    print textwrap.fill("In this tutorial you will learn the basic concepts of the Python programming language", width=75)
    print
    print "================================================================================"


def q1():
    print
    print
    print"The Python interpreter acts as a simple interactive calculator."
    print
    print "Type 3 + 6 and press Enter: "

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "") == "3+6":
            print 3 + 6
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \n3 + 6"
            print
            print "================================================================================"
            break
        elif answer == "main()":
            print "Quitting tutorial & returning to main menu\n"
            global mainflag
            mainflag = 1
            break
        else:
            tries = tries + 1
            if tries < 3:
                print feedback.wrong[random.randint(0, len(feedback.wrong)-1)]
            elif tries >= 3:
                print "Not quite what I'm looking for.\nType 3 + 6 and press Enter"


def q2():
    print
    print textwrap.fill("The result of a calculation could also be stored in a variable. This is handy if you're using the result in a second calculation and don't want to retype the calculation everytime.", width=75)
    print
    print textwrap.fill("It's very simple to create a new variable in Python, just type whatever you want the variable name to be followed by equals symbol (=) and the value you want assigned. Example z = 2 * 4", width=75)
    print
    print "Let's assign the result of 3 + 6 to a new variable called x"

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "") == "x=3+6":
            print
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print textwrap.fill("The result is not printed this time because you assigned the value to a variable. Python assumes you don't want to see the result immediately.", width=75)
            print
            print "================================================================================"
            break
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nx = 3 + 6"
            print
            print "================================================================================"
            break
        elif answer == "main()":
            print "Quitting tutorial & returning to main menu\n"
            global mainflag
            mainflag = 1
            break
        else:
            tries = tries + 1
            if tries < 3:
                print feedback.wrong[random.randint(0, len(feedback.wrong)-1)]
            elif tries >= 3:
                print "Not quite what I'm looking for.\nType x = 3 + 6 and press Enter"
    global x
    x = 3 + 6


def q3():
    print
    print
    print textwrap.fill("To have the contents of the variable printed out, just type the variable name and press enter.", width=75)
    print
    print "Give it a try."

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer == 'x':
            print x
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nx"
            print
            print "================================================================================"
            break
        elif answer == "main()":
            print "Quitting tutorial & returning to main menu\n"
            global mainflag
            mainflag = 1
            break
        else:
            tries = tries + 1
            if tries < 3:
                print feedback.wrong[random.randint(0, len(feedback.wrong)-1)]
            elif tries >= 3:
                print "Not quite what I'm looking for.\nType x and press Enter"


def q4():
    print
    print
    print textwrap.fill("It's important in Python to note the difference between = and ==. Assignment uses ones equals sign (=), whereas comparision uses two equal signs (==).", width=75)
    print
    print "In the above example, we assigned 3 + 6 to the variable x using the = sign."
    print
    print textwrap.fill("We could compare x to the value 9 to see if this is the result stored in x. To do this we would use ==. If it is then 'True' will be returned, otherwise 'False'.", width=75)
    print
    print ">>> x == 9"
    print x == 9
    print
    print "================================================================================"


def q5():
    print
    print
    print "Assign the result of x - 4 to a new variable named y"
    print

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "") == "y=x-4":
            print
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \ny = x - 4"
            print
            print "================================================================================"
            break
        elif answer == "main()":
            print "Quitting tutorial & returning to main menu\n"
            global mainflag
            mainflag = 1
            break
        else:
            tries = tries + 1
            if tries < 3:
                print feedback.wrong[random.randint(0, len(feedback.wrong)-1)]
            elif tries >= 3:
                print "Not quite what I'm looking for.\nType y = x - 4 and press Enter"
    global y
    y = x - 4


def q6():
    print
    print
    print "Print the result stored in y"
    print

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "") == 'y':
            print y
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \ny"
            print
            print "================================================================================"
            break
        elif answer == "main()":
            print "Quitting tutorial & returning to main menu\n"
            global mainflag
            mainflag = 1
            break
        else:
            tries = tries + 1
            if tries < 3:
                print feedback.wrong[random.randint(0, len(feedback.wrong)-1)]
            elif tries >= 3:
                print "Not quite what I'm looking for.\nType y and press Enter"


def q7():
    print
    print
    print "Basic datatypes in Python include integers, floats, and strings."
    print
    print "Examples:"
    print "   Integers: 5, 32"
    print "   Floats: 2.3, 3.14"
    print """   Strings: "hello", 'My name is' """
    print
    print 'Try assigning the string "good day" to a variable named message'

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.lower() == 'message = "good day"' or answer.lower() == "message = 'good day'" or answer.lower() == 'message="good day"' or answer.lower() == "message='good day'":
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break
        elif answer == "skip()":
            print
            print 'Skipping question...the correct input was: \nmessage = "good day"'
            print
            print "================================================================================"
            break
        elif answer == "main()":
            print "Quitting tutorial & returning to main menu\n"
            global mainflag
            mainflag = 1
            break
        else:
            tries = tries + 1
            if tries < 3:
                print feedback.wrong[random.randint(0, len(feedback.wrong)-1)]
            elif tries >= 3:
                print """Not quite what I'm looking for.\nType message = "good day" and press Enter"""
    global message
    message = "hello world"


def q8():
    print
    print
    print textwrap.fill("There are methods that allow you to change the case of words in a string. For example a string can be converted to all lower case by doing: message.lower(). There is also the method title() which displays each word with a capital letter.", width=75)
    print
    print textwrap.fill("Try applying the method upper() to your message variable to upcase the entire string.", width=75)

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "") == 'message.upper()':
            print message.upper()
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nmessage.upper()"
            print
            print "================================================================================"
            break
        elif answer == "main()":
            print "Quitting tutorial & returning to main menu\n"
            global mainflag
            mainflag = 1
            break
        else:
            tries = tries + 1
            if tries < 3:
                print feedback.wrong[random.randint(0, len(feedback.wrong)-1)]
            elif tries >= 3:
                print "Not quite what I'm looking for.\nType message.upper() and press Enter"


def q9():
    print
    print
    print textwrap.fill("You can also combine strings using a method called concatenation. Python uses the + symbol to combine strings.", width=75)
    print
    print 'First, assign the string "Jane" to a variable named first_name'

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "") == 'first_name="Jane"' or answer.replace(" ", "") == "first_name='Jane'":
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break
        elif answer == "skip()":
            print
            print 'Skipping question...the correct input was: \nfirst_name = "Jane"'
            print
            print "================================================================================"
            break
        elif answer == "main()":
            print "Quitting tutorial & returning to main menu\n"
            global mainflag
            mainflag = 1
            break
        else:
            tries = tries + 1
            if tries < 3:
                print feedback.wrong[random.randint(0, len(feedback.wrong)-1)]
            elif tries >= 3:
                print """Not quite what I'm looking for.\nType first_name = "Jane" and press Enter"""
    global first_name
    first_name = "Jane"


def q10():
    print
    print
    print 'Assign another string "Doe" to a variable named last_name'

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "") == 'last_name="Doe"' or answer.replace(" ", "") == "last_name='Doe'":
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break
        elif answer == "skip()":
            print
            print 'Skipping question...the correct input was: \nlast_name = "Doe"'
            print
            print "================================================================================"
            break
        elif answer == "main()":
            print "Quitting tutorial & returning to main menu\n"
            global mainflag
            mainflag = 1
            break
        else:
            tries = tries + 1
            if tries < 3:
                print feedback.wrong[random.randint(0, len(feedback.wrong)-1)]
            elif tries >= 3:
                print """Not quite what I'm looking for.\nType last_name = "Doe" and press Enter"""
    global last_name
    last_name = "Doe"


def q11():
    print
    print
    print textwrap.fill("Now concatenate first_name and last_name into a new variable full_name.", width=75)
    print
    print 'Example: a = b + " " + c'
    print
    print textwrap.fill("Note: we need to also add a blank space between the variables to seperate the words.", width=75)

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer == 'full_name = first_name + " " + last_name' or answer == "full_name = first_name + ' ' + last_name":
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break
        elif answer == "skip()":
            print
            print 'Skipping question...the correct input was: \nfull_name = "Jane Doe"'
            print
            print "================================================================================"
            break
        elif answer == "main()":
            print "Quitting tutorial & returning to main menu\n"
            global mainflag
            mainflag = 1
            break
        else:
            tries = tries + 1
            if tries < 3:
                print feedback.wrong[random.randint(0, len(feedback.wrong)-1)]
            elif tries >= 3:
                print """Not quite what I'm looking for.\nType full_name = "Jane Doe" and press Enter"""
    global full_name
    full_name = "Jane Doe"


def q12():
    print
    print
    print textwrap.fill("We've already seen at the beginning of this tutorial how integers work in Python. In Python any number with a decimal point is a float. These work similarly to integers. One important note in Python 2 is division of two integers may return different results than expect.", width=75)
    print
    print "For example, divide 3/2"

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "") == "3/2":
            print 3/2
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print textwrap.fill("However, this is not the answer we expected. This is because division of integers in Python 2 results in an integer with the remainder truncated. Important to note the result is not rounded; the remainder is simply left off.", width=75)
            print
            print "================================================================================"
            break
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \n3/2"
            print
            print "================================================================================"
            break
        elif answer == "main()":
            print "Quitting tutorial & returning to main menu\n"
            global mainflag
            mainflag = 1
            break
        else:
            tries = tries + 1
            if tries < 3:
                print feedback.wrong[random.randint(0, len(feedback.wrong)-1)]
            elif tries >= 3:
                print "Not quite what I'm looking for.\nType 3/2 and press Enter"


def q13():
    print
    print
    print textwrap.fill("To avoid this behavior in Python 2, you must make sure at least one of the numbers is a float. This will ensure the result is also a float.", width=75)
    print
    print "Let's try again and this time divide 3/2.0"

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "") == "3/2.0":
            print 3/2.0
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \n3/2.0"
            print
            print "================================================================================"
            break
        elif answer == "main()":
            print "Quitting tutorial & returning to main menu\n"
            global mainflag
            mainflag = 1
            break
        else:
            tries = tries + 1
            if tries < 3:
                print feedback.wrong[random.randint(0, len(feedback.wrong)-1)]
            elif tries >= 3:
                print "Not quite what I'm looking for.\nType 3/2.0 and press Enter"


def q14(year = 1987):
    print
    print
    print textwrap.fill("Sometimes you'll want to use a variable's numeric value within a message. Concatenating a string and a number will result in a Type Error. You can use the str() function to avoid this by converting the number to a string. I've already created a variable called year which contains the integer 1987.", width=75)
    print "We can check this:"
    print
    print ">>> print year"
    print year
    print
    print textwrap.fill('Now enter print "Birth year is " + str(year) (Include the print and notice the blank space in the string after "is " which is needed to add a space between the concatenation)', width=75)

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer == 'print "Birth year is " + str(year)' or answer == "print 'Birth year is ' + str(year)":
            print 'Birth year is ' + str(year)
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break
        elif answer == "skip()":
            print
            print """Skipping question...the correct input was: \nprint "Birth year is " + str(year)"""
            print
            print "================================================================================"
            break
        elif answer == "main()":
            print "Quitting tutorial & returning to main menu\n"
            global mainflag
            mainflag = 1
            break
        else:
            tries = tries + 1
            if tries < 3:
                print feedback.wrong[random.randint(0, len(feedback.wrong)-1)]
            elif tries >= 3:
                print """Not quite what I'm looking for.\nType print "Birth year is " + str(year) and press Enter"""


def q15():
    print
    print textwrap.fill("Sometimes whitespace can be an issue. For example, the strings 'apples' and 'apples ' are  different to Python because of the extra space in 'apples '. There are methods in Python that can be used to strip out whitespace from a string. The rstrip() removes whitespace at the right end of a string, while lstrip() removes whitespace at the left end of a string.", width=75)
    print
    print ">>> fruit = ' apple '"
    fruit = ' apple '
    print ">>> print fruit"
    print repr(fruit)
    print ">>> fruit = fruit.rstrip()"
    fruit = fruit.rstrip()
    print ">>> print fruit"
    print repr(fruit)
    print
    print textwrap.fill("Note to remove whitespace permanently from a string, you have to store the stripped value back into the variable", width=75)
    print
    print "Follow the example above to strip the whitespace from the left side"

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer == "fruit = fruit.lstrip()":
            fruit = fruit.lstrip()
            print repr(fruit)
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nfruit = fruit.lstrip()"
            print
            print "================================================================================"
            break
        elif answer == "main()":
            print "Quitting tutorial & returning to main menu\n"
            global mainflag
            mainflag = 1
            break
        else:
            tries = tries + 1
            if tries < 3:
                print feedback.wrong[random.randint(0, len(feedback.wrong)-1)]
            elif tries >= 3:
                print "Not quite what I'm looking for.\nType fruit = fruit.lstrip() and press Enter"



def conclusion():
    print
    print
    print textwrap.fill("Congratulations!! You've reached the end of this tutorial. In this lesson, you learned about the basic data types in Python (integers, floats, strings). You learned how to work with numbers and perform calculations. You learned how to create and name variables. You learned about modifying the case of strings using lower(), upper(), and title().", width=75)



def basics():
    intro()

    print
    raw_input("Press Enter to continue...")
    print
    print "================================================================================"
    q1()


    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q2()


    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q3()


    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q4()


    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q5()

    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q6()


    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q7()


    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q8()


    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q9()


    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q10()


    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q11()


    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q12()


    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q13()


    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q14()


    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q15()


    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        conclusion()
        print
        print "================================================================================"
        print