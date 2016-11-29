#!/usr/bin/env python
#
# Test cases for tournament.py

from tournament import *

def testDeleteMatches():
    deleteMatches()
    print "1. Old matches can be deleted."

def testDelete():
deleteMatches()
deletePlayers()
print "2. Player records can be deleted."