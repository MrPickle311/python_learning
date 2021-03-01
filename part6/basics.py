# Są obiekty klas (fabryki) oraz są obiekty instancji
# Instrukcja class tworzy obiekt klasy i przypisuje mu nazwę.
# Atrybuty klasy udostępniają stan obiektu oraz jego zachowanie
# Przypisania wewnątrz instrukcji class tworzą atrybuty klasy.

# Kiedy wywołujemy obiekt klasy, otrzymujemy obiekt instancji
# Każdy obiekt instancji dziedziczy atrybuty klasy oraz otrzymuje własną przestrzeń nazw.
# Przypisania do atrybutów self w metodach tworzą atrybuty dla poszczególnych instancji

# Pierwszy przykład 831

class  FirstClass:
    def setData(self,value):
        self.data = value
    def display(self):
        print(self.data)

x  = FirstClass()
x.setData(4)
x.display()

y = FirstClass()
#y.display() błąd ,zmienna data nie jest zdefiniowana

#Można dodawać nawet zmienne w locie

y.xd = 'xd'
print(y.xd) 

#W Pythone instancje dziedziczą po klasach

# Klasy nadrzędne są wymieniane w nawiasach w nagłówku instrukcji class.
# Klasy dziedziczą atrybuty po swoich klasach nadrzędnych.
# Instancje dziedziczą atrybuty po wszystkich dostępnych klasach.
# Każda referencja obiekt.atrybut wywołuje nowe, niezależne wyszukiwanie.
# Zmiany logiki wykonuje się przez tworzenie klas podrzędnych, a nie modyfikację klas nadrzędnych.

class SecondClass(FirstClass):
    def display(self): # przysłonięcie
        print("Present value = %s " % self.data)

z = SecondClass()
z.setData(800)
z.display()

#Trochę o przeciążaniu operatorów

# Metody zawierające w nazwie podwójne znaki _ (jak __X__) są specjalnymi punktami zaczepienia.
# Takie metody wywoływane są automatycznie, kiedy instancje pojawiają się w operacjach wbudowanych.
# Klasy mogą nadpisywać większość operacji na typach wbudowanych.
# Nie istnieją wartości domyślne dla metod przeciążania operatorów i nie są one potrzebne.
# Klasy w nowym stylu mają pewne wartości domyślne, ale nie dla typowych operacji.
# Operatory pozwalają klasom na integrację z modelem obiektów Pythona

class ThirdClass(SecondClass):
    def __init__(self,value): # konstruktor
        self.data = value
    def __add__(self,other): # operator dodawania 
        return ThirdClass(self.data + other)
    def __str__ (self): # operator konwersji do str
        return 'ThirdClass : {0}'.format(self.data)
    def mul(self,other): # jakaś metoda
        self.data *= other # zauważ ,że argumentami tutaj są ThirdClass oraz liczba

b = ThirdClass(4)
b.mul(8)
print(b + 6)

# Metody o specjalnych nazwach, takie jak __init__, __add__ oraz __str__, są dziedziczone
# przez klasy podrzędne oraz instancje

# Zalecane jest ,by operatory zwracały pewne obiekty przez return

# Tworzenie pustej klasy

class rec: pass

# ale do niej i tak można dodawać atrybuty
# ZAUWAŻ ,ŻE ŻADNA INSTACJA KLASY JESCZE NIE POWSTAŁA

# klasy same w sobie są obiektami , bez instancji
rec.name = 'adam'

print(rec.name)

o = rec()
# tutaj też mamy adam, widać ,że instancja dziedziczy artrybuty po klasie
print(o.name)

# Tak naprawdę, jak zobaczymy w rozdziale 29 842

