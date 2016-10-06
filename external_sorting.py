"""
pip install --user psutil

import sys

"""

"""
with open(file_name) as f:
    for line in f:
        <do something with line>
"""


def getObjectSize(x):
  return sys.getSizeOf(x)


print getObjectSize("abc")



# First step. Get available memory in the system (with an offset)

# Second step. Open input file

# Third step, read first line and calculate size in memory

# Chunk lines into groups of M

# Loop. Until chunk size is maximized:

###   Sort M

###   Create new File f

###   Dump sorted(M) to file f

###   Close file f

# Read generated files

# Read a line from each one, decide which is the first and dump to disk



