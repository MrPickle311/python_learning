import math, numbers, random, decimal, fractions
from decimal import Decimal
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

dec1 = 10
bin1 = 0b10101
hex1= 0xFFF
oct1 = 0o777

print(oct(dec1))
print(bin(hex1))
print(hex(bin1))

print(int('23232323',4))
print(int('34343434KKKMM',35)) #pierwszy argument jest jakas liczba
#zapisana w formacie , ktory okresla drugi argument
#sama funkcja int konwertuje wszystko do postaci dziesietnej

#13:00
print("BITY")

n = 0b00101
m = 0b10100
s = n << 2
print(bin(s))
print(bin(n | m))
print(bin(n & m))
print(bin(0b10101 ^ 0b01010))
print(bin(0b1111 ^ 0b0101))
print(n.bit_length())

print("Modul math")

print(max(math.pi,math.e,math.inf,math.tau))
print(min(math.pi,math.e,math.inf,math.tau))
print(sum((3,4,4,3,2,3))) # przyjmuje tylko zbior liczb
print(sum([1,2,3,4,5]))

print("Modul random")

print(random.randint(-30,500))
print(random.random())

collection = ['apple','orange','strawberry','cherry']
print(random.choice(collection))#wybranie losowego elementu
random.shuffle(collection)#tasowanie
print(collection)

print("Modul decimal")
d1 = Decimal('0.1')
print(d1)
print(Decimal('0.1') - Decimal('0.2') + Decimal('0.1'))
#tutaj juz sa dokladne liczby

print(Decimal(0.10))
#szalenie duza dokladnosc,az powoduje blad

decimal.getcontext().prec = 5 #ustawienie stalej precyzji

print(Decimal(34) / Decimal(65))

print("Modul fraction")

print(fractions.Fraction(2,3))
print(fractions.Fraction(4,7))
print(fractions.Fraction(3,9))#automatycznie skraca ulamki

print(fractions.Fraction(3,7)+ fractions.Fraction(5,21))
#niezły jest

print(fractions.Fraction('34/321') + fractions.Fraction('32'))

# liczby Decimal oraz Fraction są mogą być dokładne,ale są wolniejsze 

g = 2.7

print(fractions.Fraction(*g.as_integer_ratio()))# gwiazdka przekształca 
# krotkę na zbiór argumentów