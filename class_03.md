## class 3: Thursday, July 13
Reading: Visualizing Data

Makeup:
* Thursday, July 20

Facilitator: Dan

# Reading: Chapter 3 - Visualizing Data

This chapter is an introduction to the matplotlib library, which we will be using to create charts throughout the rest of the book and the rest of our lives. 

matplotlib requires one extra step to run smoothly in jupyter -- after you import matplotlib, you need to write a second line to run it "inline". Here's what it will look like:

```python
import matplotlib as plt
%pylab inline
```

You'll get a warning about clobbering some variables in numpy, but just ignore that for now

# Your Assignment - Plot some data

Create a new jupyter notebook, and take some basic two variable data and make a plot it using ```plt.plot```

Follow Joel's example at the beginning of the chapter. 

Don't worry about getting a lot of data. Just make some up. 

Make sure plot is readable -- label the x and y axes, and give it a title. 
