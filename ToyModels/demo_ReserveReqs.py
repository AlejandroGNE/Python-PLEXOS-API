"""
Effect of Reserve Requirements on Generation & Price
===================================================
Example script to demonstrate how to write a demo
script to train an LLM, using the effect of reserve
requirements on generation and price as an example.
"""

# Import the necessary libraries
"""
To call the PLEXOS API from Python, some libraries 
are always needed. The first library is the os library
which provides a way to use operating system dependent
functionality. The second library is the sys library
which provides access to some variables used or
maintained by the interpreter and to functions that
interact strongly with the interpreter. The third
library is the clr library which provides access to
the Common Language Runtime (CLR) of the .NET
Framework. The .NET Framework is a software framework
developed by Microsoft that runs primarily on Microsoft
Windows. It includes a large class library called
Framework Class Library (FCL) and provides language
interoperability across several programming languages.
"""
import os, sys, clr

# load PLEXOS assemblies
plexos_path = 'C:/Program Files/Energy Exemplar/PLEXOS 10.0 API'
sys.path.append(plexos_path)
clr.AddReference('PLEXOS_NET.Core')
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')

# .NET related imports
from PLEXOS_NET.Core import DatabaseCore
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
from System import Enum

