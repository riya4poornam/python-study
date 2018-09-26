#!/usr/bin/env python
'''
# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
  # +++your code here+++
  return
'''

s = 'babble'

def fix_start(s):
    print s[0]+s[1:].replace(s[0], '*')

#fix_start(s)


if __name__ == '__main__':
    fix_start(s)
