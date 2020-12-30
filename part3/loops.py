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

#Warto pamiętać — skanery plików 450