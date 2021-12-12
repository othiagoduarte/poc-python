# This program add up integer that have beepassed as arguments in the command line
import sys

try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print ('sum =', total)
    print ('all args',sys.argv[1:])
except ValueError:
    print ('please supply integer arguments')