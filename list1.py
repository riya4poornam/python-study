#!/usr/bin/env python

'''
# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
  # +++your code here+++
  return
'''

words = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

def front_x(words):

    x_list = []
    other_words = []
    for i in words:
        if (i[0] == 'x'):
            x_list.append(i)
        else:
            other_words.append(i)
    x_list.sort()
    other_words.sort()
    print x_list + other_words
    

if __name__ == '__main__':
    front_x(words)
                                                                                                                                                                                         
