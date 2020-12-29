# w pythonie nie ma instrukcji switch

#operatory and oraz or nie zwracają True ,czy False ,tylko obiekty 
#reprezentujące True lub False 

#operator or zwraca pierwszy obiekt będący prawdą ,lub zwraca element z 
#prawej strony będący prawdą lub fałszem
#  i stop wyszukiwanie
print([] or [1])
#[1]

print({} or [])
#[]

print(not [] or not [1])
#True

#Dla operatora and Python zatrzmuje się dla pierwszego elementu będącego 
#fałszem 

print(5 and 2)
print(2 and 5)
#dla true and true zwraca po prostu prawą stronę

print([] and 2)
print(2 and [])
#zwraca fałsz

print([] and {})
print({} and [])
#jeśli mamy false and false to zwraca lewą stronę

#instrukcję warunkową można zapisać w jednym wyrażeniu

X = 0
Z = 0

if X:
    Z = 9
else:
    Z = 12

Z = 9 if X else 12
print(Z)

#dwie powyższe instrukcje są tożsame

#można równiez zrobić taką sztuczkę za pomocą listy
A = [23,'sd'][bool(X)]
print(A)

#wyodrębnianie elementów o wartości true

L= [1,2,{},'',0,2,3]
L  = list(filter(bool,L))
print(L)