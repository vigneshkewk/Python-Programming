#!/usr/bin/env python
# coding: utf-8

# ## Function -
# - Expression which takes input and returns output
# - can i define it?
# - yes i can define it by using keyword "def function_name"
# - once we define it can we access it
# - yes we can access it it is called "calling a function"
# 
# ## return only shows o/p in jupyter notebook, but not in vs code or linux cli
# ## #always store func in varible good practice

# ## advantages of functions-
# 
# - we can a function from ny location(path)
# - enhances better readability
# - code is structured

# In[51]:


def welcome():
    print("hello world")
welcome()


# In[52]:


# f(x) = 3x^2 + 4x + 5
def my_exp(x):
    #print(x,"this is my output")                   debuging step
    #print(type(x),"this is the data type")          debugging step
    print(3*x**2 + 4*x +5)
my_exp(4)


# In[53]:


def exp2(x,y):
    add = x+y
    return add
# exp2(45,5) # only shows o/p in jupyer bcz we used return
my_ans = exp2(45,5)  # to overcome this in vs code or linux cli we use a new variable to store it and print it
print(my_ans)


# In[54]:


def tes(x):
    y=x+2
    return y
#tes(5)# only shows o/p in jupyer bcz we used return
ans = tes(5) # to overcome this in vs code or linux cli we use a new variable to store it and print it
print(ans)


# ## Global and local variables
# - Global variabls are declared out of function and can be accessed anywhere in the code
# - local variables are declared inside the function and can only be accessed inside the function

# In[55]:


#local
def tes(x):
    y=x+2
    return y
#tes(5)# only shows o/p in jupyer bcz we used return
ans = tes(5) # to overcome this in vs code or linux cli we use a new variable to store it and print it
print(ans)
#print(y) # here we get error because y is alocal variable and cannot be accessed outside the function


# In[56]:


#global
my_global = 67
def addi(x,y):
    c = (x+y)*my_global # here we can access the global variable anywhere in the code
    return c
addi(1,1)


# In[57]:


#creating a function
# calling a function
#Arguments or parameters - positional , keywords
# number of arguments- *args,keyword_arguments,default
# return something/nothing
#pass
#recursion
#max min
#simple calculator
#ps combination of conditional statements and function
# special functions: zip,lambda,map,filter,reduce


# ### postional arguments

# In[58]:


#Arguments or parameters - positional , keywords are input values to the function
def addition(x,y):
    print(x,"this is my x input")
    print(y,"this is my  y input")
   
    c = x+y
    return c
print(addition(3,4))
print(addition(4,3))


# In[59]:


def my_division(x,y):
    z = x / y
    return z
print(my_division(2,3))
print(my_division(3,2))
# here the results change according to postions of the passed arguments


# In[60]:


def double_div(x,y):
    dd = x // y
    return dd
print(double_div(2,3))
print(double_div(3,2))

# here the results change according to postions of the passed arguments


# ### Keyword arguments

# In[61]:


def print_message(x="hello",y="world"):
    return x+y
# print_message("")  #NOTE
print_message()


# In[62]:


def print_message(x="a",y="b"):
    g = "hello Good morning"+ x+""+y
    return g
print_message()


# ### Default argument

# In[63]:


def sub(x,y=7):  # here 7 is the default value of argument y 
    f = x-y
    return f

subract = sub(1) #here even though we need to enter two args we can enter onl x as we have y=7 as default argument
print(subract)


# In[64]:


def welcome_message_1(x,y,z="Innomatics"):
    c = x+" "+y+" Welcome to "+" "+z
    return c
welcome_message_1("vignesh","atluri")


# ### # number of arguments- *args,keyword_arguments,default
# - *args are used when we donot know how many inputs we get in a function

# In[65]:


def infinite_args(*inputs):
    return inputs
infinite_args(1,2,3,4,5,6) #here we can add as many inputs as we need


# In[66]:


def infinite_args(*inputs):
    return inputs[1]# to get the output of value whose index is 2, we can also do slicing [2:4:-1] like that, it also has negative indexing
infinite_args(1,2,3,4,5,6) 


# In[67]:


def test(*details,age = 20):
    return (print("hello",details[0],details[1],age))  #we can add our args even afre *args
test("vignesh","atluri")

#or

# def test(*details):
#     return "hello"+ details[0]+ details[1]
# test("vignesh","atluri")




# ## keyword arguments: while creating the function, pass input as **args

# In[68]:


def smthng(**inputs):
    return inputs
d = smthng(A=1,B=2,C=3)
print(d)


# ## passing a data structure to the function

# In[69]:


#list
l1 = [-2,-1,0,1,2]
# problem statement:
def filtet_ds(x):
    for i in x:
        if i<0:
            print(i,'it is an negative number')
        else:
            print(i,"it is an positive number")
d = filtet_ds(l1)
print(d)


# ## return something/nothing

# In[70]:


def ran_fun(x):
    return None
d = ran_fun(1)
print(d)


# In[71]:


def ran_f1(x,y,z):

    return x,y,z

x1,x2,x3 =ran_f1("hello","good","morning")  # we can use indexing but not right approach
print(x1)
print(x2)  # we assign three diff variables instead of usin g indexing
print(x3)
print(x1,x3)


# In[72]:


def welc(a,b,c,d):
    return a,c  #we can return whatever the values we want
output1,output2 = welc("hello","world","im python","bye") #always store func in varible good practice
print(output1)
print(output2)


# #### we can a function from ny location(path)

# In[76]:


#we can a function from ny location(path) our file containing functiom must be in working directory(download as .py and store in working directory)
# from <file that consists function> import <funnction name> is the syntax to call the function in any other file
def call_add(x,y):
    z = x+y
    return z
def call_sub(x,y):
    z = x-y
    return z
print(call_add(1,2))
print(call_sub(3,4))


# In[74]:


# special functions: zip,lambda,map,filter,reduce






# In[ ]:




