# -*- coding: utf-8 -*-
"""
Created on Mon Dec 05 09:39:59 2016

Author: Amber Zaratsian
"""


import feedback
import random
from kanga import textwrap

mainflag = 0


def intro():
    print
    print "================================================================================"
    print  
    print textwrap.fill("The final Python data structure that we will be covering in these tutorials is dictionaries.", width=75)
    print
    print "================================================================================"
    
    
def q1():
    print
    print
    print textwrap.fill("Python dictionaries use a type of structure called mapping, which allows you to refer to each value by name. Values are stored under a key, which can be a number, string, or some tuples.", width=75)
    print
    print textwrap.fill("Think of dictionaries as an unordered set of key to value pairs (called items)...you can look up a specific word (key) to find its definition (value). Keys must be unique within a dictionary.", width=75)
    print
    print "================================================================================"  
    

def q2():
    print
    print
    print textwrap.fill("Keys are separated from its value by a colon (:), and the items are separated by commas, and all of this is wrapped in curly braces.", width=75)
    print
    print "A simple dictionary would be written like this:"
    print
    print ">>> dict = {'Name': 'Tom', 'Age': 27, 'Occupation': 'Pilot'}"
    global dict
    dict = {'Name': 'Tom', 'Age': 27, 'Occupation': 'Pilot'}
    print
    print textwrap.fill("In the above example, 'Name' is one of the keys and 'Tom' is the value associated with that particular key. 'dict' is the name of the dictionary in this case.", width=75)
    print
    print "================================================================================"  
      

def q3():
    print
    print
    print textwrap.fill("To access elements in a dictionary, you can use square brackets with the key to obtain its value.", width=75)
    print
    print ">>> print dict['Name']"
    print dict['Name']
    print
    print "================================================================================"    


def q4():
    print
    print
    print textwrap.fill("Try printing the value associated with 'Age'", width=75)

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.lower() == "print dict['Age']" or answer.lower() == 'print dict["Age"] ':
            print dict['Age']
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nprint dict['Age']"
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
                print "Not quite what I'm looking for.\nType print dict['Age'] and press Enter"  


def q5():
    print
    print
    print textwrap.fill("Let's take a look at some of the other basic dictionary operations. ", width=75)
    print
    print "len(d) will return the number of items (key-value pairs) in the dictionary"
    print
    print
    print "Go ahead and check the number of items in our dictionary dict"
    
    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.lower() == "len(dict)":
            print len(dict)
            print
            print "That's correct. There are 3 items in our dictionary"
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nprint len(dict)"
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
                print "Not quite what I'm looking for.\nType print len(dict) and press Enter" 
                

def q6():
    print
    print
    print textwrap.fill("Other dictionary methods:", width=75)
    print
    print "dict.items()       Returns a list of the pairs (key, value) in dict"
    print "dict.keys()        Returns a list of keys in dict"
    print "dict.values()      Returns a list of values in dict"
    print "dict.update(dict2) Adds the items (key-value pairs) from dict2 to dict"
    print "dict.has_key(k)    Returns true if k in dict, false otherwise"
    print "dict.copy()        Returns a shallow copy of dictionary dict"
    print
    print "================================================================================" 

                
def q7():
    print
    print
    print textwrap.fill("You can update a dictionary by adding a new item, modifying an existing item, or deleting an existing item.", width=75)
    print
    print "Let's add a new item to the dict dictionary: the person's employer."
    print
    print
    print ">>> dict['Employer'] = 'Airlines Inc.'"
    dict['Employer'] = 'Airlines Inc.'
    print
    print "Now we can check to see if it's been added:"
    print
    print ">>> print dict['Employer']"
    print dict['Employer']
    print
    print "================================================================================" 
    
                
def q8():
    print
    print
    print textwrap.fill("To modify an existing item we follow the same syntax as we did to add an item, but rather than adding a new key we just reference the name of the key who's value we want to change.", width=75)
    print
    print "Try changing 'Age' to 32"
    
    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "").lower() == "dict['age']=32" or answer.replace(" ", "").lower() == 'dict["age"]=32':
            dict['Age'] = 32
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \ndict['Age'] = 32"
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
                print "Not quite what I'm looking for.\nType dict['Age'] = 32 and press Enter" 
                

def q9():
    print
    print
    print textwrap.fill("You can delete an individual item, clear all the entries in the dictionary, or delete the entire dictionary.", width=75)
    print
    print "To delete an individual item use the del statement. It is written like:"
    print "del dict['k']"
    print
    print "Try deleting the item 'Occupation'"
    
    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.lower() == "del dict['occupation']" or answer.lower() == 'del dict["occupation"]':
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \ndel dict['Occupation']"
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
                print "Not quite what I'm looking for.\nType del dict['Occupation'] and press Enter" 
                

def q10():
    print
    print
    print "To clear all the entries in a dictionary:"
    print "dict.clear()"
    print
    print "To delete the entire dictionary:"
    print "del dict"
    print
    print "================================================================================" 
                 

def q11():
    print
    print
    print textwrap.fill("The dictionary we have been using for the above examples involves storing different kinds of information about one object. However, you can also use a dictionary to store one kind of information about many objects. For example, let's create a dictionary of our employee's favorite foods.", width=75)
    print
    print ">>> favorite_food = {\n\t'Joey': 'pizza',\n\t'Robin': 'sushi',\n\t'Megan': 'fried chicken',\n\t'Nick': 'ice cream'\n\t}"
    global favorite_food
    favorite_food = {'Joey': 'pizza', 'Robin': 'sushi', 'Megan': 'fried chicken', 'Nick': 'ice cream'}
    print
    print 
    print "In this case, each person's name is a key and their favorite food is a value."
    print
    print
    print "Try printing out Megan's favorite food"
    
    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer == "print favorite_food['Megan']" or answer == 'print favorite_food["Megan"]':
            print favorite_food['Megan']
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nprint favorite_food['Megan']"
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
                print "Not quite what I'm looking for.\nType print favorite_food['Megan'] and press Enter" 
                

def q12():
    print
    print
    print textwrap.fill("A single dictionary can hold large amounts of data. Because of this, Python allows you to loop through a dictionary. This can be done by looping through all the key-value pairs in a dictionary, through just its keys, or just its values.", width=75)
    print
    print 
    print "for k, v in dict.items():\n\tprint '\\nKey: ' + k \n\tprint 'Value: ' + v"
    print
    print
    print textwrap.fill("The first line is the syntax for writing a loop, you create names for the two variables that will hold the key and value for each pair. In this example, I have named them 'k' and 'v', but you can choose any names you want. The second part of the first line includes the dictionary name followed by the method items(), which we have already seen in the examples of dictionary methods above this will return a lits of key-value pairs. The last two lines are print statements with some formatting so our output will look nice. We use the variables to print each key followed by each value to labels that we have defined in this case to be 'Key' and 'Value'. Note that the '\\n' in the print statement inserts a blank line between each key-value pair.", width=75)
    print
    print "================================================================================" 
    
    
def q13():
    print
    print
    print "Let's try to loop through our favorite_food dictionary:"
    print
    print ">>> for k, v in favorite_food.items():\n\tprint '\\nName: ' + k \n\tprint 'Food: ' + v"    
    for k, v in favorite_food.items():
        print '\nName: ' + k 
        print 'Food: ' + v
    print
    print "================================================================================" 

    
def q14():
    print
    print
    print textwrap.fill("Note that the key-value pairs are not returned in the order in which they were stored. Python doesn't care about order in dictionaries, rather it only cares about the connections between keys and their values.", width=75)
    print
    print textwrap.fill("In the example above, we looped through our dictionary's key-value pairs. This was done by using the method items(). You can also loop through just the keys or values by using other dictionary methods.", width=75)
    print
    print "================================================================================" 

    

def conclusion():
    print
    print
    print textwrap.fill("Congratulations!! You've reached the end of this tutorial. The purpose of this lesson was to make you familiar with dictionaries. As a recap, dictionaries are made up of key-value pairs. The key must be unique and keys are immutable. You can look up a value by referencing its key. You can add new items, modify existing items, delete existing items, or even clear all items from a dictionary. This was a high-level overview of dictionaries, but there is plenty more you can do with this data structure.", width=75)
      
    
    
def dictionaries():
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
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        conclusion()   
        print
        print "================================================================================"
        print