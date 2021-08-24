from __future__ import print_function    # 2.X compatibility

# Rozszerzanie typów za pomocą osadzania

# Ten przykład rozszerza klasę wbudowanej listy

class Set:
   def __init__(self, value = []):    # Constructor
       self.data = []                 # Manages a list
       self.concat(value)

   def intersect(self, other):        # other is any sequence
       res = []                       # self is the subject
       for x in self.data:
           if x in other:             # Pick common items
               res.append(x)
       return Set(res)                # Return a new Set

   def union(self, other):            # other is any sequence
       res = self.data[:]             # Copy of my list
       for x in other:                # Add items in other
           if not x in res:
               res.append(x)
       return Set(res)

   def concat(self, value):           # value: list, Set...
       for x in value:                # Removes duplicates
          if not x in self.data:
               self.data.append(x)

   def __len__(self):          return len(self.data)            # len(self), if self
   def __getitem__(self, key): return self.data[key]            # self[i], self[i:j]
   def __and__(self, other):   return self.intersect(other)     # self & other
   def __or__(self, other):    return self.union(other)         # self | other
   def __repr__(self):         return 'Set:' + repr(self.data)  # print(self),...
   def __iter__(self):         return iter(self.data)           # for x in self,...ta)

x = Set([1, 3, 5, 7])
print(x.union(Set([1, 4, 7])))
print(x | Set([1, 4, 6]))

# Rozszerzanie typów za pomocą klas podrzędnych
# Można wbdowane typy rozszerzać również przez dziedziczenie

class Set(list):
    def __init__(self, value = []):      # Constructor
        list.__init__([])                # Customizes list
        self.concat(value)               # Copies mutable defaults

    def intersect(self, other):          # other is any sequence
        res = []                         # self is the subject
        for x in self:
            if x in other:               # Pick common items
                res.append(x)
        return Set(res)                  # Return a new Set

    def union(self, other):              # other is any sequence
        res = Set(self)                  # Copy me and my list
        res.concat(other)
        return res

    def concat(self, value):             # value: list, Set, etc.
        for x in value:                  # Removes duplicates
            if not x in self:
                self.append(x)

    def __and__(self, other): return self.intersect(other)
    def __or__(self, other):  return self.union(other)
    def __repr__(self):       return 'Set:' + list.__repr__(self)

if __name__ == '__main__':
    x = Set([1,3,5,7])
    y = Set([2,1,4,5,6])
    print(x, y, len(x))
    print(x.intersect(y), y.union(x))
    print(x & y, x | y)
    x.reverse(); print(x)

# Klasy w nowym stylu

# 1011

# POMINĄŁEM : Pomijanie instancji we wbudowanych operacjach
# przy pobieraniu atrybutów 

# Klasy są typami
# Obiekt type generuje klasy będące jego instancjami, natomiast klasy generują instancje
# swoich typów. Oba pojęcia są typami, ponieważ generują instancje

# Wszystkie obiekty dziedziczą po klasie object

class C: pass
X = C()

print(type(X), type(C))
print(isinstance(X, object))
print(isinstance(C, object))

# to samo tyczy się typów wbudowanych

print(isinstance('spam', object))
print(isinstance(str, object))

# i type

print(isinstance(type, object))

# Zmiany w dziedziczeniu diamentowym

# lewo , a potem do góry

class A: attr = 1
class B(A): pass
class C(A): attr = 2
class D(B,C): pass

x = D()
print(x.attr) 
# stary styl : Kolejność przeszukiwania: x, D, B, A
# nowy styl : Kolejność przeszukiwania: x, D, B, C

# ten mechanizm tzw. MRO można śledzić poprzez __mro__

print(D.__mro__)

print('\n\n')
# Sloty: deklaracje atrybutów

# Aby móc używać slotów, należy przypisać sekwencję nazw specjalnej zmiennej __slots__
# i atrybutowi na najwyższym poziomie instrukcji class . Tylko te nazwy, które znajdują się na
# liście __slots__ , mogą być atrybutami instancji, którym będzie można przypisywać wartości.

class limiter(object):
    __slots__ = ['age', 'name', 'job']

# Przed użyciem należy przypisać wartość

x.age = 40
print(x.age)

x.h = 6
print(x.h)

# slotów nie należy używać z wyjątkiem naprawdę szczególnych przypadków
# wykorzystujemy je , gdy wykorzystanie pamięci jest kwestią krytyczną

# Gdy tworzonych jest wiele instancji, a wymaganych jest tylko kilka atrybutów, wtedy przydziela-
# nie słownika przestrzeni nazw każdemu obiektowi instancji może być kosztowną operacją pod
# względem wykorzystania pamięci. Aby oszczędzić miejsce, Python nie przydziela słownika każ-
# dej instancji, tylko rezerwuje w każdej z nich przestrzeń niezbędną do przechowywania
# wartości każdego atrybutu slotu wraz z odziedziczonymi atrybutami we wspólnej klasie na
# potrzeby zarządzania dostępem do slotów. W ten sposób przyspiesza się wykonywanie kod

# Sloty i słowniki przestrzeni nazw 1035

# POMIJAM : SLOTY, tylklo i wyłącznie przyspieszają dostęp do pamięci

# Właściwości klas 

# To jest przypisanie getterów , setterów , deleterów oraz doców
# do pewnej zmiennej w klasie , co oznacza tyle ,że operacje IO na 
# nich będą się odbywać poprzez te nowe funkcje

class newprops():
    def getage(self):
        return 40
    def setage(self, value):
        print('ustawienie wieku: %s' % value)
        self._age = value
    age = property(getage, setage, None, None)

x = newprops( )
print(x.age) # Wykonuje getage
x.age = 42 # Wykonuje setage ustawienie wieku: 42
print(x._age) # Normalne pobranie; nie ma wywołania getage -> PODŁOGA PO NAZWIE
print(x.age) # Wykonuje getage
x.job = 'instruktor' # Normalne przypisanie; nie ma wywołania setage
print(x.job)# Normalne pobranie; nie ma wywołania getage

# Odpowiednik tej samej klasy ,ale za pomocą przeciążania operatorów

class classic:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError
    def __setattr__(self, name, value):
        print('ustawienie: %s %s' % (name, value))
        if name == 'age':
            self.__dict__['_age'] = value # Lub object.__setattr__()
        else:
            self.__dict__[name] = value

# Metody statyczne
# Są stworzone do współpracy z obiektem klasy, a nie — jak zwykłe metody — z obiektem instancji.

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
    def printNumInstances(): # O to jest metoda statyczna , nie przyjmuje obiektu instancji
        print("Liczba utworzonych instancji: ", Spam.numInstances)

class Methods:
    def imeth(self, x):            # Normal instance method: passed a self
        print([self, x])

    def smeth(x):                  # Static: no instance passed
        print([x])

    def cmeth(class_, x):             # Class: gets class, not instance
        print([class_, x])

    smeth = staticmethod(smeth)    # Make smeth a static method (or @: ahead)
    cmeth = classmethod(cmeth)     # Make cmeth a class method (or @: ahead)

#Z technicznego punktu widzenia Python pozwala na stosowanie trzech typów metod:
#  metod instancji, którym przekazywany jest obiekt instancji self
#  metod statycznych, którym nie jest przekazywany żaden dodatkowy obiekt (za pomocą
#staticmethod );
#  metod klas, którym przekazywany jest obiekt klasy (za pomocą classmethod i standardowo
#w metaklasach).

obj = Methods()


# Metoda statyczna, wywoływana z klasy
print(Methods.smeth(3)) # Instancja nie jest przekazywana ani oczekiwana
# Metoda statyczna, wywoływana z instancji
print(obj.smeth(4))# Instancja nie jest przekazywana


Methods.cmeth(5) #Metoda klasy, wywoływana z klasy
obj.cmeth(6)

# POMINĄŁĘM DO KOŃCA ROZDZIAŁU , nic przydatnego -> zaczynamy wyjątki