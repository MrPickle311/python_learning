from collections.abc import Iterable
import math

def isString(element):
    if isinstance(element,str): return True

def isNumbersCollection(collection):
    for element in collection:
        if isString(element): return False
        if not str.isnumeric(str(element)): return False
    return True

def isStringsCollection(collection):
    for element in collection:
        if not isString(element): return False
    return True   

def addNumbers(collection):
    return sum(collection,0)

def joinStrings(collection):
    ret = ''
    for element in collection:
        ret.join(element)
    return ret

def convertTupleToList(T):
    return [(key,T[key]) for key in T.keys()]

def adder(*args,**kargs):
    L = [*args]
    if isStringsCollection(L):
        return joinStrings(L)
    if isNumbersCollection(L):
        return addNumbers(L)
    T = convertTupleToList(kargs)
    return L + T
    
def addDict(dict1,dict2):
    D = dict(dict1)
    D.update(dict2)
    return D

print(adder(1,2,"2323",[213,23]))
print(adder(1,2,"2323"))
print(adder(1,2,2323))
print(adder({2,3},2,'sdsa',name=5,xd='xd'))
print(addDict(dict(name='xd',srs=3),dict(name='xd')))

print(list(map(math.sqrt,[2,4,9,16,25,36])))