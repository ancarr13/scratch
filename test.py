'''
Introductory Python Coding Examples

created by Anthony Carroll github: @ancarr13

A few very thoroughly commented examples of basic python functionality such as creating and calling functions,
understanding inputs and outputs of functions,
defining variables, and using print statements,

The examples are very simple and redundant to built in python functionality,
with the intention of highlighting python syntax
'''


#example of a void function, a function which returns nothing
#input: str - string
#output:
#desc: prints the input string to the terminal
def print_me(str):
    print(str)
    return

#example of a function which returns something, in this case an int
#input: n1,n2 - integers
#output: n1+n2 - integer
#desc: returns the integer sum of two integer inputs
def plus(n1,n2):

    return(n1+n2)

#defining a variable
#using quotes around the content automatically makes this the variable type string
my_str = "Hello There"

#calling a defined function using our new variable
print_me(my_str)

#create some integers
a = 4
b = 8
c = plus(a,b)

#try an inline print statement
print(c)
