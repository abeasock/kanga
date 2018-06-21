# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 13:06:17 2016

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
    print textwrap.fill("Now that you have a foundation on the different data structures in Python, we can move on to loops", width=75)
    print 
    print "================================================================================"
    

def q1():
    print
    print
    print textwrap.fill("A loop statement allows you to execute a statement or code block multiple times.", width=75)
    print
    print "There are two primary types of loops in Python:"
    print "    - while loop"
    print "    - for loop"
    print
    print "================================================================================" 
    
    
def q2():
    print
    print
    print textwrap.fill("A while loop executes a block of code while a given boolean condition is true.", width=75)
    print
    print textwrap.fill("A common example to show a while loop in action is use a while loop to count through a series of numbers. We will start with setting a variable, y, equal to 1. The while loop is set to keep executing the code as long as the value of y is less than 5. The code inside the loop prints the value of y and then adds 1 to that value.", width=75)
    print
    print "This would be written like this:"
    print
    print
    print ">>> y = 1"
    print ">>> while y < 5:"
    print "        print y"
    print "        y += 1"
    y = 1
    while y < 5:
        print y
        y += 1
    print
    print
    print "The += operation in the code above is shorthand to mean y = y + 1"
    print
    print textwrap.fill("Python repeats the while loop as long as the condition y < 5 is true. Once the value of y equals 5 the loop stops running.", width=75)
    print
    print textwrap.fill("Notice the colon at the end of a while statement, this tells Python to interpret the next line as the start of a loop. For code to be executed as part of the loop the lines must be indented. This tells Python the line of code is connected to the line above it. There must always be atleast one line indented after the while statement. For loops follow this same syntax.", width=75)
    print
    print "================================================================================" 
  

def q3():
    print
    print   
    print textwrap.fill("Let's set up an exercise for you to write your own while loop. For this exercise, say that you want take a vacation that will cost $300. In order to save up enough money to take the vacation you've decided to set aside $75 per month. Write a loop to see how many months it will take for you to have enough money saved to take the vacation.", width=75)
    print
    print textwrap.fill("Simply start by creating a variable named 'balance' and setting it to 0 because you start with no money saved.",  width=75)
    
    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer.replace(" ", "") == "balance=0":
            print 
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break 
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \nbalance = 0"
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
                print "Not quite what I'm looking for.\nType balance = 0 and press Enter"
    global balance
    balance = 0


def q4():
    print
    print   
    print textwrap.fill("Next write a while loop that will loop while the balance is less than/equal to 300. In the body, write a statement to print the balance and another statement that will increment the balance by 75. So you should have total of 3 lines, a while loop heading and two lines in the body that. Remember the while loop heading ends with a colon (:). At the end of the indented body, execution returns to the while loop heading for another test until it is false.", width=75)
    print
    
    tries = 0
    while True:
        answer1 = raw_input(">>> ")
        if answer1 == "skip()":
            print
            print "Skipping question...the correct input was: \nwhile balance <= 300:\n     print balance\n     balance += 75"
            print
            print "================================================================================"
            break
        elif answer1 == "main()":
            print "Quitting tutorial & returning to main menu\n"
            global mainflag
            mainflag = 1
            break       
        else:
            answer2 = raw_input("      ")
            answer3 = raw_input("      ")
            if     (answer1.lower() == "while balance <= 300:"
                and answer2.lower() == "print balance"
                and answer3.lower() == "balance += 75"):
                print 
                balance = 0
                while balance <= 300:
                    print balance
                    balance += 75
                print
                print "================================================================================"
                break 
            else:
                tries = tries + 1
                if tries < 3:
                    print textwrap.fill("The syntax checker is picky on how this is typed in...a few things that may be wrong: check spacing & ensure the while heading (first line) ends with a colon.", width=75)
                elif tries >= 3:
                    print "Type the following and press Enter:\nwhile balance <= 300:\n     print balance\n     balance += 75"

def q5():
    print
    print
    print textwrap.fill("In the example above, first the initial balance is printed out, then $75 is added to the balance, and the execution is returned to the while condition to check to see if it is still true. While it's true it prints out the balance and adds another 75. Once the balance hits 300, the loop stops executing. After 4 months you will have enough money to take your vacation.", width=75)
    print
    print "================================================================================"
     

def q6():
    print
    print
    print textwrap.fill("IMPORTANT NOTE: when using while loops ensure that you have included a way to stop running the loop or else the loop will continue indefinitely. This accidently happens to every programmer occasionally. If you get stuck in an infinite loop, press CTRL-c to abort (some editors have an embedded output window, which can make it difficult to stop an infinite loop and you may have to close the editor to end the loop). Review your while statement(s) and make sure that the condition will be False at some point in order to avoid indefinite loops. If you're unsure, try printing out the test variable at the top and bottom of the while loop so you can observe what it's doing.", width=75)
    print
    print "================================================================================"
    
    
    
def q7():
    print
    print
    print textwrap.fill("A for loop executes a block of code once for each item in a collection. You may hear this described as iterating over a set or sequence of values. Iterating simply means looping.", width=75)
    print
    print textwrap.fill("Let's say we have a list of states, and we want to print out each state in the list. We could retrieve each item in the list individually, but this is repetitive when there is a long list of items and the code would need to be modified if the list's length changed. A for loop is much cleaner.", width=75)
    print
    print
    print ">>> states = ['florida', 'texas', 'tennessee']"
    print ">>> for state in states:"
    print "        print state"
    states = ['florida', 'texas', 'tennessee']
    for state in states:
        print state
    print
    print "================================================================================" 
  

def q8():
    print
    print
    print textwrap.fill("In the for loop above, first we define a list of states. Then the for loop statement tells Python to pull a value from the list states and store it in the variable state. The first value is 'florida'. Then Python moves to the next line, which tells it to print the item that was just stored in the variable state, so in this case 'florida'. Because there are more values in the list, Python returns to the first line of the loop and retrieves the next state in the list and stores that value in state, then it moves to the next line and prints out that value, which is now 'texas'. Python repeats the entire loop for each item in the list of states. After the loop is executed for the last value, in this case 'tennessee', Python moves on to the next line in the program because it recognizes there are no more values in the list. In our case, there is no Python code after the loop so the program ends.", width=75)
    print
    print textwrap.fill("In this example, the temporary variable was named state, but this could have been named anything you like. Best practice is to choose a name that best describes a single item from the list. So it is common practice to use singular names for the single item from a list and plural names for the entire list. ", width=75)
    print    
    print textwrap.fill("The loop will be repeated no matter how many items are in the list.", width=75)
    print
    print "================================================================================"
    
    
def q9():
    print
    print
    print textwrap.fill("I want you to try creating a for loop. We will keep it very similar to the one we just did. I will go ahead and create a list for you, named numbers.", width=75)
    print
    print
    print ">>> numbers = [1, 2, 3, 4]"
    numbers = [1, 2, 3, 4]
    print
    print
    print textwrap.fill("Now I want you to write a for loop that iterates through the list and prints out each value. For this exercise, please name the temporary variable number.", width=75)
    print
    
    tries = 0
    while True:
        answer1 = raw_input(">>> ")
        if answer1 == "skip()":
            print
            print "Skipping question...the correct input was: \nfor number in numbers:\n     print number"
            print
            print "================================================================================"
            break
        elif answer1 == "main()":
            print "Quitting tutorial & returning to main menu\n"
            global mainflag
            mainflag = 1
            break       
        else:
            answer2 = raw_input("      ")
            if     (answer1.lower() == "for number in numbers:"
                and answer2.lower() == "print number"):
                print 
                for number in numbers:
                    print number
                print
                print "================================================================================"
                break 
            else:
                tries = tries + 1
                if tries < 3:
                    print
                    print textwrap.fill("The syntax checker is picky on how this is typed in...a few things that may be wrong: check spacing & ensure the first line ends with a colon.", width=75)
                elif tries >= 3:
                    print "Type the following and press Enter:\nfor number in numbers:\n     print number"


def q10():
    print
    print
    print textwrap.fill("You can also iterate over dictionaries.", width=75)
    print
    print textwrap.fill("Remember from the dictionary tutorial that we can use the dictionary method items() to return a list of the pairs (key, value)", width=75)
    print
    print
    print ">>> d = {'bob': 45, 'sarah': 32, 'jake': 14}"
    print ">>> for key, value in d.items():"
    print "        print key, 'is ', value, 'years old'"
    global d    
    d = {'bob': 45, 'sarah': 32, 'jake': 14}
    for key, value in d.items():
        print key, 'is', value, 'years old'
    print
    print "================================================================================" 
    
    
def q11():
    print
    print
    print textwrap.fill("In the example above, first we define a dictionary with a few people's names and their ages. The for loop statement tells Python to pull a key and a value from a pair in the dictionary and store the key in the variable key and the value in the variable value. Again, these temporary variables can be named anything, but with dictionaries remember that the items() method returns the key first, followed by the value. Then in the second line we compose a message that prints the person's name and age in a sentence.", width=75)
    print
    print "================================================================================"  
    
    
def q12():
    print
    print
    print textwrap.fill("Indentation is very important when working with loops. Python uses indentation to know which lines of code are part of the loop. The line after the for statement in a loop must always be indented or Python will give you an error. Additional lines may also need to be indented depending on what you are intending to do in your loop.", width=75)
    print
    print "Let's compare two for loops that differ in the third line"
    print
    print "================================================================================"


def q13():
    print
    print
    print "for key, value in dict.items():"
    print "    print key, 'is ', value, 'years old'"
    print "    print 'Happy birthday', key"
    print
    for key, value in d.items():
        print key, 'is', value, 'years old'
        print 'Happy birthday', key
    print
    print
    print "for key, value in dict.items():"
    print "    print key, 'is ', value, 'years old'"
    print "print 'Happy birthday', key"
    print
    for key, value in d.items():
        print key, 'is', value, 'years old'
    print 'Happy birthday', key      
    print
    print "================================================================================" 


def q14():
    print
    print
    print textwrap.fill("In the second example, the print statement on the third line is not indented so Python does not see it as part of the loop. Since there was a line already indented after the for statement Python doesn't see this as an error. Because the second print statement is not indented, Python first executes the loop for each item in the dictionary, then after the loop is finished Python executes the second print statement. The final value stored in the variable is the one printed out in this statement.", width=75)
    print
    print "================================================================================"     
  
 
def q15():
    print
    print
    print textwrap.fill("Most of the time a loop executes until its condition becomes false or until it has iterated through all items in a sequence. However, there may be times when you want to change the normal sequence of execution and Python has loop control statements to do just that.", width=75)
    print
    print "Loop control statements include:"
    print "    - break statement"
    print "    - continue statement"
    print
    print "================================================================================"
    

def q16():
    print
    print    
    print textwrap.fill("The break statement ends the execution of a loop and moves execution to the statement following the loop.", width=75)
    print
    print "================================================================================"    
  
  
def q17():
    print
    print    
    print textwrap.fill("The continue statement causes the loop to skip the rest of its current iteration and move on to the beginning of the next iteration.", width=75)
    print
    print "================================================================================"     
  
 
def q18():
    print
    print    
    print textwrap.fill("Let's look at a simple example of the break statement.", width=75)
    print
    print
    print ">>> number = 0"
    print ">>> while number < 5:"
    print "        number += 1"
    print "        if number == 3:"
    print "            break"
    print "        print 'Current number:, number"
    print
    number = 0
    while number < 5:
        number += 1
        if number == 3:
            break
        print 'Current number:', number
    print
    print "================================================================================"
    
    
def q19():
    print
    print    
    print textwrap.fill("In the above example, the number begans as 0. We create a while statement that will loop as long as the number is less than 5. In the second line, we add 1 to the number during each iteration. However, we then add a condition that will break (end) the execution of the loop if the number equals 3. Finally we add a print statement to see the current number at the end of each iteration.", width=75)
    print 
    print textwrap.fill("Notice from this example that you can add if conditions inside of loops. You can also add else clauses.", width=75)
    print  
    print "================================================================================"    
   
def q20():
    print
    print    
    print textwrap.fill("The continue statement is used less often than break. In the example above, we can replace the break statement with a continue statement to check out the difference.", width=75)
    print
    print
    print ">>> number = 0"
    print ">>> while number < 5:"
    print "        number += 1"
    print "        if number == 3:"
    print "            continue"
    print "        print 'Current number:, number"
    print
    number = 0
    while number < 5:
        number += 1
        if number == 3:
            continue
        print 'Current number:', number
    print
    print "================================================================================"  
    
    
def q21():
    print
    print    
    print textwrap.fill("In the iteration where number = 3, the rest of the statements in the loop are skipped and moves the execution back to the beginning of the loop.", width=75)
    print 
    print "================================================================================"       
    
    
def conclusion():
    print
    print
    print textwrap.fill("Congratulations! You've reached the end of this tutorial. The purpose of this lesson was to provide you with a basic knowledge of loops in Python. You can use a while loop to continue executing it while a condition is true or you can use a for loop to iterate through a sequence of items and execute a block of code once for each item.", width=75)
    print
    print textwrap.fill("A while loop is very flexible and can be used to repeat a block of code for as long as a condition is true. However, they can be more difficult to get right so if you can use a for loop rather than a while loop you probably should. For loops can be customized for specific needs. To end the execution of a loop use a break statement. To skip the rest of the code block in a loop and continue with the next iteration use the continue statement.", length=75)
    print
    print textwrap.fill("People often find loops in Python to be tricky at first. Remember to include the colon at the end of a while/for statement to tell Python to interpret the next line as the start of a loop.", width=75)   
    


def loops():
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
        q20() 
        
        
    if mainflag != 1:
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        q21() 
        
        
    if mainflag != 1:     
        print
        raw_input("Press Enter to continue...")
        print
        print "================================================================================"
        conclusion()       
        print
        print "================================================================================"
        print
