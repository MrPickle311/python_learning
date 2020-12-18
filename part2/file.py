from pathlib import Path
import pickle
import json, struct

path_base = Path(__file__).parent # pobieranie ścieżki obecnego katalogu
#print(path_base)
path_base /= 'data'
#print(path_base)

inData = open(path_base,'r')

data = inData.read()# załadowanie całej zawartości pliku do łańcucha znaków
print(data) 

inData.seek(0) # przesuwam się do konkretnej pozycji w pliku

print(inData.read(4)) # wczytanie 4 bajtów od bieżącej pozycji

inData.seek(0)

dataLine = inData.readline() # wczytywanie jednej linii z pliku

print(dataLine)

inData.seek(0)

dataList = inData.readlines() # wczytuje plik w postaci listy stringów 
                              #uwaga! zachowuje znaki nowej linii \n
print(dataList)

inData.close() # ręczne zamknięcie pliku

out = open(path_base,'a')

out.write('\n'+dataLine) # dopisanie łańcucha na koniec pliku

out.writelines(dataList) # zapisuje listę w pliku w postaci kilku nowych wierszy
#funkcja sama z siebie dodaje znaki \n

out.flush()#Zapisanie zawartości bufora wyjściowego na 
#dysku bez zamykania pliku

out.close()

#iterowanie po pliku , pamiętaj ,że pętla wczytuje znaki \n ,co wpływa na 
#wczytanego stringa
for row in open(path_base,'r'):
    print(row + ' : readen')

out = open(path_base,'r+') # w przypadku r+ dane mogę odczytywać z początku
#pliku oraz dopisywać na koniec pliku

print(out.readline())

out.write('xd')

#kilka uwag dotyczących plików
#Do odczytywania wierszy najlepiej nadają się iteratory plików
#Zawartość pliku to łańcuchy znaków, a nie obiekty
#Pliki są buforowane i można je przeszukiwać, zanim trafią na dysk
#są przechowywane w pamięci tzn. zamknięcie pliku oraz wywołanie metody flush()
#dopiero zapisuje dane z pamięci na dysk
#Wywołanie metody close jest zazwyczaj opcjonalne,ale jej wywoływanie to 
#dobry nawyk

k = out.write('abc') # metoda write zwraca ilość zapisanych znaków 
print(k)

out.close()

print(open(path_base).read()) # wczyta cały plik 

# metoda open akceptuje znaki \ oraz / ,tylko w przypadku tych windowsowych
# muszę użyć surowego łańcucha znaków r''

bin_path = Path(__file__).parent # pobieranie ścieżki obecnego katalogu

bin_path /= 'data.bin'

#pliki binarne 

out = open(bin_path,'wb')
#uzycie w wymazuje cały plik
ba = bytearray(b'\x00\x00\x00\x07mielonka\x00\x08')
out.write(ba)

out.close()

out = open(bin_path,'rb')

#print(bin(out[4:12][0]))

#Przechowywanie obiektów w plikach

L = [6,8,443,98,34,56756]

out.close()

out = open(path_base,'w')

out.write(str(L)) # by zapisać obiekty do pliku trzeba je przetworzyć na tekst

#teraz wczytam tę listę z powrotem
out.close()

out = open(path_base,'r')

S = out.readline()

S.rstrip() # usuwanie znaku \n

print(S)

S = S[1:len(S) - 1]
print(S)

stringList = S.split(', ')

print(stringList)

print(S[0])

numbersList = [int(x) for x in stringList]

print(numbersList)

#trochę sie zeszło

out.seek(0)

# a tak można prościej za pomocą funkcji eval
S = out.readline()
S = S.rstrip()

nmbrList = list(eval(S))

print(nmbrList)

# moduł pickle służący do przechowywania obiektów w plikach

D = {'2' :2,'1' :1 }

datafilepath = Path(__file__).parent # pobieranie ścieżki obecnego katalogu

datafilepath /= 'objfile.pkl'

objfile = open(datafilepath,'wb')

pickle.dump(D,objfile) #serializacja słownika D do pliku objfile

objfile.close()

objfile = open(datafilepath,'rb')

D.clear()

D = pickle.load(objfile) # załadowanie słownika z pliku

print(D)

#serializacja do JSON

D = {'adam' : ' i ewa','ford' : 'mustang','price' : 3}

string = json.dumps(D) #funkcja ta serializuje obiekt do stringa sformatowa
                       #nego jako json

print(string)

D.clear()

D= json.loads(string) # załadowanie obiektu ze stringa JSON

print(D)

#operacje plikowe na JSON

jsonpath =  Path(__file__).parent

jsonpath /= 'dict.json'

jsondata = open(jsonpath,'w')

json.dump(D,jsondata , indent= 5 ) # zapisywanie obiektu do pliku json

jsondata.close()

jsondata = open(jsonpath,'r')
D.clear()

D = json.load(jsondata) # wczytywanie obiektu z pliku json 

print(D)


# moduł struct ogarnia spakowane dane binarne

data2path = Path(__file__).parent

data2path /= 'data2.bin'

data = struct.pack('>i4sh',7,b'sdasdasd',8)
#pakowanie danych do zmiennej data

F = open(data2path,'wb')

F.write(data)

F.close()

F = open(data2path,'rb')

data2 = F.read()

data3 = struct.unpack('>i4sh',data2)
#wypakowanie 
print(data3)