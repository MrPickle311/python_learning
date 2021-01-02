import os
from urllib.request import urlopen

def pred(x):
    return x != 0

z = 6
while pred(z): # wykonuje dopóki dostaję tutaj true
    z -= 1
    print(z)
else: # jeśli dostanę false włażę tutuaj i wykonuję ten blok jednorazowo
    print("Done")
print("OK!")

#while True: # ctrl+c by zakończyć nieskończoną pętlę
#    print('inf!')

x= 'sdsadas'
while x:
    x = x[1:]
    print(x)

#break - omija całą instrukcję swojej pętli 
#continue przechodzi na górę instrukcji
#pass - nic nie robi ,jest pustym elementem zastępczym instrukcji
#else - ten blok wykonany ,gdy nie przerwę pętli breakiem

#while True: pass # ten kod nic nie robi

def func1():
     pass # pusta funkcja ,bez zgłaszania błędu składni
def func2():
    ... # to samo ,lecz z wykorzystaniem elipsy ( ... )

X = ... # aleternatywa dla None

#contine
z = 20
while z:
    print(z)
    z -= 1
    if (z % 2): continue
    z -= 2
#break
z = 0
while True:
    z += 1
    print(z)
    if z == 15 : break
#else

while False: # jeśli pętla nie zostanie ani razu wykonana ,to i tak wchodzi
    print("True")                   # to else
else:
    print("False")

L = [1,2,3,4,5]
while len(L) != 0:
    print(L)
    L.pop()
else:
    L = [99,99,99]
print(L)

while L:
    if(len(L) == 1):
        break
    L.pop()
else:
    print("Im in the else !")
#jak widać break nie pozwala na przejście do else

#while ((x = next(obj)) != NULL) {...przetwarzanie x...}
#w Pythone nie można tak zagnieżdżać wyrażeń , wszystko musi być policzone
#na zewnątrz

#pętle for

#obsługa krotek i słowników
L = [(4,4),(2,2),(1,5),(9,0)]
for (x,y) in L:
    print(x,y)

D = dict(rommel="abc",wow=34,crt='sad')

for node in D.items():
    key,val = node
    print(key,val)

for key in D.keys():
    print(key)

L = [((1,2),3),((1,2),3),((1,2),3)]

#obsługa zagnieżdżeń
for ((x,y),z) in L:
    print(x,y,z)

L = [[1,2],[1,2,3],[1,2,3,4]]
for a,*b,c in L:
    print(a)
    for x in b: print(x) 
    print(c)

#else

items = [13,"232d","maya",(6,5)]
keys = ["robert","maya","esteban"]

for key in keys:
    for item in items:
        if key == item:
            print("Dopasowano!")
            break
    else: #Wykonywane po ostatniej iteracji pętli 
        print("Nie znaleziono")

#uwaga zmienne przed in np x in są kopiami ,ale tylko w przypadku typów ,wiec...
#niemutowalnych

L = [1,2,3,4,5]
for x in L:
    x = 0
print(L)

#obsługa plików za pomocą pętli

f = open('mydata.txt')
while True:
    dat = f.read(1)
    if not dat: break
    print(dat,sep='',end='')
else:
    f.close()

print('\n')

for char in open('mydata.txt').read():
    print(char,sep='',end='')

print('\n')

f = open('mydata.txt')

while True:
    line = f.readline()
    if not line: break
    print(line,end='')

f.seek(0)
print('\n')
while True:
    dat = f.read(8) #bierz po 8 bajtów
    if not dat: break
    print(dat,sep='',end='')
print('\n')
#for -> iterowanie jednokrotne po całej kolekcji
#while -> wyspecjalizowane iterowanie

#range -> zwraca listę kolejnych liczb całkowitych
#zip -> zwraca serię krotek równoległych elementów -> można za pomocą jednego
#fora przechodzić po kilku sekwencjach
#enumerate -> generuje wartości , jak i indeksy elementów obiektu iterowalnego

#preferuj for nad while , oraz traktuj range jako ostatnią deskę ratunku
#tworzenie listy za pomocą range
L = list(range(20,2,-2))
print(L)

#coś jak reverse
L = list('strgth')
for i in range(int(len(L)/2 - 1)):
    buffer = L[len(L) - i - 1] 
    L[len(L) - i - 1] = L[i]
    L[i] = buffer
print(L)

#ale lepiej za pomocą wycinków

#wypisywanie,co drugi znak
S = 'enryhaenber'
for x in range(0,len(S),2):
    print(S[x],end='')
print('\n')
#lub łatwiej
for c in S[::2]: print(c,end='')

print('\n')

#iterowanie po liście i jej modyfikowanie
L = [1,2,3,4,5]
for x in L:
    x *= 2
print(L)
#nie działa ,bo modyfikuję zmienną x , a nie element z listy

for i in range(len(L)):
    L[i] *= 2
print(L)
#teraz działa

L1 = ['a','b','c','d']
L2 = [1,2,3,4]

for (x,y) in zip(L1,L2):
    print(x,y,sep=' ')

L3 = [12,23,34,45]

#jednak zip potrafi robić listę krotek 
for (x,y,z) in zip(L1,L2,L3):
    print(x,y,z)

#ale jeśli dam listy o różnych długościach ,to lista krotek będzie mieć
#długość najkrótszej z list

L3 = [12,23]

for (x,y,z) in zip(L1,L2,L3):
    print(x,y,z)

#jeśli chcę jednocześnie iterować przez elementy listy oraz mieć obecny 
#numer indeksu

for (idx,val) in enumerate(L):
    print('value: '+str(val) + ' under idx : ' + str(idx))

for (idx,line) in enumerate(open('mydata.txt')):
    print(str(idx) + ' : ' + line,end='')
print('')

#obsługa powłoki

F = os.popen('dir') # polecenie powłoki 
print(F.readline()) # cała linia
print(F.read(50)) #bajty
print(os.popen('dir').readlines()) # wszystkie linie
print('')
for cmd in os.popen('dir'):
    print(cmd)

os.system('dir') # tutaj zwykle zostaje odpalone nowe okno 

for (itr,line) in enumerate(os.popen('systeminfo')):
    print(str(itr)+': '+line)

for line in urlopen('http://learning-python.com/books'):
    print(line)