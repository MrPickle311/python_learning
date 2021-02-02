import sys,math,operator
from tkinter import Button,mainloop
from functools import  reduce
#rekurencja

def sum(L):
    if not L:
        return 0
    else: return L[0] + sum(L[1:])
L = [1,2,3]
print(sum(L))

#rekurencja pośrednia
def forward(first,rest):
    print('Actual element is : ' ,first)
    return first if not rest else first + mysum(rest)

def mysum(L):
    return forward(L[0],L[1:])
print(mysum(L))

def prntTree(L,inj):
    if not L: return
    for e in L:
        if isinstance(e,list):
            prntTree(e,inj + '---')
        else: print(inj,e)
L = [1,[2,3,[7,8]],4]
prntTree(L,'')

print(sys.getrecursionlimit()) # podglad maksymalnej liczby wywołań rekursywnych
sys.setrecursionlimit(10000) #ustawienie maksymalnej liczby wywołań rekursywnych

#Introspekcja funkcji
#607

#artrybuty funkcji ,czyli lepsze stany funkcji 

def f():
    f.attr1 += 30
    pass
print(dir(f)) # pokazuje wszystkie wbudowane artrybuty
print(str(f.__class__))
print(str(f.__hash__))

f.attr1 = 2
f.attr2 = 3
f.attr2 += 5
f.attr1 += 1
print(f.attr2,f.attr1)
f()
print(f.attr2,f.attr1)

print(len(dir(f)))

#dodawanie adnotacji , tam mogą być podane tylko nazwy typów

def func2(a : 'str',b : 'list' = []) -> int:
    print(a,b)
func2(5)

print(func2.__annotations__,func2.__class__)
for x in func2.__annotations__:
    print(x)

#lambda

f = lambda L : sum(L) + len(L)
print(f([1,2,3]))

def func3():
    x = "xd"
    return lambda y: print(x,y) #lambdy obowiązuję takie same prawa zasięgowe ,co funkcje
k = func3()
k('XD')

#wykorzystanie lambd jako tablic skoków,czyli tablic operacji
L = [lambda x: x**2,
     lambda x: math.sqrt(x),
     lambda x: x + 10
    ]

for x in L:
    print(x(3))

#wsadzenie lambd do słownika
D = {"power" : lambda x: x**2,"sqrt" : lambda x: math.sqrt(x),"plus 10" : lambda x: x + 10}

for what in D:
    print("Operation of 5",what,'equals :',D[what](5))

#w lambdach można umieszać jednowierszowe ify oraz pętle

t = lambda a,b:  a if a % b == 0 else b
u = lambda L:  [x**2 for x in L] 
L = u([1,2,3,4])
print(L)

#zagnieżdżanie lambd
weirdo = lambda x: lambda y: x + y
internal = weirdo(5)
print(internal(10))

#fajny przycisk
#x = Button(
#    text="Push me",
#    command=lambda : sys.stdout.write("HELLOO BUTTON")
#)
#x.pack()
#mainloop()

#przekazywanie własnych funkcji do map

def inc(x) : return x + 10
L = [1,2,3,4]
print(list(map(inc,L)))
#załadowanie lambdy do map
print(list(map(lambda x: x**2,L)))

#map potrafi obsłużyć równolegle kilka sekwencji

print(list(map(pow,[1,2,3],[4,5,6])))

#funkcja filter , filture nam obiekt iterowalny

L = range(-5,5)
print(list(filter(lambda x: x < 0,L)))

#reduce ,coś jak std::accumulate
#dodatkowo przedsawiam jeden z predefiniowanych operatorów-lambd 
print(reduce(lambda x,y: x / y,[1,2,3,4]))
print(reduce(operator.add,[1,2,3,4]))


