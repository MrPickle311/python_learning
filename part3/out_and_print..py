import sys
#składnia funkcji print
#print([object, ...][, sep=' '][, end='\n'][, file=sys.stdout][, flush=False])
# w celu rezygnacji ze separatorów sep=''
# * file określa plik ,strumień standardowy lub inny obiekt typu plikowego
#,do którego zostanie wysłany tekst, ma obsługiwać metodę .write(znaki)
# * flush pozwala na natychmiastowe opróżnienie bufora do strumienia wyjściowego

#poniższa instrukcja print nie wypisze teraz danych na ekran , lecz do pliku
x,y,z = 1,2,3
print(x,y,z,sep=' ... ',file=open('data.txt','w'))

#poniższa instrukcja wyciągnie wszystko z pliku i wypisze dane na ekran
print(open('data.txt','r').read())

L = [1,2,3]
sys.stdout.write(str(L))
#działa tak samo jak print ,ale nie ma tutaj fajnych bajerów

#instrukcje print po prostu wywołują metodę .write() na sys.stdout

#jednak pamiętaj by sobie zapisać ten strumień!

temp = sys.stdout

sys.stdout = open('data.txt','w')
print('xdxdxdxdxdxdx') # zapis znaków do pliku

sys.stdout.close()
sys.stdout = temp
print(open('data.txt','r').read())

#Automatyczne przekierowanie strumienia

#jednak da się jednorazowo zmienić plik docelowego zapisu
f = open('data.txt','w')
print(4*'{0[what]} and {1}'.format(dict(xd= 1,what= 5),555),sep= ' // ',
end='\n\n',file=f)
f.close()

#strumień błędów
sys.stderr.write('Some error!')
