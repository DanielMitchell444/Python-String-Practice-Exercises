"""
Over the past week, we have been learning about strings and different methods
that you can use to slice strings. Today, we will start by reviewing 
what we have learned so far, as well as add a few more things on top of that
"""

"""
For a refresher, a string is basically text where you can hold sentences.
You can create a string using the following syntax
"""

string1 = "Hello"


"""
Now that is taken care of, its time to learn about slicing. The definition of
slicing is returning a range of characters. For example, lets use the string1
variable to demonstrate what we are talking about
If we go
"""

print(string1[2:5])

"""
This will essentially get all the characters from position or index two
of the string to index 4 of the string
I know you are probably asking yourself, wait, but it says 5?
Well, when slicing in Python, the 2nd position or the last position specified
is not included. Meaning that we do not include 5 in the range of characters
selected.

An important note is that the first character has an index of 0
"""

"""
PRACTICE:
Using what we just learned, i want you to create s string with whatever
text you want inside it. Then, i want you to get the first 3 characters
of the string and print it to the console.
Please type the code below this comment
"""

"""
Now, lets say you want to get the characters from the start position 0
and up to 4, well theres an easier syntax to use then to just go 0 to 5
We can go
"""

print(string1[:5])

"""
This is essentially telling the compiler to get the first 4 positions of
a string up to 4. Remember that 5 is not included, so when we print the 
string, it would not show up
"""

"""
PRACTICE:
Using the variable you most recently created, i want you to get the first
3 positions of your string variable using the syntax above
Please type the code below this comment
"""

"""
You can also do something similar if you want to get the indexs or
positions from a position in the middle of the string to the end
For example, lets say we want to get the string positions or indexes
from position 2 and we also want to get the rest of the string.
In this example, we could go
"""

print(string1[2:])

"""
This would essentially just get all the strings from position
2 to the end of the string.
"""

"""
Practice:
Using the syntax above, and using the variable you just created,
i want you to select the entire string, starting from position 1,
and then the rest.
Please type the code in the comment below.
"""

"""
There is also negative indexing with strings. Negative slices can start the
slice from the end of the string
so essentially, lets create another string variable and show you
"""

string8 = "Hello World!"

"""
Using negative slices, we can get the values from -5 to -2 like so
"""

print(string8[-5:-2])

"""
This would start the from the end of the string and count backwards from it,
so it would essentially get us orl. Negative indexing can be confusing
but it is an essential tool to programming.
"""

"""
PRACTICE:
Create a variable named x with whatever text you want inside it, and then
get the indexes -4 to -2 using the syntax listed above
"""

"""
Another useful method is the replace method. Basically, the replace
method replaces a string with another string. For example, lets
say we have a string variable like so
"""

string5 = "Hello World"

"""
We could essentially replace the H and the W in Hello World by doing 
something like this
"""

string5.replace('H', "J")

"""
The new string would replace j with h and print out Jello World
in this instance, the first argument is the letter you want to replace
followed by a comma, followed by the character you want to put in.
"""

"""
PRACTICE:
Using the variable you created above, i want you to replace the first
position of that string to the letter P
Please type the code below this comment
"""

"""
Another useful method is split, the split method returns a list where
the text between the specified seperator becomes the list items
So, lets say we want to make a list seperated by commas.
First, we would have to make a variable, luckily, we already did that
in string 5, so we have that step down
next we will have to select string5 and use the .split method,
we can do this like so, we can also visually see what happens if 
we print it out like so
first lets create the variable
"""
a = "Hello, World!"

"""
Then, we can use the split method to split it into two index like so
"""
b = a.split(',')

"""
And then if we print it, it'll look like this
"""

print(b)


"""
This method can be incredibly useful when you want to split characters
"""

"""
PRACTICE:
For this exercise, i want you to create a variable similar to the variable
above. For reference, the variable above looked similar to this
"""

string7 = "Hello, Neighbor"

"""
After you do this, i want you to use the split method to turn the string variable
into a list. Then, i want you to print out the newly created list.
"""


"""
Len is another useful method to use with strings
len is used to return the number of characters in a string
the syntax is as follows
"""

x = len(string7)


"""
The return method is something that we haven't talked about yet, but
it is essential in programming
a return statement is used to end the execution of the function call and
returns the results to the caller. Lets say we have a function named sayName,
and we use the return statement to return hello and name, we could do this like
so
"""

def sayName(name):
    return "Hello" + name

"""
Essentially we are just passing the name variable as a parameter
and then returning hello + whatever name argument the user decides to pass
so, lets say we want to call this function, we could do this like so
"""

print(sayName("Daniel"))

"""
When we call a function, inside the parenthesis, we call that a function argument
that is essentially what we are passing inside the sayName function.
"""
