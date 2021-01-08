#Zasady
#Moduł zawierający funkcję jest zasięgiem globalnym.
#Zasięg globalny rozciąga się jedynie na jeden plik.
#W Pythonie nie istnieje coś takiego jak jeden
#obejmujący wszystko globalny zasięg oparty na plikach
#Przypisane nazwy są lokalne, o ile nie zostaną zadeklarowane jako globalne lub nielokalne.
#Pamiętaj również o tym, że modyfikacje obiektów w miejscu nie klasyfikują zmiennych jako lokalnych
#Jeżeli na przykład
#nazwa L zostanie przypisana do listy na najwyższym poziomie modułu, instrukcja taka
#jak L.append(X) wewnątrz funkcji nie zaklasyfikuje L jako zmiennej lokalnej, natomiast L = X
#już tak.
#W tym pierwszym przypadku zmieniamy obiekt listy, do którego odwołuje się
#zmienna L, a nie samą zmienną L.

#Rozwiązywanie nazw — reguła LEGB