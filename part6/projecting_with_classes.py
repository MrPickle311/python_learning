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

# Odczyt listy atrybutów obiektu — __dict__ 985