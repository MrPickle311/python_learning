import builtins
#Zasady
#Moduł zawierający funkcję jest zasięgiem globalnym.
#Zasięg globalny rozciąga się jedynie na jeden plik.
#W Pythonie nie istnieje coś takiego jak jeden
#obejmujący wszystko globalny zasięg oparty na plikach
#Przypisane nazwy są lokalne, o ile nie zostaną zadeklarowane jako globalne lub nielokalne.
#Pamiętaj również o tym, że modyfikacje obiektów w miejscu nie klasyfikują zmiennych jako lokalnych
#Jeżeli na przykład
#nazwa L zostanie przypisana do listy na najwyższym poziomie modułu, instrukcja taka
#jak L.append(X) wewnątrz funkcji nie zaklasyfikuje L jako zmiennej lokalnej, natomiast L = X
#już tak.
#W tym pierwszym przypadku zmieniamy obiekt listy, do którego odwołuje się
#zmienna L, a nie samą zmienną L.

#w instrukcji def:
#przypisania nazw tworzą i modyfikują nazwy lokalne
#referencje do nazw przeszukują co najwyżej 4 zasięgi - 
#lokalny funkcji ,
# funkcji zawierających(może być więcej niż jedna, kilka )
#tę funkcję,globalny, wbudowany
#global - zasięg modułu, nonlocal - funkcja zawierająca

#LEGB - local,enclosing,global,built-in

#pętle for nie ograniczają zasięgu swoich zmiennych do zasiegu instrukcji
#w bloku try wszystko jest lokalne
#zasięg wbudowany zawiera się w module builtins ,jednak sam moduł trzeba zaimportować
#jednak można korzystać z niego bez jego importowania

#zasięg globalny
X = 2

#zasięg lokalny
def func():
    X = 3 # tworzenie zmiennej lokalnej
    print(X)
func()
print(X) # będzie 2 

print(dir(builtins))

#w następujacej funkcji funkcja open została przysłonięta przez zmienną open
def func2():
    open = 23
    # f = open("mydata.txt") nie zadziała
func2()

#NIE ZMIENIAJ DEFINICJI WBUDOWANYCH NAZW PYTHONA

#instrukcja global daje znać ,że funkcja zmieni jedną lub więcej nazw globalnych 

def func3():
    global X # te nazwy będą modyfikowane
    X = 20
func3()
print(X)

#prezentacja działania reguły legb
z,y = 2,3
def glob():
    global X
    X = z + y # zmienna globalna może się odnosić do innych globalnych bez global
glob()
print(X)

#541

#zasięgi zagnieżdżone
#Referencja -> szuka zmienną w zasiegu lokalnym funkcji ,a potem w zasiegach
#lokalnych wszystkich funkcji zawierających tę funkcję 
#potem global , a potem builtin

#Przypisanie tworzy lub modyfikuje zmienną w bieżącym zasięgu lokalnym
#nonlocal sprawia ,że przypisanie modyfikuje zmienną w zasięgu lokalnym najbliższej funkcji
#zawierającej

def f1():
    X = 99
    def f2():
        print(X) # można sięgnąć do X
    f2()
f1()

def f3():
    X = 88
    def f2():
        print(X)
    return f2
action = f3()#coś jak wskaźnik na funkcję
action() # wywołąnie f3.f2

#funkcje w Pythonie są obiektami jak wszystko inne
#nawet pamięta wartość zmiennej X
#takie funkcje (chodzi o tę zwróconą) będą zawsze pamiętać zmienne z otaczających je
#zasięgów 

#Funkcje fabrykujące (domknięcia)

def maker(N):
    def action(X):
        return X ** N
    return action
# tutaj wewnętrzna funkcja action pamięta argumenty N i dlatego każde wywołanie maker z innymi
# daje inny rezultat funkcji action

r1 = maker(3)
print(r1(2)) # pamięta 3
r2 = maker(5)
print(r2(2)) # pamięta 5
print(r2(3)) # pamięta 5

#lub użycie lambdy zamiast tego 
def maker2(N):
    return lambda X: X ** N
r3 = maker(2)
print(r3(3))

#549
#funkcja zawsze pamięta wszystkie wartości w zasięgu otaczającym ją
def fn1():
    x = 88  #Python zanim wejdzie do funckji fn2() x,y zostają obliczone
    def fn2(x=x,y=20): #domyślne argumenty
        print(x,y)
    fn2()
fn1()

#staraj się unikać zagnieżdżenia funkcji


L = [23,2.3,"sadsada",'XD',dict(x=23,y=45)]

#lambdy mają swoje własne zasięgi

def fn3():
    x = 4
    action = lambda n: x ** n + 3 # x=4 jest pamiętane 
    # lub action = (lambda n: x ** n + 3)
    return action
x = fn3()
print(x(3))

def makeActions(): # funkcja zwracająca listę funkcji
    acts = []       # jednak takie rozwiązanie nie działa
    for i in range(5): # zauważ ,że lambdy będą wywoływane po zakończeniu pętli
        acts.append(lambda x: i ** x)#więc dla wszystkich pięciu lambda i będzie równe 4
    return acts

acts = makeActions()
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))

def makeActions2(): # funkcja zwracająca listę funkcji
    acts = []       # takie rozwiązanie działa
    for i in range(5): #ale pamiętaj ,że tak mogę przekazać obiekt mutowalny ,co może narobić kłopotów
        acts.append(lambda x,i=i: i ** x)#użycie domyślnej wartości
    return acts                          #argumentów pozwala na takie zapamiętywanie

acts = makeActions2()
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))

#dzięki instrukcji nonlocal istnieje możliwość modyfikacji zmiennej w zasięgu funkcji 
#zawierającej funkcję. W przeciwieństwie do global zmienne nonlocal muszą już istnieć
#w momencie deklaracji w zasięgu funkcji zawierającej
#nazwa zmiennej jest szukana tylko w zasięgu funkcji zawierającej funkcję

#instrukcja nonlocal całkowicie pomija zasięg lokalny funkcji
# 555
print('nonlocal\n\n')

def func4(y):
    x = y
    def nested(z):
        nested.state = z #artrybut funkcji
        print('state = ',str(nested.state))
        nonlocal x,k # od teraz będzie można zmodyfikować
        x += z     # x
        k += z
        print(x)
        print('k = ' + str(k))
    k = 1 # tę zmienną też zobaczy
    return nested
t = func4(5)
t(2)
t(3) # UWAGA!! nastąpi tutaj modyfikacja istniejącego stanu
     # zostanie wyświetlona wartość 10 = 5 + 2 + 3
k = t
k(1)
print('the state is = ' + str(t.state)) # odniesienie się do artrybutu funkcji
t(1) #można tak przekazywać referencje obiektu funkcji w pamięci
k(1)

#Uwaga!
#W przeciwieństwie do instrukcji global , zanim zmienna będzie ustawiona jako 
#nonlocal ,to musi istnieć już w pamięci,czyli musi zostać ówcześnie stworzona w funkcji zawierajacej!



