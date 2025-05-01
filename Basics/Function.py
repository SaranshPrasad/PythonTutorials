def func():
    print("Hellow Saransh")

def sum(a,b):
    return a+b

# Passing function as an argument with *args
def fun(func, *args):
    return func(*args)

# *args -> this keyword allows a variable number of arguments passed in the function.  Used when we dont know the actual amount of arguments we recieve in a function. Here *args contains 2 arguments 2 - 4 which is then passed to func using same *args keyword

# **kwargs is used to pass a variable number of keyword arguments to a function. The ** syntax collects the keyword arguments into a dictionary, where the keys are the argument names and the values are the corresponding argument values. This allows the function to accept any number of named (keyword) arguments.

# k is the keyword and value is the values of kwargs containing here we are extracting 2 data from kwargs one is k -> key and val -> value as our arguments passin in function is in key value. items() is a function used to iterate over key-value paris of dictionary.
def dic(**kwargs):
    for k, val in kwargs.items():
        print(f"{k} : {val}")

def demo(*a, **k):
    print("Positional Arguments : ", a)
    print("Keyword Arguments : ", k)


demo(1,2,3,4,5, a=1,b=2,c=3)

#lambda function

cube = lambda x: x*x*x
print(cube(2))

#Use lambda function to check whether a given number is Negative or Postitive

s = lambda x:"Positive" if x > 0 else "Negative"
print(s(0))
func()
print(sum(1,2))
print(fun(sum, 2,4))
dic(name="Saransh", age=20, city="Ranchi")