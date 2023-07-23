#temperature.py
"""module to convert temperature from
celcius to fahrenite and vise versa"""

#functions
def to_celcius(x):
    """returns: x converted to centigrate"""
    return 5*(x-32)/9.0

def to_fahren(x):
    """returns: x converted to fahrenite"""
    return 9*x/5.0+32

#constants
freezing_c=0.0
freezing_f=32.0
