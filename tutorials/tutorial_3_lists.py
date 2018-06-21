# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 10:20:48 2016

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
    print textwrap.fill("This tutorial introduces data structures. A data structure is a way to store data that is structured in some way. Python has a few built-in data structures such as lists, tuples, dictionaries, and sets.", width=75)
    print textwrap.fill("This tutorial will introduce and focus on lists in Python.", width=75)
    print
    print "================================================================================"
    

def q1():
    print
    print
    print textwrap.fill("A list is a collection of items in a particular order. Lists can contain any number of items any type of items. They are mutable, meaning they can be changed in place.", width=75)
    print
    print textwrap.fill("In Python, a list is represented by square brackets ([]) and individual items are separated by commas.", width=75)
    print    
    print "Here's an example of a simple list:"
    print ">>> cities = ['Raleigh', 'New York', 'Orlando', 'Las Vegas', 'Los Angeles', 'Dallas']"
    print
    global cities
    cities = ['Raleigh', 'New York', 'Orlando', 'Las Vegas', 'Los Angeles', 'Dallas']
    print "The print function can be used to print a list"
    print
    print "print cities"
    print cities
    print
    print "================================================================================"


def q2():
    print
    print
    print textwrap.fill("Your turn! Let's create a list named animals that contains the items: dog, cat, bird.", width=75)

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "").lower() == "animals=['dog','cat','bird']" or answer.replace(" ", "").lower() == 'animals=["dog","cat","bird"]':
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nanimals = ['dog', 'cat', 'bird']"
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
                print "Not quite what I'm looking for.\nType animals = ['dog', 'cat', 'bird'] and press Enter"
    global animals
    animals = ['dog', 'cat', 'bird']
    

def q3():
    print
    print         
    print "Now try printing out the list you just created."   
    
    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "").lower() == "animals" or answer == "print animals":
            print animals
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nanimals"
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
                print "Not quite what I'm looking for.\nType animals and press Enter"              
                
 
def q4():
    print
    print         
    print textwrap.fill("Most of the time you don't want to print the entire list so let's learn how to access individual items in a list.", width=75)
    print 
    print textwrap.fill("Since lists are ordered collections of items, you can access any item by telling Python the index of the item. To do this, you simply type the name of the list followed by the position in square brackets ([]).", width=75)
    print    
    print textwrap.fill("Remember in Python index positions always start with 0, not 1. So the first item in a list has an index of 0 and the second item has an index of 1", width=75)
    print    
    print "For example, to print the first item in the previously created list cities:"
    print
    print ">>> print cities[0]"
    print cities[0]
    print 
    print "Print the third item in the list you created called animals."
    
    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "").lower() == "animals[2]":
            print animals[2]
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nanimals[2]"
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
                print "Not quite what I'm looking for.\nType animals[2] and press Enter"                  
                

def q5():
    print
    print  
    print textwrap.fill("Python also has a way to count from the right. This can be useful if you want to see the last item or items toward the end and maybe you're unsure how long the list is. The syntax is to use negative numbers. The last item in a list would be -1, the second to last item would be -2.", width=75)
    print
    print "Print the last item in the list animals."
    
    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "").lower() == "animals[-1]":
            print animals[-1]
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nanimals[-1]"
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
                print "Not quite what I'm looking for.\nType animals[-1] and press Enter"                      
      
 
def q6():
    print
    print   
    print textwrap.fill("You can use individual values from a list just like you would do for any other variable in Python. Let's print a message using an item from the list.", width=75)
    print
    print '>>> print "My favorite animal is a " + animals[0]'
    print "My favorite animal is a " + animals[0]
    print
    print "================================================================================"

         
def q7():
    print
    print  
    print "Index Error:"
    print textwrap.fill("When working with lists you may see an index error. This occurs when you refer to an index position that is out of range, which is common in lists since people often forget that indexing begans with 0 and you must account for the off by one nature.", width=75)
    print    
    print textwrap.fill("For example, if you have four items in your list and you call for the fifth item then Python can't figure out the index you requested.", width=75)
    print
    print "================================================================================"


def q8():    
    print
    print
    print "The len() function can be used on a list to check the total number of items a list contains."
    print
    print ">>> print len(animals)"
    print len(animals)
    print
    print "================================================================================"
                

def q9():
    print
    print
    print textwrap.fill("Slicing can also be used on lists to access a range of items. The notation for using slicing is the name of the list followed by the index positions of the first item and last item in the desired range separated by a colon in square brackets ([]) .", width = 75)
    print    
    print "Example list[1:4]"
    print textwrap.fill("This will slice items beginning at the 1st position and include all elements up to the 4th position, but will not include the item at the 4th position. If you omit the first index, then Python will automatically start at the beginning of the list. Example:", width=75)
    print
    print "list[:3]"
    print
    print textwrap.fill("Similarly if you omit the second index, then the slice will continue to the end of the list:", width=75)
    print "list[2:]"
    print
    print "Try slicing the list cities from the 2nd index position to the 5th"
    
    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "").lower() == "cities[2:5]":
            print cities[2:5]
            print
            print textwrap.fill("Great job! Notice we get a range of items starting with the 3rd item in the list and up to the 6th item, but not including it.", width=75)
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \ncities[2:5]"
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
                print "Not quite what I'm looking for.\nType cities[2:5] and press Enter"  


def q10():
    print
    print    
    print textwrap.fill("Remember how we discussed indexing errors if you refer to an index out of range? Slice indices are handled more elegantly.", width=75)
    print
    print cities[3:7]
    print
    print textwrap.fill("The list cities only has 6 items, so the last index position would be 5. However, if we select an index that is too large then it's replaced by the string size.", width=75)
    print
    print "================================================================================"
    
    
def q11():
    print
    print                     
    print "Lists can be modified by changing, adding, and deleting items."
    print "Let's create a new list called fruit."
    print
    print ">>> fruits = ['apples', 'oranges', 'bananas', 'kiwis', 'pears', 'coconuts', 'pineapples']"   
    global fruits  
    fruits = ['apples', 'oranges', 'bananas', 'kiwis', 'pears', 'coconut', 'pineapple']    
    print
    print textwrap.fill("You can change any item in a list. To make a change simply specify the item we want changed and set it equal to a new value.", width=75)
    print    
    print "For example, I want to change 'bananas' to 'grapes' in our list of fruits:"
    print ">>> fruits[2] = 'grapes'"
    fruits[2] = 'grapes'
    print "print fruits"
    print fruits
    print
    print textwrap.fill("The output shows that bananas have been replaced with grapes and everything else in the list stays the same", width=75)
    print
    print "Try changing 'apples' to 'peaches'"
    
    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "").lower() == "fruits[0]='peaches'" or answer.replace(" ", "").lower() == 'fruits[0]="peaches"':
            fruits[0] = 'peaches'
            print "print fruits"
            print fruits
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nfruits[0] = 'peaches'"
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
                print "Not quite what I'm looking for.\nType fruits[0] = 'peaches' and press Enter"         
        

def q12():
    print
    print 
    print "Here's an overview of some of the most handy list methods:"
    print
    print "list.append(x) adds a single item to the end of the list"
    print "list.insert(i, x) inserts the element at the given index"
    print "list.remove(x) searches for the first instance of the given element & removes it"
    print "list.pop(i) removes the last item or the item at the given index"
    print "list.index(x) searches for the element from the beginning & returns its index"
    print "list.count(x) returns the number of times an item appears in the list"
    print "list.sort() sorts the list in place"
    print "list.reverse() reverses the list in place"
    print
    print textwrap.fill("In the examples above, 'list' is the list name, 'x' is an item and 'i' is the index position.", width=75)
    print
    print "Add 'apples' to the list fruits using the append() method"

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "").lower() == "fruits.append('apples')" or answer.replace(" ", "").lower() == 'fruits.append("apples")':
            fruits.append('apples')
            print "print fruits"
            print fruits
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nfruits.append('apples')"
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
                print "Not quite what I'm looking for.\nType fruits.append('apples') and press Enter"      


def q13():
    print
    print 
    print textwrap.fill("Add 'oranges' to the list fruits in the 3rd index position using the insert(i,x) method. The 'i' is an integer value.", width=75)
    print    
    print "Example: list_name.insert(1,'item')"

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "").lower() == "fruits.insert(3,'oranges')" or answer.replace(" ", "").lower() == 'fruits.insert(3,"oranges")':
            fruits.insert(3,'oranges')
            print "print fruits"
            print fruits
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nfruits.insert(3, 'oranges')"
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
                print "Not quite what I'm looking for.\nType fruits.insert(3, 'oranges') and press Enter"    
                
                
def q14():
    print
    print 
    print textwrap.fill("Remove 'kiwis' from the list fruits using the remove() method. Note if there are duplicate items in the list the remove will only delete the first occur of the item", width=75)

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "").lower() == "fruits.remove('kiwis')" or answer.replace(" ", "").lower() == 'fruits.remove("kiwis")':
            fruits.remove('kiwis')
            print "print fruits"
            print fruits
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nfruits.remove('kiwis')"
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
                print "Not quite what I'm looking for.\nType fruits.remove('kiwis') and press Enter"  
                

def q15():
    print
    print 
    print textwrap.fill("The pop() method removes the last item in a list, but lets you work with that item after it's removed.", width=75)
    print    
    print "Example to remove the last item:"
    print ">>> last_fruit = fruits.pop()"
    last_fruit = fruits.pop()
    print
    print ">>> last_fruit"
    print last_fruit
    print
    print ">>> fruits"
    print fruits
    print
    print textwrap.fill("The item 'apples' was removed from the list and is now stored in the variable last_fruit.", width=75)
    print
    print textwrap.fill("You can also specify an index of an item and remove that particular item rather than the last item.", width=75)
    print    
    print "Example to remove the 2nd item: second_item = list_name.pop(1)"
    print
    print textwrap.fill("Try removing the 3rd item from the list fruits and store it in a variable named fruit_removed (Hint: 3rd item does not have an index of 3)", width=75)

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "").lower() == "fruit_removed=fruits.pop(2)":
            fruit_removed = fruits.pop(2)
            print "print fruit_removed"
            print fruit_removed
            print
            print "fruits"
            print fruits
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nfruit_removed = fruits.pop(2)"
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
                print "Not quite what I'm looking for.\nType fruit_removed = fruits.pop(2) and press Enter"  


def q16():
    print
    print 
    print textwrap.fill("Find the index position of the item 'pears' in the list fruits using the index() method", width=75)

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "").lower() == "fruits.index('pears')" or answer.replace(" ", "").lower() == 'fruits.index("pears")':
            fruits.index('pears')
            print fruits.index('pears')
            print
            print "Excellent, this shows us that 'pears' is the 3rd item in the list"
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nfruits.index('pears')"
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
                print "Not quite what I'm looking for.\nType fruits.index('pears') and press Enter"  
          
          
def q17():
    print
    print 
    print "Count the number of times 'oranges' appears in the list fruits"

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "").lower() == "fruits.count('oranges')" or answer.replace(" ", "").lower() == 'fruits.count("oranges")':
            print fruits.count('oranges')
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nfruits.count('oranges')"
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
                print "Not quite what I'm looking for.\nType fruits.count('oranges') and press Enter"         
          
          
def q18():
    print
    print 
    print textwrap.fill("Important note about sorting: when lists contain both numerical and string values, the sort() method will sort numerically first, then alphabetically.", width=75)
    print
    print "Example the list ['x', 3.2, 'a', 1] would be sorted [1, 3.2, 'a', 'x']"
    print    
    print "Sort the list fruits"

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "").lower() == "fruits.sort()" :
            fruits.sort()
            print "print fruits"
            print fruits
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nfruits.sort()"
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
                print "Not quite what I'm looking for.\nType fruits.sort() and press Enter"    
                

def q19():
    print
    print
    print textwrap.fill("Sequence operations, like the + and *, can be used on lists much like strings. The result will be a new string.", width=75)
    print textwrap.fill("The + operator means concatenation. When we add two lists together, we get a new list of these combined.", width=75)
    print ">>> [1, 2, 3] + [4, 5, 6]"
    print [1, 2, 3] + [4, 5, 6]
    print
    print "The * operator means repetition."
    print ">>> ['hello'] * 3"
    print ['hello'] * 3
    print
    print "You can also check to see if a value is in a list:"
    print ">>> 2 in [2, 4, 6]"
    print 2 in [2, 4, 6]
    print
    print "Check to see if 'grapes' is in fruits."

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.lower() == "'grapes' in fruits" or answer.lower() == '"grapes" in fruits':
            print 'grapes' in fruits
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \n'grapes' in fruits"
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
                print "Not quite what I'm looking for.\nType 'grapes' in fruits and press Enter"           
    
    
def conclusion():
    print
    print
    print textwrap.fill("Congratulations!! You've reached the end of this tutorial. In this lesson, you learned about lists, one of the data structures in Python. You learned how to create a list, as well as how to modify elements. You learned about several of the available methods for modifying a list like append, remove, and sort. You learned how to use indexing and slicing to access individual or a range of elements from a lists. This tutorial does not cover everything you can do with lists, but you should have a solid foundation now to began creating and working with lists on your own.", width=75)
               
          
          
def lists():
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
        q16()
        
        
    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q17()
        

    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q18()
        

    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q19()        


    if mainflag != 1:     
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        conclusion()        
        print
        print "================================================================================"
        print
