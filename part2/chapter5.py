import math, numbers
a = 3 +4j
b = 2j
print(a/b)
print(abs(a))

re = 5
im = 10

z = complex(re,im)
print(z.real)
print(z.imag)
k = z.conjugate()
print(k)


l1 = [1,2,3,4,5,6,7,8,9]
l2 = l1[2:8]
print(l2)
print(2 ** 3)

x = 5
y = 2

print(x / y) #dzielenie normalne 
print(x // y) #obcina czesc ulamkowa
print(x // float(y) ) # tutaj wynikiem bedzie liczba zmiennoprzecinkowa
A = 3 
B = 8
C = 6
if A < C < B:
    print('It works!')
if not ( 1.1 + 2.2 ) == 3.3:
    print('Bad precision error :(')
# istnieje pewna niedokladnosc sprawiajaca to ,ze nie 
# nastapi tam rownosc

print( -x // y)
#tutaj obcina w dol ,wynik to -3 ; -2.5 -> -3
print(math.floor(-x/y))
print(math.trunc(-x/y))
print(2 ** 200) # bardzo duza liczba ,ale jest od razu 
#dostepna w jednej z zmiennej ,tak od reki

dec = 10
bin = 0b10101
hex = 0xFFF
oct = 0o777
