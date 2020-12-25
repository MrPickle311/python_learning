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

#rozszerzone rozpakowanie sekwencji
w,*q = 'sdasda'
print(w)
print(q)
#w = 's'
#q = ['d', 'a', 's', 'd', 'a']
#w bierze 1-szy znak , q resztę ,tak działa tutaj gwiazdka 

#przypisanie do wielu celów 

anal = oral = 'xdxdxd'
print(anal)
print(oral)

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
#394
#Rozszerzona składnia rozpakowania sekwencji w Pythonie 3.x
