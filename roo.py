# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 10:15:23 2016

Author: Amber Zaratsian
"""


from tutorials import tutorial_1_basic_syntax, tutorial_2_var_types_and_basic_operations, tutorial_3_lists, tutorial_4_tuples, tutorial_5_dictionaries, tutorial_6_loops
import textwrap

print
print
print "###############################################################################"
print "#                                                                             #"
print "#        IMPORTANT NOTE: This tutorial program follows Python 2 syntax        #"
print "#                                                                             #"
print "###############################################################################"
print
print
print "Ready to start?? Ok! Let's begin!"


def menu():
    print
    print
    name = raw_input("What is your name? ")

    print
    print
    print "Welcome " + name +"!"
    print
    print textwrap.fill('When you see "Press Enter to continue..." simply press the Enter button when you have finished reading and are ready to proceed.', width=75)
    print
    print "================================================================================"
    print
    raw_input("Press Enter to continue...")
    print
    print "================================================================================"
    print
    print textwrap.fill("When you see the prompt >>> type your response to the question and press Enter. A message will then tell you if your answer is correct or if incorrect it will ask you to try again and prompt you to enter another response.", width=75)
    print
    print "================================================================================"
    print
    raw_input("Press Enter to continue...")
    print
    print "================================================================================"
    print
    print "When you are at the prompt >>>:"
    print "   - Typing skip() allows you to move past the current question."
    print "   - Typing main() will quit the tutorial & return back to the main menu."
    #print "   - Typing exit() while at the main menu will exit the entire program."
    print
    print "================================================================================"
    print
    raw_input("Press Enter to continue...")
    print
    print "================================================================================"

    menulist = """
    Main Menu:
    ------------

    1.Basic Syntax
    2.Variable Types & Basic Operations
    3.Lists
    4.Tuples
    5.Dictionaries
    6.Loops
    7.Functions (Coming soon!)

    To exit, type exit()
    """

    print menulist
    print "\nPlease select a tutorial from the menu above by typing in the number."


    def selection():
        while True:
            answer = raw_input(">>> ")
            if answer == '1':
                print
                print 'You selected 1.Basic Syntax'
                tutorial_1_basic_syntax.basic_syntax()
                print menulist
            elif answer == '2':
                print
                print 'You selected 2.Variable Types & Basic Operations'
                tutorial_2_var_types_and_basic_operations.basics()
                print menulist
            elif answer == '3':
                print
                print 'You selected 3.Lists'
                tutorial_3_lists.lists()
                print menulist
            elif answer == '4':
                print
                print 'You selected 4.Tuples'
                tutorial_4_tuples.tuples()
                print menulist
            elif answer == '5':
                print
                print 'You selected 5.Dictionaries'
                tutorial_5_dictionaries.dictionaries()
                print menulist
            elif answer == '6':
                print
                print 'You selected 6.Loops'
                tutorial_6_loops.loops()
                print menulist
            elif answer == '7':
                print
                print 'Functions tutorial coming soon! Select a different tutorial'
                #print 'You selected 7.Functoins'
                #tutorial_7_functions.functions()
                #print menulist
            elif answer == 'exit()':
                print
                print 'Farewell ' + name + '! Exiting Python tutorial...please come back soon!'
                print
                print "================================================================================"
                break
            else:
                print 'Not a valid choice...please try again.\nFor example, if you want to start the tutorial "Lists" enter 1\nEnter exit() to exit program'

    selection()

menu()
