from collections import Counter

import time
from string import join


def remove_spaces(string):
    final = [char for char in string
             if char != ' ']
    return ('').join(final)


def is_palindrome(string):
    string = remove_spaces(string)
    if len(string) in [0, 1]:
        return True
    else:
        return string[0] == string[-1] and is_palindrome(string[1:-1])


def my_name_stats():
    print ("Prepare to have your mind blown ...")
    time.sleep(1.5)
    print ("Annoucing:")
    time.sleep(1.5)
    print ("MY_NAME_STATS")
    my_name = (raw_input("So, what's your name? ")).lower()
    print ("Thinking")
    time.sleep(1.5)
    print "The unique letters in your name are: ", sorted(set(my_name))
    print "The frequency of letters in your name is: ", Counter(my_name)
    print "Is your name a palindrome? ", is_palindrome(my_name)


my_name_stats()
