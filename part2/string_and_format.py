import sys
#łańcuchy są niemutowalne
s1 = " 'hello' " #tak możemy dodać sobie cudzysłowy
s2 = 'hello'
print(s1)
print(s2)
s3 = '"hello"'
print(s3)
#apostrofy i cudzysłowy są stosowane wymiennie 
#są po to ,by móc się w sobie nawzajem osadzać

e = "Hello " 'World' # niejawna konkatencja S
print(e)

print('\' hello \' ') #jednak tak też można umieścić apostrofy

#W Pythonie jeden znak nie zajmuje jednego bajta!!!

#jak dam \0 to print szaleje, nie wiem czemu
s4 = 'abc'
print(s4) # znak \0
print(len(s4))# długość łańcucha będzie zachowana 

S = "m\tielonka"
print(S)
#print(len(S))

print(1)

str1 = r'\nasd\b\0\tsad\\' # surowy łańcuch znaków blokujący sekewncje ucieczki
#str2 = r'df\' <--- nie wolno dawac na koncu znaku \ ,gdyz powoduje to 
print(str1)             # blad skladni
print(len(str1))

str2 = """Monty
 Monty  
\tPython\n!"""
#taka składnia zaczynająca się od """ pozwala na kontynujację
#wielowierszowych napisów, zauważ ,że początek kontynuacji zaczyna się
#od początku następnej linii

#Tymczasowe wyłączenie kodu ze skrytpu
"""
a = 4
print('xd')
"""

print(str2)

mystring ='superstring'
for c in mystring:
    print(c,end=' ') 
print('\n')
strx = 'Python'
print(strx[1:4]) # zaczynamy od znaku 1 ,ale kończymy na 3 
#dla strx[a,b] zostanie pobrany wycinek ,którego graniczne
# znaki kryją się pod indeksami  [a.b-1]
#przedział jest lewostronnie domknięty oraz prawostronnie otwarty

print(strx[:-1]) #pobranie całego ciągu bez ostatniego znaku

# str[-2] = str[len(str) - 2]

stry = strx[0:10:2] # [start,koniec,krok]
print(stry)

print(strx[::2]) # to samo 

#iteracja od konca , co drugi znak
print(strx[::-2])
#Python
print(strx[2:0:-1]) #jezeli stosuję ujemny krok ,to granice się odwracają

S = 'abcedfg'
#   S[3]^  ^S[7] zaczynam od 7 znaku i koncze na 3 ale bez jego pobrania
print(S[7:3:-1])

print('harrypoter'[slice(0,None,2)]) # składnia wycinka
print('harrypoter'[slice(None,None,-1)])

#wycinki pozwalają na ekstrakcję pewnego podwyrażenia w stringu
#służą również do oczyszczania łańcuchów z niepotrzebnych elementów

print(ord('S')) # konwertuje znak na odpowiadający mu indeks liczbowy
print(chr(83))  # konwertuje indeks na znak
print(ord(chr(67))) # operacje jednoznaczne

print(ord('0'))

#algorytmik konwersji liczb binarnych na dziesietne
B = '11101'
I = 0
while B != '':
    I = I * 2 + ( ord(B[0]) - ord('0'))
    B = B[1:] # pop_front
print(I)

#########################################################################
print("Modyfikacja lancuchow znakow")

s = 'gamma'
#s[0] = 'k'
#łańcuchy to obiekty niemutowalne !!!

k = 'k' + s[1:]
print(k) 

#trzeba to robic przez kopiowanie 

######################< TABELKA METOD NA OBIEKTÓW str >~###################
#S.capitalize()                           S.ljust(width [, fill])
#S.casefold()                             S.lower()
#S.center(width [, fill])                 S.lstrip([chars])
#S.count(sub [, start [, end]])           S.maketrans(x[, y[, z]])
#S.encode([encoding [,errors]])           S.partition(sep)
#S.endswith(suffix [, start [, end]])     S.replace(old, new [, count])
#S.expandtabs([tabsize])                  S.rfind(sub [,start [,end]])
#S.find(sub [, start [, end]])            S.rindex(sub [, start [, end]])
#S.format(fmtstr, *args, **kwargs)        S.rjust(width [, fill])
#S.index(sub [, start [, end]])           S.rpartition(sep)
#S.isalnum()                              S.rsplit([sep[, maxsplit]])
#S.isalpha()                              S.rstrip([chars])
#S.isdecimal()                            S.split([sep [,maxsplit]])
#S.isdigit()                              S.splitlines([keepends])
#S.isidentifier()                         S.startswith(prefix [, start [, end]])
#S.islower()                              S.strip([chars])
#S.isnumeric()                            S.swapcase()
#S.isprintable()                          S.title()
#S.isspace()                              S.translate(map)
#S.istitle()                              S.upper()
#S.isupper()                              S.zfill(width)
#S.join(iterable)
########################################################################

S = 'karma'
a = S.replace('a','o') # zmien wszystkie a na o 
b = S.replace('a','o',1) # zmien tylko jedno a na o
print(a)
print(b)

i = S.find('m') #zwraca liczbę reprezentującą indeks początkowy podciągu
print(i)        # lub -1 ,gdy nie zostanie znaleziony

L = list(S) # przemiana stringa na liste
print(L)

L[4] = 't'
L[3] = 's' # modyfikacja
print(L)

S = ''.join(L + L + [' xd']) # skladanie stringow z list
print(S)
S = ' , '.join(L + L + [' xd']) # skladanie stringow z list
#---^^^^- to jest separator kazdego znaku z kompletu list
print(S)

#wydzielanie podłańcuchów do postaci listy
h = 'abc def ghi jkl'
d = h.split()#domyślnie dowolny bialy znak
print(d)

h = 'abc::def::ghi::jkl'
d = h.split('::')#określenie separatora
print(d)

#METODY ŁAŃCUHCÓW NIE PRZYJMUJĄ WZORCRÓW , SŁUŻY DO TEGO MODUŁ re

if(S.startswith('k ,')):
    print('S zaczyna sie od \'k ,\'')

#############################################################################
print("Wyrazenia formatujace tekst")

#za pomocą operatora % można formatowac ciagi znakow
# formatowany_lancuch_znakow % (wyraz_formatujacy_1,wyraz_formatujacy_2,...)

print('Dostalem %f punktow %s' % (1.5,'z pasow'))

#%f - liczba float
#%d - całkowita
#%s - string

print('Dostalem %s lub %s punktow %s ' % (1,1.6,'z pasow'))
#wszystkie typy pasuja do %s,czesto bywa to najlepsze rozwiazanie
#formatowanie tworzy nowy lancuch

#znaki ,które można postawić po %
# s Łańcuch znaków (lub dowolny obiekt str(X))
# r To samo co s, z tym że wykorzystuje funkcję repr, a nie str
# c Znak (int lub str)
# d Liczba dziesiętna
# i  Liczba całkowita
# u To samo co d (przestarzałe, dawniej wymuszało liczbę całkowitą bez znaku)
# o Liczba ósemkowa (podstawa 8)
# x Liczba szesnastkowa (podstawa 16)
# X To samo co x, jednak wyświetlane wielkimi literami
# e Liczba zmiennoprzecinkowa w formacie wykładniczym, małą literą
# E To samo co e, wyświetlane wielką literą
# f Liczba zmiennoprzecinkowa w zapisie dziesiętnym
# F Liczba zmiennoprzecinkowa w zapisie dziesiętnym (wielkie litery)
# g Zmiennoprzecinkowe e lub f
# G Zmiennoprzecinkowe E lub F
# % Literał % (zapisywany jako %%)

#Ogólna składnia formatująca 
# %[(nazwa)][opcje][szerokość][.precyzja]kod_typu
# Nazwa klucza do indeksowania słownika znajdującego się po prawej stronie wyrażenia
# Opcje (flagi) określające na przykład wyrównywanie do lewej strony (-), znak liczby (+), spację
#przed liczbami dodatnimi i znak - przed liczbami ujemnymi czy dopełnienie zerami (0).
# Całkowita szerokość pola dla podstawionego tekstu.
# Liczba cyfr (precyzja) wyświetlana po przecinku dla liczb zmiennoprzecinkowych

x = 2341
y = 32.3523423897642347823 * 0.0000000000001
print( 'integers: ...%d...%-6d...%06d' % (x,x,x) )
print('%05.6s' % y )
print('%e | %.20f | %g' % (y,y,y))

#print('%.*f' % (1/3.0 , 1/3.0) ) nie zadziała 
print('%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0))
#                                      ^^^ precyzja trzeciej liczby

#formatowanie za pomocą słownika

print('This costs %(value)d %(currency)s' % {'value':23 , 'currency' : 'euro' })

#stworzmy kilka zmiennych

x = 34
y = "OK!"
z = 23.231

#uzycie tych zmiennych w stringu

print('there are some nmbrs: %(x)d , %(y)s , %(z)f' % vars())
#funkcja vars() pozwala na odnoszenia sie w sposób słownikowy do zmiennych

var = ' i have %s of %s'
print(var % ('couple','keys'))

#####################################################################
print('Metody formatujace tekst')
#jest to po prostu metoda równoważna do poprzedniej , nie lepsza ,nie gorsza

#podstawianie pozycyjne
template = '{0} {1} {2}'
#o co tu chodzi ? już tłumaczę:
# wyrażenia {0} {1} {2} odnoszą się do kolejnych argumentów przekazanych
# do funkcji format, są to klucze słownika ,czyli nie musi to być
#konkretnie {0} {1} {2}. Może to być również {dane1} {dane2}
print(template.format('xd','again xd ','XD')) 

#podstawianie po słowie kluczowym
template = '{dane1} and {dane2}'
print(template.format(dane1 = '!!!', dane2 = '???'))
#tutaj następuje użycie domyślnych argumetnów funkcji

#podstawianie przez pozycję względną:
template = '{} {} {}'
print(template.format('xd1','xd2','xd3'))

#połączenie technik
template = 'the first arg is {0} , rest... {shape} , {colours}'
template = template.format(1000,shape = 'traingle', colours = ['black','white'])
print(template)

worktype = 'I have {1[spam]} with os: {0.platform} and {1[mouse]} mouse '
#                   ^korzystam tutaj z argumentu 1 oraz szukam klucza spam
worktype = worktype.format(sys, {'spam' : 'computer','mouse' : 'wireless'} )
#                              argument nr.1 jest słownikiem
print(worktype)

#połączenie wykorzystania list oraz słowników 
list1 = 'OGAR'

#również można indeksować po elementach listy 
text = '{0[0]} + {0[1]} + AR + {1[0]} + {2}'
text = text.format(list1,list1,'XD',list1)
print(text)

tuple1 = [1,2,3],[4,5,6],'XDDDD'
text = text.format(*tuple1)
print(text)

#278

