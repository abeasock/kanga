# kanga

**Requires Python 2.7**

Dependencies: 
The Python packages `textwrap` and `random` are used. These both are part of the standard library that comes installed with native Python.

## Description
kanga is Python package intended to teach a user Python programming interactively in a real Python environment by allowing the user to enter commands and providing feedback or retries for incorrect answers. 

## Warning
kanga was a project I was working on when I was starting to program in Python. I never had time to go back and improve it as I became a better developer. The inspiration for this project was from using the R library `Swirl` to learn R. While this package should currently work, please note it needs more attention and development.**

## Set up
The location that you save the kanga directory to must be added to the your Python path. For example, run this from Python:

	import sys
	sys.path.append('C:/Users/abeasock/Documents')

This should work in any IDE, but it was built in Spyder so that will provide the best results at render the outputs. Spyder is one of the IDEs included in the Anaconda install. Not tested in Jupyter.

Once your in the python console (and after adding the path):
	
	from kanga import roo
