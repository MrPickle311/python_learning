#zwykłe przypisanie pozycyjne 1->1 , 2->2
hello, xd  = 'gogo' , 'backback'
print(hello,xd)

#liczba elementów po lewej stronie musi być taka sama , jak po prawej
#lub prawa strona musi być ciągiem o odpowiedniej długości

[spam,ham] = ['spam','ham']
# takiej formie to działa tak samo jak to wyżej
print(spam)

a, b, c, d = 'abcd'
#tutaj tak samo ,ale jako ,że string jest typem iterowalnym
#to do zmiennych zostaną przypisane poszczególne znaki

print(a)

####rozszerzone rozpakowanie sekwencji

#działa z dowolnymi typami iterowalnymi
w,*q = 'sdasda'
print(w)
print(q)
#w = 's'
#q = ['d', 'a', 's', 'd', 'a']
#w bierze 1-szy znak , q resztę ,tak działa tutaj gwiazdka 

#zmienną z gwiazdką można umieścić w dowolnym miejscu sekwencji

*a,b = [1,2,3,4]
print(a,b)
#[1, 2, 3] 4

a,*b,c = [1,2,3,4,5]
print(a,b,c)
#1 [2, 3, 4] 5

#przypadki brzegowe
a,b,c,*d = [1,2,3,4] # d = [4] jest jednoelemetnową listą
a,b,c,d,*e = [1,2,3,4] # tutaj nie będzie błędu ,lecz e = [] będzie puste

#wyrażenie z gwiazdką może być tylko jedno

#przykład z pętlą while
L = range(4)
while L:
    front,*L = L
    print(front,L)

#przykład z pętlą for
for a,*b,c in [(1,2,3,4),(5,6,7,8)]:
    print(a,b,c)

####przypisanie do wielu celów 

anal = oral = 'xdxdxd'
print(anal)
print(oral)

#jednak należy uważać z typami mutowalnymi
a = b = [1,2,3] # tutaj zostaną utworzone 2 referencje do [1,2,3]
a[0] = 99
print(b[0])
#99

#by tego uniknąć można zrobić tak:
a,b = [1,2,3] , [1,2,3]


string = 'jajo'
a,b,c = list(string[:2]) + [string[2:]]#['j', 'a', 'jo']
print(a,b,c)
#j a jo

#przypisywanie z zagnieżdżaniem

((a,b),c,d) = ('ab','c','d')
print(a,b,c,d)
#a b c d

#przypisanie kolejnych liczb całkowitych za pomocą range()

a,b,c,d,e = range(5)
print(a,b,c,d,e)
#0 1 2 3 4 

###możliwe skróty przypisań

#X += Y     X &= Y      X -= Y      X |= Y
#X *= Y     X ^= Y      X /= Y      X >>= Y
#X %= Y     X <<= Y     X **= Y     X //= Y

#są szybsze niż normalna forma , gdyż następuje tylko jedno przypisanie
#konkatencja (A + B) zawsze tworzy nowy obiekt,ale += tylko go modyfikuje
L = [1,2,3]
L += 'ggo'
print(L) # taka sama operacja jak extend()
#L = L + 'ssd' dla list takie coś nie będzie działać , nie można dodać listy do stringa

#Konwencję nazw można znaleźć w Python PEP 8s