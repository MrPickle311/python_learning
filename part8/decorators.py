# w pythonie istnieją dekoratory klas oraz funkcji
# Pośrednicy funkcji
# Dekoratory funkcji instalują obiekty opakowujące, przechwytujące późniejsze wywołania
# funkcji i odpowiednio je przetwarzające. Zazwyczaj wywołanie jest przekazywane do orygi-
# nalnej funkcji w celu wykonania zarządzanej operacji.
# Pośrednicy interfejsu
# Dekoratory klas instalują obiekty opakowujące, przechwytujące późniejsze wywołania two-
# rzące instancje i odpowiednio je przetwarzające. Zazwyczaj wywołanie jest przekazywane
# do oryginalnej klasy w celu utworzenia zarządzanej instancji.

# jak działa dekorator funkcji ? ano tak

# @dekorator
# def func(args): ...

# i jej wywolanie jest tak naprawde takie

# result = dekorator(func(args))

# implementacja za pomocą funkcji

import sys
import time


def decorator(F):
    print('Hello')
    # Przetworzenie funkcji F
    return F


@decorator
def func(a, b): return a*b


h = func(5, 6)
print(h)

# jak zwrócić jednak funkcje func , a nie jej wynik  ?
# z uzyciem klas


class decorator2:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):  # args i kwargs łapie nam argumenty wywołania funkcji
        print('Hello', *args, **kwargs)
        return self.func


@decorator2
def func2(a, b): return a*b


h = func2(2, 3)
print(h)
print(h(6, 7))

# dekorator metody klasy
# powyższe sposoby na dekoratory nie sprawdzą się dla metod klas


def decorator3(F):
    def wrapper(*args):
        print('Decorated!')
        F(*args)  # wykonuje funkcję lub metodę
    return wrapper


class C:
    @decorator3
    def method(self, x, y):
        print('Hello method!')
        return x*y


X = C()
h = X.method(6, 7)
print(h)

# dekoratory klas

# @decorator
# class C:
#     ...  # Udekorowanie klasy
# x = C(99)

# class C:
# ...
# C = decorator(C)
# x = C(99)

# dekorator przechwytujący wszystkie odwołania do
# nieistniejących artybutów instacji klasy


def decorator(cls):
    class Wrapper:

        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            print('Caught an attriute! , ', name)
            return getattr(self.wrapped, name)

    return Wrapper


@decorator
class D:
    def __init__(self, x, y):
        self.attr = 'spam'  # C = decorator(C)


# Wykonywane przez Wrapper.__init__
x = D(6, 7)
print(x.attr)

# zagnieżdzone dekoratory

# taki zapis dekoratorów
# @A
# @B
# @C
# def f(...):

# odpowiada temu

# def f(...):
# ...
# f = A(B(C(f)))


def d1(F): return lambda: 'X' + F()
def d2(F): return lambda: 'Y' + F()
def d3(F): return lambda: 'Z' + F()


@d1
@d2
@d3
def func1():
    return 'mielonka'


print(func1())

# artrybuty dekoratorów

# @decorator(A, B)
# def F(arg)


def F(arg): ...

# Ponowne dowiązanie F do wyniku wartości zwracanej przez dekorator
# F = decorator(A, B)(F)
# F(99)

# możliwość zachowywania wiadomości o stanie funkcji - wielokrotne wywoływanie dekorowanej funkcji

# - za pomocą atrybutów instacji klasy


class tracer:                                # State via instance attributes
    def __init__(self, func):                # On @ decorator
        self.calls = 0                       # Save func for later call
        self.func = func

    def __call__(self, *args, **kwargs):     # On call to original function
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


@tracer
def spam(a, b, c):          # Same as: spam = tracer(spam)
    print(a + b + c)        # Triggers tracer.__init__


@tracer
def eggs(x, y):             # Same as: eggs = tracer(eggs)
    print(x ** y)           # Wraps eggs in a tracer object


spam(1, 2, 3)               # Really calls tracer instance: runs tracer.__call__
spam(a=4, b=5, c=6)         # spam is an instance attribute

eggs(2, 16)                 # Really calls tracer instance, self.func is eggs
eggs(4, y=4)                # self.calls is per-decoration here

# za pomocą zmiennych nonlocal


def tracer(func):                        # State via enclosing scope and nonlocal
    calls = 0                            # Instead of class attrs or global

    def wrapper(*args, **kwargs):        # calls is per-function, not global
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper


@tracer
def spam(a, b, c):        # Same as: spam = tracer(spam)
    print(a + b + c)


@tracer
def eggs(x, y):           # Same as: eggs = tracer(eggs)
    print(x ** y)


spam(1, 2, 3)             # Really calls wrapper, bound to func
spam(a=4, b=5, c=6)       # wrapper calls spam

eggs(2, 16)               # Really calls wrapper, bound to eggs
eggs(4, y=4)              # Nonlocal calls _is_ per-decoration here

# za pomocą artrybutów funkcji
# ożemy za pomocą zapisu funkcja.atrybut=wartość
# przypisywać dowolne atrybuty do funkcji w celu ich dołączania. Ponieważ funkcja fabryczna
# przy każdym wywołaniu tworzy nową funkcję, więc jej atrybuty przechowują stan


def tracer(func):                        # State via enclosing scope and func attr
    def wrapper(*args, **kwargs):        # calls is per-function, not global
        wrapper.calls += 1
        print('call %s to %s' % (wrapper.calls, func.__name__))
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


@tracer
def spam(a, b, c):        # Same as: spam = tracer(spam)
    print(a + b + c)


@tracer
def eggs(x, y):           # Same as: eggs = tracer(eggs)
    print(x ** y)


spam(1, 2, 3)             # Really calls wrapper, assigned to spam
spam(a=4, b=5, c=6)       # wrapper calls spam

eggs(2, 16)               # Really calls wrapper, assigned to eggs
eggs(4, y=4)              # wrapper.calls _is_ per-decoration here

# dlaczego dekorowanie metod za pomocą klas nie działa ?

# niech sobie będzie taka o to klasa dekorująca


class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('wywołanie %s %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

# ale tutaj, powyższy dekorator spadnie z rowerka


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)  # giveRaise = tracer(giverRaise)

    @tracer
    def lastName(self):
        return self.name.split()[-1]


bob = Person('Robert Zielony', 50000)
try:
    bob.giveRaise(0.25)
except TypeError as e:
    print(e)  # to się wywróciło

# A call tracer decorator for both functions and methods


def tracer(func):                        # Use function, not class with __call__
    calls = 0                            # Else "self" is decorator instance only!

    # Or in 2.X+3.X: use [onCall.calls += 1]
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall


if __name__ == '__main__':

    # Applies to simple functions
    @tracer
    def spam(a, b, c):                       # spam = tracer(spam)
        print(a + b + c)                     # onCall remembers spam

    @tracer
    def eggs(N):
        return 2 ** N

    spam(1, 2, 3)                            # Runs onCall(1, 2, 3)
    spam(a=4, b=5, c=6)
    print(eggs(32))

    # Applies to class method functions too!
    class Person:
        def __init__(self, name, pay):
            self.name = name
            self.pay = pay

        @tracer
        def giveRaise(self, percent):        # giveRaise = tracer(giveRaise)
            self.pay *= (1.0 + percent)      # onCall remembers giveRaise

        @tracer
        def lastName(self):                  # lastName = tracer(lastName)
            return self.name.split()[-1]

    print('methods...')
    bob = Person('Bob Smith', 50000)
    sue = Person('Sue Jones', 100000)
    print(bob.name, sue.name)
    sue.giveRaise(.10)                       # Runs onCall(sue, .10)
    print(int(sue.pay))
    # Runs onCall(bob), lastName in scopes
    print(bob.lastName(), sue.lastName())

# za pomocą deskryptorów


class tracer(object):                        # A decorator+descriptor
    def __init__(self, func):                # On @ decorator
        self.calls = 0                       # Save func for later call
        self.func = func

    def __call__(self, *args, **kwargs):     # On call to original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):      # On method attribute fetch
        return wrapper(self, instance)


class wrapper:
    def __init__(self, desc, subj):          # Save both instances
        self.desc = desc                     # Route calls back to deco/desc
        self.subj = subj

    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)  # Runs tracer.__call__


anna = Person('Anna', 10)
anna.giveRaise(.10)
# wywołanie udekorowanej metody
# uruchamia czteroetapowy proces: wywołanie tracer.__get__ , po nim wywołanie metod
# wrapper.__call__ i tracer.__call__ , a na koniec wywołanie oryginalnej, opakowanej metody.


# dodawanie argumentów do dekoratora
# przykład klasy osadzonej w funkcji dekorującej , która mierzy czas wywoływania funkcji

def timer(label='', trace=True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kargs):

            start = time.process_time()
            result = self.func(*args, **kargs)
            elapsed = time.process_time() - start
            self.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format % values)
            return result
    return Timer


force = list if sys.version_info[0] == 3 else (lambda X: X)


@timer(label='[CCC]==>')
def listcomp(N):                             # Like listcomp = timer(...)(listcomp)
    # listcomp(...) triggers Timer.__call__
    return [x * 2 for x in range(N)]


@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))


for func in (listcomp, mapcall):
    result = func(5)        # Time for this call, all calls, return value
    func(50000)
    func(500000)
    func(1000000)
    print(result)
    print('allTime = %s\n' % func.alltime)   # Total time for all calls

print('**map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))

# kod dekoratorów klas

# metoda __init__ wywoływana jest, kiedy
# dekorator @ zostanie zastosowany do klasy, natomiast jej metoda __call__ uruchamiana jest,
# kiedy tworzona jest instancja klasy podmiotowej.

# jest tutaj podany przykład implementacji singletona za pomocą 3 różnych technik
# nonlocal , artrybutów funkcji oraz klasy

# 3.X only: nonlocal


def singleton(aClass):                                   # On @ decoration
    instance = None

    def onCall(*args, **kwargs):                         # On instance creation
        nonlocal instance                                # 3.X and later nonlocal
        if instance == None:
            instance = aClass(*args, **kwargs)           # One scope per class
        return instance
    return onCall


# 3.X and 2.X: func attrs


def singleton(aClass):                                   # On @ decoration
    def onCall(*args, **kwargs):                         # On instance creation
        if onCall.instance == None:
            # One function per class
            onCall.instance = aClass(*args, **kwargs)
        return onCall.instance
    onCall.instance = None
    return onCall

# 3.X and 2.X: classes


class singleton:
    def __init__(self, aClass):                          # On @ decoration
        self.aClass = aClass
        self.instance = None

    def __call__(self, *args, **kwargs):                 # On instance creation
        if self.instance == None:
            self.instance = self.aClass(
                *args, **kwargs)  # One instance per class
        return self.instance


@singleton                                      # Person = singleton(Person)
class Person:                                   # Rebinds Person to onCall
    def __init__(self, name, hours, rate):     # onCall remembers Person
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


@singleton                                      # Spam = singleton(Spam)
class Spam:                                     # Rebinds Spam to onCall
    def __init__(self, val):                    # onCall remembers Spam
        self.attr = val


bob = Person('Bob', 40, 10)                     # Really calls onCall
print(bob.name, bob.pay())

sue = Person('Sue', 50, 20)                     # Same, single object
print(sue.name, sue.pay())

X = Spam(val=42)                                # One Person, one Spam
Y = Spam(99)
print(X.attr, Y.attr)

# ----------------------------------------------
# przykłady zastosowania

# rejestrowanie wywołań funkcji
registry = {}


def register(obj):
    registry[obj.__name__] = obj
    return obj  # Dekorator zarówno klasy, jak i funkcji


@register
def spam(x):
    return(x ** 2)  # spam = register(spam)


@register
def ham(x):
    return(x ** 3)


@register
class Eggs:
    def __init__(self, x):
        self.data = x ** 4

    def __str__(self):
        return str(self.data)


print('Rejestr:')
for name in registry:
    print(name, '=>', registry[name], type(registry[name]))
print('\nWywołania ręczne:')
print(spam(2))
print(ham(2))
X = Eggs(2)
print(X)
print('\nWywołania z rejestru:')
for name in registry:
    print(name, '=>', registry[name](3))
# Wywołanie z rejestru


# Implementacja artrybutów prywatnych w Pythonie za pomocą dekoratorów

traceMe = False


def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')


def Private(*privates):                              # privates in enclosing scope
    def onDecorator(aClass):                         # aClass in enclosing scope
        print(aClass)

        class onInstance:                            # wrapped in instance attribute
            def __init__(self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)

            def __getattr__(self, attr):             # My attrs don't call getattr
                # Others assumed in wrapped
                trace('get:', attr)
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):             # Outside accesses
                # Others run normally
                trace('set:', attr, value)
                if attr == 'wrapped':                       # Allow my attrs
                    self.__dict__[attr] = value             # Avoid looping
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)      # Wrapped obj attrs
        return onInstance                                   # Or use __dict__
    return onDecorator

#  Argumenty funkcji Private wykorzystywane są, zanim nastąpi dekoracja, i są zachowywane
# w postaci referencji do zakresu funkcji zawierającej — do wykorzystania w onDecorator
# oraz onInstance .
#  Argument klasy dla onDecorator wykorzystywany jest w czasie dekoracji i zachowywany
# w postaci referencji do zakresu funkcji zawierającej — do wykorzystania w czasie two-
# rzenia instancji.
#  Obiekt opakowanej instancji zachowywany jest w postaci atrybutu instancji w onInstance —
# do wykorzystania, gdy w późniejszym czasie ma miejsce próba dostępu do atrybutów
# spoza klasy.


if __name__ == '__main__':
    traceMe = True

    # Doubler = Private(...)(Doubler)
    @Private('data', 'size')
    class Doubler:
        def __init__(self, label, start):
            self.label = label                 # Accesses inside the subject class
            self.data = start                 # Not intercepted: run normally

        def size(self):
            return len(self.data)              # Methods run with no checking

        def double(self):                      # Because privacy not inherited
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2

        def display(self):
            print('%s => %s' % (self.label, self.data))

    X = Doubler('X is', [1, 2, 3])
    Y = Doubler('Y is', [-10, -20, -30])

    # The following all succeed
    print(X.label)                             # Accesses outside subject class
    X.display()
    X.double()
    X.display()       # Intercepted: validated, delegated
    print(Y.label)
    Y.display()
    Y.double()
    Y.label = 'Spam'
    Y.display()

    # The following all fail properly
try:
    print(X.size())          # prints "TypeError: private attribute fetch: size"
    print(X.data)
    X.data = [1, 1, 1]
    X.size = lambda S: 0
except TypeError as te:
    print("Failed!", te)

# dekorator sprawdzający poprawność argumentów

trace = True


def rangetest(**argchecks):                 # Validate ranges for both+defaults
    def onDecorator(func):                  # onCall remembers func and argchecks
        if not __debug__:                   # True if "python -O main.py args..."
            return func                     # Wrap if debugging; else use original
        else:
            code = func.__code__
            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__

            def onCall(*pargs, **kargs):
                # All pargs match first N expected args by position
                # The rest must be in kargs or be omitted defaults
                expected = list(allargs)
                positionals = expected[:len(pargs)]

                for (argname, (low, high)) in argchecks.items():
                    # For all args to be checked
                    if argname in kargs:
                        # Was passed by name
                        if kargs[argname] < low or kargs[argname] > high:
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(
                                funcname, argname, low, high)
                            raise TypeError(errmsg)

                    elif argname in positionals:
                        # Was passed by position
                        position = positionals.index(argname)
                        if pargs[position] < low or pargs[position] > high:
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(
                                funcname, argname, low, high)
                            raise TypeError(errmsg)
                    else:
                        # Assume not passed: default
                        if trace:
                            print('Argument "{0}" defaulted'.format(argname))
                    # OK: wykonanie oryginalnego wywołania
                    return func(*pargs, **kargs)
            return onCall
    return onDecorator


@rangetest(age=(0, 120))                  # persinfo = rangetest(...)(persinfo)
def persinfo(name, age):
    print('%s is %s years old' % (name, age))


@rangetest(M=(1, 12), D=(1, 31), Y=(0, 2013))
def birthday(M, D, Y):
    print('birthday = {0}/{1}/{2}'.format(M, D, Y))


persinfo('Bob', 40)
persinfo(age=40, name='Bob')
birthday(5, D=1, Y=1963)

try:
    persinfo('Bob', 150)
    persinfo(age=150, name='Bob')
    birthday(5, D=40, Y=1963)
except TypeError as te:
    print(te)

# Test methods, positional and keyword


class Person:
    def __init__(self, name, job, pay):
        self.job = job
        self.pay = pay
        # giveRaise = rangetest(...)(giveRaise)

    @rangetest(percent=(0.0, 1.0))        # percent passed by name or position
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


bob = Person('Bob Smith', 'dev', 100000)
sue = Person('Sue Jones', 'dev', 100000)
bob.giveRaise(.10)
sue.giveRaise(percent=.20)
print(bob.pay, sue.pay)
try:
    bob.giveRaise(1.10)
    bob.giveRaise(percent=1.20)
except TypeError as te:
    print(te)

# Test omitted defaults: skipped


@rangetest(a=(1, 10), b=(1, 10), c=(1, 10), d=(1, 10))
def omitargs(a, b=7, c=8, d=9):
    print(a, b, c, d)


omitargs(1, 2, 3, 4)
omitargs(1, 2, 3)
omitargs(1, 2, 3, d=4)
omitargs(1, d=4)
omitargs(d=4, a=1)
omitargs(1, b=2, d=4)
omitargs(d=8, c=7, a=1)

try:
    omitargs(1, 2, 3, 11)         # Bad d
    omitargs(1, 2, 11)            # Bad c
    omitargs(1, 2, 3, d=11)       # Bad d
    omitargs(11, d=4)             # Bad a
except TypeError as te:
    print(te)
