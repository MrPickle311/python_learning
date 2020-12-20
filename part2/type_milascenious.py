#Metody porównywania różnych typów przez Pythona

#Liczby - od największej do najmniejszej 
#Łańcuchy - leksykograficznie ( według kodów zwracanych przez funkcję ord)
# Listy i krotki - porównywane są poprzez zestawienie każdego komponentu
#  od lewej do prawej strony oraz rekurencyjnie dla struktur
#  zagnieżdżonych, aż do końca lub pierwszego niedopasowania
# Zbiory są równe jeśli zawierają te same elementy 
#Słowniki uznawane są za równe, jeżeli ich posortowane 
# listy (klucz, wartość) są równe.

#nie można wykonywać testów  wielkości dla  typów mieszanych
#nie można sortować kolekcji typów mieszanych

#ten kod nie zadziała
#11 >= '11'
#ale ten tak i zwróci false
print(11 == '11')

#nie można bezpośrednio porównywać słowników ,ale można pośrednio

D1 = {'2' : 2, '3' : 3}
D2 = {'2' : 2, '4' : 4}

print(
    sorted(D1.items()) < sorted(D2.items()) 
)

#obiekt jest prawdą lub fałszem ,gdy

#liczby są prawdą , jeżeli nie są zerem
#obiekty są fałszem ,jeżeli są puste

#istnieje funkcja konwertująca obiekty na typ bool

print(
    bool({}),
    bool([3,2]),
    sep='\t',
    end='\n'
)

#Wstępna inicjalizacja listy o 100 elementach

L = [None] * 100

#Uwaga na cykliczne struktury danych!!!

L = ['Abba']
L.append(L)

print(L) # [...] symbolizuje odwołanie do samej siebie
#nie używaj ich jeżeli naprawdę nie musisz ,bo wpadniesz w nieskończoną pętle

#363
