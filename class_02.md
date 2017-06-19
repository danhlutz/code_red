## class 2: Thursday, June 29

Makeups:
* Thursday, June 22
* Thursday, July 6

Class facilitator: Dan L.

# Reading: Chapter 2 - *A Crash Course in Python*

This chapters covers basic Python data structures very quickly. You should type all of the code in this class into a Jupyter Notebook, and run it, to make sure you get it. 

If you have any trouble getting your code to run, talk to Dan. 

There is a lot to cover in this class, and we will have two make-ups. Feel free to attend as many of them as possible. 

# Assignment: my_name_stats.py

I want you to try to write a simple python function that asks for someone to enter their name, and then tells them a lot of **COOL, HIP** things about their name, like:
* How long is your name?
* What are the unique letters in the name?
* How many times do those letters appear?
* And if you're feeling really ambitious, is your name a **PALINDROME**?
* Maybe you have other cool features you'd love to add to this cool new app -- like telling someone the vowels that appear in their name. Your imagination is the limit here.

Here are some hints to get you started: 
* Use the python function raw_input to ask for the name. It works like this

```your_name = raw_input("What's your favorite color? ") ```

* The ```len``` function tells you how long a string is

* How about useing a ```Counter``` to tell you how many times the letters appear. You can also use a ```set``` to give you the unique values in a string. (And don't forget to use ```Counter``` you must ```import``` it ```from collections```

* It's a good idea to wrap up all your code in a function. A function defintion looks like this

```python
def my_name_stats():
    your
    code
    here
```

* Use the ```print``` function to spit out your results

* If you want to check if a string is a palindrome, talk to Dan about how to write a recursive function 

Please take a stab at this exercise after you've finished the reading. If you get stuck or have any problems, feel free to bring it up in class -- it will be helpful to work through the problems. 

# class agenda

* review my_name_stats -- who had errors? 

* side note on division in Python 2.7

* introduction to lists!
    * making a list
    * list indexing
    * list slicing
    * going thru a list and doing something to each item 

* getting a grounding in computer science: MIT OCW 6.00SC
