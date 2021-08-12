
# Przeciążanie operatorów

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self): # Dodana metoda
        return '[Person: %s, %s]' % (self.name, self.pay) # Wyświetlany łańcuch znaków  

# Technicznie rzecz biorąc, metoda __str__ jest preferowana przez funkcje print i str,
# a metoda __repr__ jest używana jako rezerwowa dla tych ról i we wszystkich innych kontekstach.

# Wywołanie metody klasy bazowej oraz redefiniowanie konstruktorów

class Manager(Person):
    def __init__(self, name, pay): # Zredefiniowanie konstruktora
        Person.__init__(self, name, 'manager', pay) 
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus) # MUSISZ TUTAJ NA POCZĄTKU PRZESŁAĆ SELF!!!

bob = Person('Robert Zielony')
anna = Person('Anna Czerwona', job='programista', pay=100000)
tom = Manager('Tomasz Czarny', 50000)

# a oto jak działa polimorfizm

for obj in (bob, anna, tom):
    obj.giveRaise(.10)
    print(obj)

# nie używaj funkcji super

# printowanie nazw klas , artrybutów obiektów 

#Wbudowany atrybut instancja.__class__ udostępnia łącze z instancji do klasy, z której została ona utworzona

# __bases__ dającą dostęp do klas nadrzędnych.

# obiekt.__dict__ udostępnia słownik z parami klucz-wartość dla
# każdego atrybutu dołączonego do obiektu przestrzeni nazw (w tym modułów, klas oraz
# instancji)

print(bob.__class__)

print(bob.__class__.__name__)

print(list(bob.__dict__.keys()))

# bases

print(Person.__bases__)
print(bob.__class__.__bases__)

# Przyklad wykorzystania różnych artrybutów i funkcji do implementacji narzędzia do 
# wyswietlania nazw artrybutów i ich wartości jako klucz-wartość 

class AttrDisplay:
    """
    Udostępnia dziedziczoną metodę przeciążania wyświetlania, która pokazuje instancje z ich nazwami klas, a także parę
    nazwa=wartość dla każdego atrybutu przechowanego w samej instancji (ale nie atrybutów odziedziczonych po klasach).
    Można ją wmieszać w dowolną klasę i będzie działała na dowolnej instancji.
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)
    def __repr__(self):
            return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

class TopTest(AttrDisplay):
    count = 0
    def __init__(self):
        self.attr1 = TopTest.count
        self.attr2 = TopTest.count+1
        TopTest.count += 2

class SubTest(TopTest):  
    pass

X, Y = TopTest(), SubTest() # Utwórz dwie instancje
print(X) # Pokazanie wszystkich atrybutów instancji
print(Y) # Pokazanie najniższej nazwy klasy

# operator __str__ ma zastosowanie tylko do print oraz funckcji str !!!!
# do reszty idzie __repr__

# wyświetlenie wszystkich artrybutów i metod
print(dir(bob))

# serializacja i deserializacja obiektów

# pickle - prosta serializacja do pliku
# shelve - pozwala przechowywać zserializowane obiekty po kluczu

# oto przykład serializacji obiektów za pomocą shelve

import shelve
db = shelve.open('persondb') # Nazwa pliku, w którym przechowywane są obiekty
for obj in (bob, anna, tom): # Użycie atrybutu name obiektu jako klucza
    db[obj.name] = obj # Przechowanie obiektu w pliku shelve po kluczu
db.close() # Zamknięcie po wprowadzeniu zmian

# wartością klucza musi być UNIKALNY STRING , ale może być byle jaki

#deserializacja

db = shelve.open('persondb')

print(len(db))

print(list(db.keys()))

bob = db['Robert Zielony'] # Pobranie obiektu bob po kluczu
print(bob)

db.close()

# uaktualnienie danych
db = shelve.open('persondb')
anna = db['Anna Czerwona'] # Indeksowanie za pomocą klucza w celu pobrania
anna.giveRaise(.10) # Uaktualnienie w pamięci za pomocą metody klasy
db['Anna Czerwona'] = anna # Przypisanie do klucza w celu uaktualnienia w pliku shelve
db.close() # Zamknięcie po wprowadzeniu zmian

# 891
