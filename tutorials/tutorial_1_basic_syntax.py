# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 13:53:28 2016

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
    print textwrap.fill("This is a short tutorial on basic syntax in Python and some best practices. This tutorial is mainly informative rather than hands on like the others.", width=75)
    print
    print "================================================================================"


def q1():
    print
    print
    print "Let's began by you typing the following text when you see the prompt:"
    print 'print "Hello World"'

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer == 'print "Hello World"' or answer == "print 'Hello World'":
            print "Hello World"
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break
        elif answer == "skip()":
            print
            print 'Skipping question...the correct input was: print "Hello World"'
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
                print """Not quite what I'm looking for.\nType print "Hello World" and press Enter"""


def q2():
    print
    print
    print textwrap.fill("""In Python, you can use double ("") or single ('') quotes to specify a string, as long as the same type of quote is used for the beginning and the ending of a string. This allows flexibility for using quotes & apostrophes within your strings.""", width=75)
    print textwrap.fill("Triple quotes ('''" 'or """) can be used for strings that span across multiple lines.', width=75)
    print
    print "Here are some examples, all which are allowed in Python:"
    print
    print ">>> string1 = 'hey'"
    print '>>> string2 = "Multiple words in a sentance"'
    print '>>> string3 = """A paragraph that is made up of\n\tmultiple lines"""'
    print
    print "================================================================================"


def q3():
    print
    print
    print textwrap.fill("There are a few rules that you should follow when naming variables in Python. Variable names can start with a letter or an underscore. They can contain letters, numbers, & underscores. Spaces are not allowed in variable names. Python is case sensitive, for example speed and Speed would be two different variables.", width=75)
    print
    print "There are some reserved words in Python that cannot be used as a variable name:"
    print """\tand, assert, break, class, continue, def, del, elif, else,\n\texcept, exec, finally, for, from, global, if, import, in,\n\tis, lambda, not, or, pass, print, raise, return, try, while"""
    print
    print "================================================================================"


def q4():
    print
    print
    print textwrap.fill("Comments can be used in Python to create notes to explain what your code is doing or any other helpful information. Simply add a hash mark (#) in front of text to make it a comment and anything following the hash mark to the end of the line will be ignored by the Python interpreter.", width=75)
    print
    print "Try typing in the following comment:"
    print "# An ignored comment"

    tries = 0
    while True:
        answer = raw_input(">>> ")
        if answer == "# An ignored comment":
            print "# An ignored comment"
            print
            print feedback.correct[random.randint(0, len(feedback.correct)-1)]
            print
            print "================================================================================"
            break
        elif answer == "skip()":
            print
            print "Skipping question...the correct input was: \n# An ignored comment"
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
                print "Not quite what I'm looking for.\nType # An ignored comment and press Enter"


def q5():
    print
    print
    print textwrap.fill("Multi-line comments can also be created by enclosing the comment in triple double-qoutes.", width=75)
    print "For example:"
    print
    print '"""'
    print "This is a block of text which will be ignored."
    print "These comments are intended as documentation for anyone reading the code"
    print '"""'
    print
    print "================================================================================"


def q6():
    print
    print
    print textwrap.fill("Python does not use curly braces or explicit keywords like `begin` or `end` to mark where the code starts and stops. Rather, the only delimiter is a colon (:) and line indentation of the code.", width=75)
    print
    print textwrap.fill("""Code blocks are denoted by line indentation, which is strictly enforced in Python. A "code block" is a function: `if` statements, `for` loops, `while` loops, etc.""", width=75)
    print
    print textwrap.fill("The amount of spacing is not relevant, it just needs to be consistent. Indenting a line starts a block and unindenting ends it. So the first line with less indentation is outside the code block and the first line with more indentation starts a nested code block.", width=75)
    print
    print textwrap.fill("A colon often appears at the start of a new block (ex. for function and class definitions).", width=75)
    print
    print "================================================================================"




def q7():
    print
    print
    print textwrap.fill("Here's an example of an `if` statement with proper code indentation. Note: Functions will be explained later so you do not need to know what is going on in this code for now. This is just intended to show you best practice for writing code in Python. As we move through the tutorials we will try to follow these practices in examples.", width=75)
    print
    print
    print "def sumExample(a=4, b=7):"
    print "   if a + b < 10:"
    print "      print print 'less than'"
    print "   else:"
    print "      print 'greater than'"
    print "      return a + b"
    print
    print
    print textwrap.fill("Line 1: This is a function named sumExample that takes two arguments, a and b. All code within a function is indented", width=75)
    print textwrap.fill("Line 2: if statements are a type of code block.", width=75)
    print textwrap.fill("line 3: if the if statement is true then this code block is executed, otherwise it moves to the else block (line 4 in this case).", width=75)
    print textwrap.fill("Line 5 & 6: if and else blocks can contain multiple lines as long as the indentation is consistent.", width=75)
    print
    print "================================================================================"


def q8():
    print
    print
    print textwrap.fill("Indentation is ignored when using implicit and explicit continuation lines.", width=75)
    print
    print "Line continuation can be done in two ways:\n   - wrapping expressions in brackets [], {}, or () \n   - backslash to break the line prematurely"
    print
    print ">>> animals = (\n    'dog',\n    'cat',\n    'horse'\n    )"
    animals = (
               'dog',
               'cat',
               'horse'
               )
    print
    print ">>> print animals"
    print animals
    print
    print
    print ">>> sentence = 'Today I went ' \ \n               'to the store ' \ \n               'to buy groceries'"
    sentence = 'Today I went ' \
               'to the store ' \
               'to buy groceries'
    print
    print ">>> print sentence"
    print sentence
    print
    print "================================================================================"


def q9():
    print
    print
    print textwrap.fill(r"Whitespace can be added to make your output easier to read. Whitespace refers to any nonprinting character, such as spaces, tabs, and returns. To add a tab to your text, insert \t before the text you want indented. To add a newline, insert \n before the desired line break.", width=75)
    print
    print "For example, we can print a list with each item on a new line by doing:"
    print
    print r'>>> print "Food:\nPizza\nBurger\nSteak"'
    print "Food:\nPizza\nBurger\nSteak"
    print
    print "You can also combine tabs and newlines together:"
    print
    print r'>>> print "Food:\n\tPizza\n\tBurger\n\tSteak"'
    print "Food:\n\tPizza\n\tBurger\n\tSteak"
    print
    print "================================================================================"


def q10():
    print
    print
    print textwrap.fill("Multiple statements can be made on a single line using the semicolon (;), as long as none of the statements start a new code block.", width=75)
    print
    print "x = 'word'; print x"
    print
    print "This is not often used in coding because it is not as readable."
    print
    print "================================================================================"


def q11():
    print
    print
    print textwrap.fill("PEP 8 is a style guide for Python code that I highly recommend anyone learning the language to read (https://www.python.org/dev/peps/pep-0008/). This is part of the Python Enhancement Proposals (PEPs) which describe changes to Python or the standards around the language.", width=75)
    print
    print textwrap.fill("Even though line indentation is not required to be consistent, it's best practice to keep it consistent.", width=75)
    print
    print textwrap.fill("""Use parentheses over backslashes when possible, according to PEP 8, 'The preferred way of wrapping long lines is by using Python's implied line continuation inside parentheses, brackets, and braces. Long lines can be broken over multiple lines by wrapping expression in parentheses. These should be used in preference to using a backslash for line continuation'.""", width=75)
    print
    print "================================================================================"


def q12():
    print
    print
    print textwrap.fill("Recommended style is to break lines before binary operators, although it is permissible to break before or after a binary operator as long as the convention stays consistent throughout your code.", width=75)
    print
    print """Example:
    net_pay = (gross_pay
               + bonus
               - taxes
               - ira_deduction
               - insurance)"""
    print
    print "================================================================================"


def conclusion():
    print
    print
    print textwrap.fill("End of tutorial. I know this was not the most exciting tutorial, but it's important to understand the Python syntax and be aware of best practices. This is especially important when you are sharing your code with others.", width=75)



def basic_syntax():
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
        conclusion()
        print
        print "================================================================================"
        print
