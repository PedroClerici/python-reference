"""
Scopes and the "global" keyword
"""
var = 'some value'

def func():
    var = 'another value'
    print(var)

func()

# Changing global variables inside function scopes:
def func2():
    global var
    var = 3

func2()
print(var)
