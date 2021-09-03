# Funkcja umieszczona w argumencie fget musi zwracać wartość atrybutu,
# natomiast funkcje umieszczone w argumentach fset i fdel nie mogą zwracać żadnego wyniku
# (albo zwracać wartość None ).

class Person:                       # Add (object) in 2.X
    def __init__(self, name):
        self._name = name
    def getName(self):
        print('fetch...')
        return self._name
    def setName(self, value):
        print('change...')
        self._name = value
    def delName(self):
        print('remove...')
        del self._name
    name = property(getName, setName, delName, "name property docs")

bob = Person('Bob Smith')           # bob has a managed attribute
print(bob.name)                     # Runs getName
bob.name = 'Robert Smith'           # Runs setName
print(bob.name)
del bob.name                        # Runs delName

print('-'*20)
sue = Person('Sue Jones')           # sue inherits property too
print(sue.name)
print(Person.name.__doc__)          # Or help(Person.name)

print('\n\n')
# Dekoratory setter i deleter

class Person:
    def __init__(self, name):
        self._name = name

    @property                       # getter
    def name(self):                 # name = property(name)
        "name property docs"
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):          # name = name.setter(name)
        print('change...')
        self._name = value

    @name.deleter
    def name(self):                 # name = name.deleter(name)
        print('remove...')
        del self._name

bob = Person('Bob Smith')           # bob has a managed attribute
print(bob.name)                     # Runs name getter (name 1)
bob.name = 'Robert Smith'           # Runs name setter (name 2)
print(bob.name)
del bob.name                        # Runs name deleter (name 3)

print('-'*20)
sue = Person('Sue Jones')           # sue inherits property too
print(sue.name)
print(Person.name.__doc__)          # Or help(Person.name)

# Deskryptory 1237

# Sygnatura klasy deskryptora

class Descriptor:
    "miejsce na łańcuch znaków dokumentacji"
    def __get__(self, instancja, właściciel): ... # Zwraca wartość atrybutu
    def __set__(self, instancja, właściciel): ... # Nic nie zwraca (None)
    def __delete__(self, instancja): ... # Nic nie zwraca (None)

# Klasy zawierające dowolną z powyższych metod uznawane są za deskryptory, a ich metody
# są specjalne, jeśli jedna z ich instancji zostanie przypisana do atrybutu innej klasy — przy dostę-
# pie do atrybutu są one wywoływane automatycznie.

# By atrybut był tylko do odczytu, należy zdefiniować
# metodę __set__ w taki sposób, aby przechwytywała przypisania i zgłaszała wyjątek.

class D:
    def __get__(*args): print('pobranie')
    def __set__(*args): raise AttributeError('nie można ustawić\n')

class C:
    a = D()

a = C()

print(a.a)
try:
    a.a = 6
except AttributeError as X:
    print(X)

class Name:                             # Use (object) in 2.X
    "name descriptor docs"
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name
    # self jest instancją klasy Name ,
    # instance jest instancją klasy Person ,
    # owner to klasa Person .
    def __set__(self, instance, value):
        print('change...')
        instance._name = value
    def __delete__(self, instance):
        print('remove...')
        del instance._name

class Person:                           # Use (object) in 2.X
    def __init__(self, name):
        self._name = name
    name = Name()                       # Assign descriptor to attr

bob = Person('Bob Smith')               # bob has a managed attribute
print(bob.name)                         # Runs Name.__get__
bob.name = 'Robert Smith'               # Runs Name.__set__
print(bob.name)
del bob.name                            # Runs Name.__delete__

print('-'*20)
sue = Person('Sue Jones')               # sue inherits descriptor too
print(sue.name)
print(Name.__doc__)                     # Or help(Name)

print('\n')
# Deskryptor jako klasa może mieć również swój stan

class DescState:                           # Use descriptor state, (object) in 2.X
    def __init__(self, value):
        self.value = value
    def __get__(self, instance, owner):    # On attr fetch
        print('DescState get')
        return self.value * 10
    def __set__(self, instance, value):    # On attr assign
        print('DescState set')
        self.value = value

# Client class
class CalcAttrs:
    X = DescState(2)                       # Descriptor class attr
    Y = 3                                  # Class attr
    def __init__(self):
        self.Z = 4                         # Instance attr

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)                 # X is computed, others are not
obj.X = 5                                  # X assignment is intercepted
CalcAttrs.Y = 6                            # Y reassigned in class
obj.Z = 7                                  # Z assigned in instance
print(obj.X, obj.Y, obj.Z)

obj2 = CalcAttrs()                         # But X uses shared data, like Y!
print(obj2.X, obj2.Y, obj2.Z)

print('\n')

# Ten typ deskryptora odnosi się do pól instancji klasy
# poprzez parametr instance w metodzie __get__

class InstState:                           # Using instance state, (object) in 2.X
    def __get__(self, instance, owner):
        print('InstState get')             # Assume set by client class
        return instance._X * 10
    def __set__(self, instance, value):
        print('InstState set')
        instance._X = value

# Client class
class CalcAttrs:
    X = InstState()                        # Descriptor class attr
    Y = 3                                  # Class attr
    def __init__(self):
        self._X = 2                        # Instance attr
        self.Z  = 4                        # Instance attr

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)                 # X is computed, others are not
obj.X = 5                                  # X assignment is intercepted
CalcAttrs.Y = 6                            # Y reassigned in class
obj.Z = 7                                  # Z assigned in instance
print(obj.X, obj.Y, obj.Z)

obj2 = CalcAttrs()                         # But X differs now, like Z!
print(obj2.X, obj2.Y, obj2.Z)

# właściwości i deskryptory są ze sobą silnie powiązane — wbu-
# dowana funkcja property jest po prostu wygodnym sposobem tworzenia deskryptora

# Symulowanie metody property() za pomocą deskryptorów 

class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel                                  # Save unbound methods
        self.__doc__ = doc                                # or other callables

    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't get attribute")
        return self.fget(instance)                        # Pass instance to self
                                                          # in property accessors
    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)

class Person:
    def getName(self): print('getName...')
    def setName(self, value): print('setName...')
    name = Property(getName, setName)                     # Use like property()

x = Person()
x.name
x.name = 'Bob'
del x.name

# Metody __getattr__ oraz __getattribute__ 1248