def pred(x):
    return x != 0

z = 6
while pred(z): # wykonuje dopóki dostaję tutaj true
    z -= 1
    print(z)
else: # jeśli dostanę false włażę tutuaj i wykonuję ten blok jednorazowo
    print("Done")
print("OK!")

#while True: # ctrl+c by zakończyć nieskończoną pętlę
#    print('inf!')

x= 'sdsadas'
while x:
    x = x[1:]
    print(x)

#break - omija całą instrukcję swojej pętli 
#continue przechodzi na górę instrukcji
#pass - nic nie robi ,jest pustym elementem zastępczym instrukcji
#else - ten blok wykonany ,gdy nie przerwę pętli breakiem

#while True: pass # ten kod nic nie robi

def func1():
     pass # pusta funkcja ,bez zgłaszania błędu składni
def func2():
    ... # to samo ,lecz z wykorzystaniem elipsy ( ... )

X = ... # aleternatywa dla None

#contine
z = 20
while z:
    print(z)
    z -= 1
    if (z % 2): continue
    z -= 2
#break
z = 0
while True:
    z += 1
    print(z)
    if z == 15 : break
#else

while False: # jeśli pętla nie zostanie ani razu wykonana ,to i tak wchodzi
    print("True")                   # to else
else:
    print("False")


# ilość godzin + 1

#443 Więcej o części pętli else