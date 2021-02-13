#jeśli wartością domyślną argumentu funkcji będzie obiekt mutowalny
#to między wywołaniami funkcji jego stan będzie zachowywany

def saver(x=[]): # x jest referencją do jednego miejsca w pamięci, podanie argumentu do funkcji 'przestawia wskaźnik' zmiennej na inny obiekt, 
    x.append(1) # Zmienia ten obiekt za każdym razem!             \  jednak pozostawienie domyślnej sprawia ,że między wywołaniami operuje się
    print(x)                                                    # \  na tym samym obiekcie

saver([2]) # otrzymam [2,2]
saver() # otrzymam [1]
saver() # otrzymam [1,1]

#tę niepożądaną cechę języka można usunąć następująco:

def saver2(x=None):
    x = x or []
    x.append(1)
    print(x)

#artrybuty działają podobnie jak domyślne argumenty mutowalne
