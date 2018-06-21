# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 12:32:29 2016

Author: Amber Zaratsian
"""


import feedback
import random
import textwrap

mainflag = 0


def intro():
    print
    print "================================================================================"
    print 
    print textwrap.fill("This tutorial introduces tuples, another data structure in Python.", width=75)
    print
    print "================================================================================"
    
    
def q1():
    print
    print
    print textwrap.fill("A tuple is very similar to a list, except that it is immutable, meaning it cannot be changed. Tuples are fixed size in nature and lists are dynamic. Use tuples, rather than lists, when you want to store a set of values that should not be changed.", width=75)
    print
    print "================================================================================"
    
    
def q2():
    print
    print
    print textwrap.fill("A tuple looks just like a list except you use parentheses instead of square brackets.", width=75)
    print    
    print "Here's an example of a simple tuple:"
    print ">>> colors = ('red', 'blue', 'green')"
    global colors
    colors = ('red', 'blue', 'green')
    print
    print "================================================================================"
    

def q3():
    print
    print
    print textwrap.fill("You can still access individual items by referring to the item's index like we did for lists:", width=75)
    print
    print ">>> colors[1]"
    print colors[1]
    print
    print "================================================================================"
    
    
def q4():
    print
    print
    print "You can also slice tuples just like we lists:"
    print ">>> colors[0:2]"
    print colors[0:2]    
    print
    print "================================================================================"
    
    
def q5():
    print
    print
    print "You can also check to see if an element exists in a tuple:"
    print
    print
    print ">>> 4 in (2, 4, 6)"
    print 4 in (2, 4, 6)
    print
    print "Try checking to see if the element 'green' is in colors."

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.lower() == "'green' in colors" or answer.lower() == '"green" in colors':
            print 'green' in colors
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \n'green' in colors"
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
                print "Not quite what I'm looking for.\nType 'green' in colors and press Enter"  
    

def q6():
    print
    print                     
    print "Remember how in the list tutorial we were able to modify an item by doing:"
    print "fruits[2] = 'grapes'"
    print
    print "If we try to change a value in a tuple then Python will return a type error because it can't be done."
    print
    print ">>> colors[0] = 'purple'"
    print """Traceback (most recent call last):  \nFile "dimensions.py", line 3, in <module>\n    colors[0] = 'purple'\nTypeError: 'tuple' object does not support item assignment" """
    print
    print "================================================================================"



def q7():
    print
    print  
    print textwrap.fill("You can overwrite a tuple if you want to change the values.", width=75)
    print
    print ">>> colors = ('purple', 'blue', 'green')"
    colors = ('purple', 'blue', 'green')
    print ">>> print colors"
    print colors
    print
    print "================================================================================"

def q8():
    print
    print  
    print textwrap.fill("As you can see there isn't much you can do with tuples outside of creating them and accessing their elements. So you're asking why would you ever use tuples...well they are good to use when you want to protect data from ever being changed. Tuples are faster than lists. They can also be used as dictionary keys, which lists cannot be used in this way.", width=75)
    print
    print "================================================================================"
    
    
def conclusion():
    print
    print
    print textwrap.fill("Congratulations!! You've reached the end of this tutorial. The purpose of this lesson was to make you familiar with tuples. As a recap, remember tuples are immutable, whereas lists are mutable. In tuples, you cannot add, remove, or modify elements. You can access elements by indexing or slicing since this does not change the tuple. You can also search using the 'in' operator to checking for elements. Most of the time you will want to use lists, but in cases where you want to ensure the data will not be changed then use tuples.", width=75)
      



def tuples():
    intro()

    print
    raw_input("Press Enter to continue...")
    print
    print "==============================================================================="
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
        conclusion()   
        print
        print "================================================================================"
        print
