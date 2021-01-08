#nazwa funkcji jest tak naprawdę referencją do obiektu funkcji
#gdy interpreter dotrze do słowa def ,to tworzy obiekt funkcji i przypisuje
#go do nazwy referencyjnej
#lambda tworzy anonimowy obiekt funkcji i go zwraca w miejscu
#return bez żadnej wartości zwraca None
#instrukcja yield działa jak return ,ale zapamiętuje gdzie zakończyła 
#działanie -> generatory -> omówione później
#global pozwala na deklarowaine zmiennych , które będą dostępne na poziomie
#modułu 

#nonlocal - pozwala na deklarowanie zmiennych z funkcji otaczającej,
#które mają być przypisane

#obiekty mutowalne są przekazywane przez referencję,a niemutowalne przez
#wartość

#w Pythone jest tylko czas wywoływania ,więc funkcje mogą być tworzone w locie

def func(attr):#kiedy Python trafi na tę definicję ,to tworzy nowy obiekt
    print('Hello!' + str(attr))

alias = func
alias(2)

#wyznaczanie części wspólnej
def func1(seq1,seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

print(func1([12,243,23,23,1,212,423,31,],[12,423,12,134,24,23,121,11]))

