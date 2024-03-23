"""
This module contains add,substract,
multiply,divide and percentage
"""
def add(a,b):
    """
    This is add function sub(a,b)
    returns the value a+b
    """
    return a+b

def sub(a,b):
    """
    This is substract function sub(a,b)
    returns the value a-b
    """

    if (a >= 0 and b >= 0):
        if a>b:
            return a-b
        else:
            return b-a
        
    else:
        return "values must be greater than 0"
    

def multiply(a,b):
    """
    This function multiply a and b 
    and return a*b
    """
    return a*b


def div(a,b):
    """
    This function divide a and b 
    and return a/b
    """
    if(a>0 and b>0):
        return a/b
    else:
        return "values must be greater than 0"

def percent(a,b):
    """
    This function find percentage of a based on b 
    and return a%
    """
    per=(a/b)*100
    return per