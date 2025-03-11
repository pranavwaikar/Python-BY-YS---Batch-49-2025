
L = [True, 10, 3.14, "Hello"]
L[0]
# True
type(L[0])
# <class 'bool'>
type(L)
# <class 'list'>
L[1]
# 10
type(L[1])
# <class 'int'>
# L[2}
# SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
L[2]
# 3.14
type(L[2])
# <class 'float'>
L[3]
# 'Hello'
type(L[3])
# <class 'str'>
for x in L:
    type(x)

    
# <class 'bool'>
# <class 'int'>
# <class 'float'>
# <class 'str'>
L[0] = False
xyz=0
L[xyz] = False
# General Syntax of modification
# L[index] = new_value # 0 <= index < len(L)
# modifying all index using common formula
L[0]
# False
L
# [False, 10, 3.14, 'Hello']
i = 0
while i < len(L):
    L[i] = 500
    i+=1

    
L
# [500, 500, 500, 500]
dir(L)
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
