import script

felhasznalo_kora = int(15.65)
felhasznalo_kora += 19
felhasznalo_neve= "Erik"
felhasznalo_neve *= 2
metszet = felhasznalo_neve[:-5]
jegyek = [2, 5, 4, 3]
jegyek += [5]
del jegyek[0]
halmaz = {'magyar', 'angol', 'orosz', 3}
hallgato = {"nev": 'Jolán', "kor": 19}
print(hallgato["nev"])
print(halmaz)
print('Szia', felhasznalo_neve, "!", jegyek)

print("Jó", "reggelt", "DUE", end='\n\n,', sep='-')
print("Új sor")
print('Több \n'
      'Kiírás\n'
      '!!!!!')
print(f'Szia {felhasznalo_neve}! \n {jegyek}')
print(f'kora: {felhasznalo_kora: .2f}')

print(felhasznalo_neve.rjust(30,'.'))
print(felhasznalo_neve.ljust(30,'.'))
print(felhasznalo_neve.center(30,'.'))
print(str(felhasznalo_kora).center(30))



