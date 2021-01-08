#1
S = "string"
sum = 0
for c in S:
    sum += ord(c)
print(sum)

L = [ord(c) for c in S]
print(L)
L = list(map(ord,S))
print(L)

#2
#for i in range(50):
#    print('Hello %d\n\a' % i)

#3
D = dict(x=2,g=4,h=6,j=3,df=56,sad=34)
L = sorted(D) # sorted zwraca listę,słowniki sortuje wg. kluczy
for key in L:
    print(key,D[key],end='\n',sep='\t')

#4
L = [1,2,4,8,16,32,64]
X = 5

for (idx,n) in enumerate(L):
    if 2**X == L[idx]:
        print('Under index i',idx)  
        break
else: print(X,'not found')
    
if 2**X in L: print('Under index i',L.index(2**X)) 
else: print(X,'not found')    

L = [2**x for x in range(X+1)]
print(L)

L = list(map(lambda x: 2 ** x,range(7)))

#5 done
