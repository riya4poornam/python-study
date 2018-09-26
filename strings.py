#!/usr/bin/env python
#greeting = 'Hello Good Morning'
#print greeting 

#num = 13
#print num * 5
'''
# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
  # +++your code here+++
  return
'''


s = 'spring'

def both_ends(s):
  '''
  first = s[0:2]
  last = s[-2:]
  print first + last
  #return
  '''
  if (len(s) >= 2):
    return s[0:2]+s[-2:]
  else:
    return ''

print both_ends(s)
