#Przykład dziedziczenia i kompozycji

class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)
    def work(self):
        print(self.name, "robi różne rzeczy")
    def __repr__(self):
        return "<Pracownik: imię=%s, wynagrodzenie=%s>" % (self.name, self.salary)
    
class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)
    def work(self):
        print(self.name, "przygotowuje jedzenie")

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)
    def work(self):
        print(self.name, "obsługuje klienta")
    
class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)
    def work(self):
        print(self.name, "przygotowuje pizzę")

class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, "zamawia od", server)
    def pay(self, server):
        print(self.name, "płaci za zamówienie", server)

class Oven:
    def bake(self):
        print("piec piecze")

class PizzaShop:
    def __init__(self):
        self.server = Server('Ernest')
        self.chef = PizzaRobot('Robert')
        self.oven = Oven()
    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


bob = PizzaRobot('robert')
print(bob)
bob.work()
bob.giveRaise(0.20)
print(bob); print()
for klass in Employee, Chef, Server, PizzaRobot:
    obj = klass(klass.__name__)
    obj.work()

scene = PizzaShop()
scene.order('Amadeusz')
print('...')
scene.order('Aleksander')

# Wraper pozwalający opakowywać dany obiekt

class wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print('Śledzenie: ' + attrname)
        return getattr(self.wrapped, attrname)

x = wrapper([1,2,3])
x.append(4)
print(x.wrapped)

x = wrapper({"a": 1, "b": 2})
print(x.keys())

# Pseudoprywatne artrybuty klas

# Jeśli mamy jakąś klasę np. X , to jeśli przed nazwą atrybutu damy
# przedrostek __ np. __method() , __data , to zostanie on niejawne zamieniony 
# na __X_method() , __X_data

class Super:
    def method(self): ... # Zwykła metoda

class Tool:
    def __method(self): pass  # Nazwa zostanie niejawnie zmieniona na _Tool__method
    def other(self): self.__method() # Użycie metody wewnętrznej
    
class Sub1(Tool, Super): 
    def actions(self): self.method() # Wywołuje Super.method()

class Sub2(Tool):
    def __init__(self): self.method = 99 # Nie psuje Tool.__method

# Wiązanie metdod klas z zewnętrznymi obiektami

class Spam:
    def doit(self, message):
        print(message)

object1 = Spam()
x = object1.doit
x('Witaj, świecie!')

object1 = Spam()
t = Spam.doit
t(object1, 'siema')

class Eggs:
    def m1(self, n):
        print(n)
    def m2(self):
        x = self.m1
        x(42)

Eggs().m2()

class Number:
    def __init__(self, base):
        self.base = base
    def double(self):
        return self.base * 2
    def triple(self):
        return self.base * 3

x = Number(2)
y = Number(3)
z = Number(4)

def square():
    return 2 ** 2

acts = [x.double, y.double, y.triple, z.double , square] # Lista metod związanych

for act in acts:
    print(act())

# Tworzenie klas mieszanych

# Jeśli klasa dziedziczy wielokrotnie i mamy tę samą nazwę zdefiniowaną
# w kilku klasach bazowych , to jest wybierana ta pierwsza z lewej , 
# a jeśli na danym poziomie nic nie ma , to lecimy do góry

# Odczyt listy atrybutów obiektu — __dict__

class ListInstance:
    """
    Klasa mieszana formatująca informacje wyświetlane przez metody
    print i str za pomocą zkodowanej tutaj dziedziczonej metody __str__.
    Nazwy __X zapobiegają konfliktom z atrybutami klas.
    """
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tnazwa %s=%s\n' % (attr, self.__dict__ [attr])
        return result
    def __str__(self):
        return '<Instancja klasy %s, adres %s:\n%s>' % (
                        self.__class__.__name__,
                        id(self),
                        self.__attrnames())

class Spam(ListInstance): # Dziedziczy metodę __str__
    def __init__(self):
        self.data1 = 'jedzenie'

x = Spam()
print(x)

class Super:
    def __init__(self):         # Metoda __init__ klasy nadrzędnej
        self.data1 = 'mielonka' # Tworzenie atrybutów instancji
    def ham(self):
        pass
    
class Sub(Super, ListInstance): # Wmieszanie metod ham i __str__
    def __init__(self):         # Metody wyświetlające mają dostęp do self
        Super.__init__(self)
        self.data2 = 'jajka'    # Więcej atrybutów instancji
        self.data3 = 42
    def spam(self):             # Definiujemy jeszcze jedną metodę
        pass

X = Sub()
print(X)

# Wyjście idealne do testowania , dziedziczenie argumentu funkcji

def tester(listerclass, sept=False):

    class Super:
        def __init__(self):
            self.data1 = 'mielonka'
        def ham(self):
            pass
    class Sub(Super, listerclass):
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'jajka'
            self.data3 = 42
        def spam(self):
            pass

    instance = Sub()  # Zwrócenie instancji z metodą __str__ klasy listującej
    print(instance)
    if sept: print('-' * 80)

# Wydobywanie atrybutów odziedziczonych z użyciem dir()

# Słownik __dict__ zawiera bowiem jedynie atrybuty
# instancji, natomiast funkcja dir dodatkowo zwraca atrybuty odziedziczone

class ListInherited:
    """
    Wykorzystujemy funkcję dir() do uzyskania listy atrybutów instancji
    oraz atrybutów odziedziczonych. W Pythonie 3.x uzyskamy większą liczbę
    nazw w porównaniu z 2.x, ponieważ w modelu klas w nowym stylu niejawnie
    stosowana jest klasa nadrzędna super. Metoda getattr pobiera odziedziczone
    nazwy, których nie ma w self._dict_. Zamiast metody __repr__ należy
    użyć __str__, ponieważ w przeciwnym wypadku podczas wyświetlania
    związanych metod nastąpi zapętlenie!
    """
    def __attrnames(self, indent=' '*4):
        result = 'Podkreślenia%s\n%s%%s\nInne%s\n' % ('-'*77, indent, '-'*77)
        unders = []
        for attr in dir(self): # Metoda dir instancji
            if attr[:2] == '__' and attr[-2:] == '__': # Pominięcie wewnętrznych nazw
                unders.append(attr)
        else:
            display = str(getattr(self, attr))[:82-(len(indent) + len(attr))]
            result += '%s%s=%s\n' % (indent, attr, display)
        return result % ', '.join(unders)
                                
tester(ListInherited)

# Wypisywanie atrybutów dla każdego obiektu w drzewie klas

class ListTree:
    """
    Klasa mieszana zwracająca ślad __str__ całego drzewa klasy
    i atrybutów wszystkich jego obiektów na poziomie self i powyżej.
    Metoda str uruchamiana za pomocą funkcji print zwraca skonstruowany
    ciąg. Klasa wykorzystuje nazwy __X atrybutów, aby uniknąć konfliktów
    z klientami. Jawnie odwołuje się do klas nadrzędnych i dla przejrzystości
    wykorzystuje metodę str.format.
    """
    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}\n'.format(attr)
        else:
            result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result
    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Klasa {1}:, adres {2}: (Patrz wyżej)>\n'.format(
                            dots,
                            aClass.__name__,
                            id(aClass))
        else:
            self.__visited[aClass] = True
            here = self.__attrnames(aClass, indent)
            above = ''
            for super in aClass.__bases__:
                above += self.__listclass(super, indent+4)
            return '\n{0}<Klasa {1}, adres {2}:\n{3}{4}{5}>\n'.format(
                        dots,
                        aClass.__name__,
                        id(aClass),
                        here, above,
                        dots)
    def __str__(self):
        self.__visited = {}
        here = self.__attrnames(self, 0)
        above = self.__listclass(self.__class__, 4)
        return '<Instancja {0}, adres {1}:\n{2}{3}>'.format(
                            self.__class__.__name__,
                            id(self),
                            here, above)

tester(ListTree)
