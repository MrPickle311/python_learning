
# takie przypisanie zmiennej ( bez konstruktora ) 
# tworzy coś na rodzaj zmiennej statycznej

class SharedData:
    spam = 42 # Wygenerowanie atrybutu danych klasy

x = SharedData()
y = SharedData()

print(x.spam, y.spam) # Dziedziczą i współdzielą zmienną spam (SharedData.spam)

SharedData.spam = 99
print(x.spam, y.spam, SharedData.spam)

# ale jeśli przypiszemy artrybut o tej samej nazwie do zmiennej tej klasy
# to tworzy się nowy artrybut i nadpisuje ten odziedziczony

x.spam = 88
print(x.spam, y.spam, SharedData.spam)

# Mimo nadpisania przez obiekt ,to do statycznej zmiennej i tak można się dostać
# poprzez nazwę klasy

class MixedNames: # Zdefiniowanie klasy
    data = 'mielonka' # Przypisanie atrybutu klasy
    def __init__(self, value): # Przypisanie nazwy metody
        self.data = value # Przypisanie atrybutu instancji
    def display(self):
        print(self.data, MixedNames.data) # Atrybut instancji, atrybut klasy

x = MixedNames(1) # Utworzenie dwóch obiektów instancji
y = MixedNames(2) # Każdy ma własne dane
x.display(); y.display() # self.data jest inny, Subclass.data jest tym samym

# Wywołania metod wykonywane za pośrednictwem instancji, takie
# jak poniższe:
# instancja.metoda(argumenty...)
# są automatycznie przekładane na wywołania funkcji metod klas w poniższej postaci:
# klasa.metoda(instancja, argumenty...)

# Konstruktor klasy nadrzędnej można wywołać w każdej nnej metodzie

class Super:
    def __init__(self, x):
        self.x = x

class Sub(Super): 
    def __init__(self, x, y):
        Super.__init__(self, x) # Wykonanie metody __init__ klasy nadrzędnej
        #...własny kod... # Wykonanie własnych działań inicjalizacyjnych

I = Sub(1, 2)

I.xyz = 2

print(I.xyz)

# Różne sposoby na rozszerzanie funkcjonalności klas

class Superior:
    def method(self):
        print('w Super.method') # Zachowanie domyślne
    def delegate(self):
        self.action() # Oczekuje zdefiniowania !!INTERFEJS!!

class Inheritor(Superior): # Odziedziczenie wszystkich metod
    pass

class Replacer(Superior): # Całkowite zastąpienie metody 
    def method(self):
        print('w Replacer.method')

class Extender(Superior): # Rozszerzenie działania metody 
    def method(self):
        print('początek Extender.method')
        Superior.method(self)
        print('koniec Extender.method')

class Provider(Superior): # Uzupełnienie wymaganej metody
    def action(self):
        print('w Provider.action')

# Ponieważ klasy
# są obiektami, możemy je umieścić w krotce i tworzyć instancje w sposób uniwersalny bez
# konieczności używania żadnej dodatkowej składni
for klass in (Inheritor, Replacer, Extender):
    print('\n' + klass.__name__ + '...')
    klass().method()
print('\nProvider...')
x = Provider()
x.delegate()

# Tworzenie klas abstrakcyjnych lub interfejsów

# Wymaga to poniższego importu 
from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self): pass

# jednak to wymaga ogranięcia metaklas oraz dekoratorów

# Przechodzenie po drzewie klas

def classtree(cls, indent):
    print('.' * indent, cls.__name__) # Wyświetlenie tu nazwy klasy
    for supercls in cls.__bases__: # Rekurencja po wszystkich klasach nadrzędnych
        classtree(supercls, indent+3) # Może odwiedzić klasę nadrzędną więcej niż raz

def instancetree(inst):
    print('Drzewo', inst) # Pokazanie instancji
    classtree(inst.__class__, 3) # Przejście do jej klasy

def selftest():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B,C): pass
    class E: pass
    class F(D,E): pass
    instancetree(B())
    instancetree(F())

selftest()

#917