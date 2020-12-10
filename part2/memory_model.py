import copy, sys
#zmienne odnoszą się do określonych obiektów zaalokowanych w 
#pamięci ,są jak wskaźniki na nie ,są tylko nazwami ,
#dlatego można przypisywać im różne typy
#Po prostu odnoszą się do konkretnego obiektu w określonym
#momencie
a = 3 
a = 'ABCDS'
a = 2.23
#działa 
#zmienna zawiera referencję do obiektu
#Obiekty zawierają dwa pola nagłówków - desygnator typu
#i licznik referencji

#po usunięciu ostatniej referencji do obiektu 

b = 3 +3j
c = b
#teraz zmienne odnoszą się do tego samego obiektu

L1 = [2,3,4]
L2 = L1
L1[0] = 23 # tutaj nastapi modyfikacja obiektu ,ktory
#jest wspoldzielony przez L1 i L2
print(L2)
print(L1)

def f1(list):
    list[0] = -1
    print(list)
f1(L1)
print(L1) # widac ,ze jesli przekaze liste do funkcji ,to jest ona
#przekazywana przez referencje

L3 = L1[:] #kopiowanie listy za pomoca wycinka
L3[0] = 0
print(L1)

#Ogólnie : przypisanie obiektu mutowalnego (listy,słownika,zbioru,
# pewnych klas) do nazwy zmiennej tworzy referencję do niego

#jednak można skopiować listę i inne kontenery używając modułu copy
L4 = copy.copy(L1)
L5 = copy.deepcopy(L1)
L4[0] = 100
L5[1] = 300
print(L4)
print(L5)
print(L1)
#L1 bez zmian

if L1 == L2:
    print("Listy są sobie równe")
if L1 is L2: # operator is sprawdza ,czy obiekty są wskaźnikami do
    print("To są te same listy")# tego samego miejsca w pamięci

x = 5
y = 5
print(sys.getrefcount(5))
# jest bardzo duzo referencji do obiektu o wartości 5
# jest to obiekt niemutowalny
# zwykła opytamalizacja

#Python stosuje model referencyjny

