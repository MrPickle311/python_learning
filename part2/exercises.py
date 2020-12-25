D = {5645: {'name' : 'Damian','surname' : 'Wojcik',
'age': 22,'email': 'mm@sp','tel_nr': 34424232}}

##print(D[5645]['email'])

f = open('myfile.txt','w')

f.write('Hello world\n')

f.close()

f = open('myfile.txt','r')

print(f.read())
