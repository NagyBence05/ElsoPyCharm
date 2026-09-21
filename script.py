import random
from random import randint
from random import *
import random as veletlen
from random import randint as veletlen_szam



def ker_ter(a,b):
    k=2* alap +2*b
    t=a+b
    return k,t

def lotto():
    i=0
    while i<5:
        print(veletlen_szam(1,90))
        i+=1




felhasznalo_kora =int(input("Hány éves vagy: "))
if felhasznalo_kora>=18:
    print("Gyere")
    print("üdv a fedélzeten")
elif felhasznalo_kora<=25:
    print('Ifjú')
elif felhasznalo_kora<=65:
    print('Koros')
else:
    print('Nyugger')

uzenet = 'Gyere be' if felhasznalo_kora >=18 else 'Maradj kint'
print(uzenet)

i=1
while i <10:
    print(i)
    i+=1
    if i ==3:
        continue
    if i==5:
        break
    print(i)

else:
    print("Gond nélkül lefutott")
    print("Vége a ciklusnak")

alap=5
magassag=3
kerulet=ker_ter(alap,magassag)[0]
terulet=ker_ter(alap,magassag)[1]
print(f'Kerulet={kerulet}\n Terulet={terulet}')

eredmeny= ker_ter(alap,magassag)
print(f'Kerulet={eredmeny[0]}\n Terulet={eredmeny[1]}')
print(f'Kerulet={ker_ter(alap,magassag)[0]}\n Terulet={ker_ter(alap,magassag)[1]}')

i=0
while i <5:
    print(veletlen_szam(1,90))
    i+=1

    print("")

    lotto()





