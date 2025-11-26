"""
Olvasunk be billentyűzetről egész számokat, és tároljuk őket egy listában! A bevitel végét a 0 jelezze.  Majd oldjuk meg a következő feladatokat!Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e -10 és -15 közé eső szám a beírtak között?
2. Írjuk ki az utolsó 2-vel és 5-tel osztható szám indexét!
3. Hány darab 20-nál nagyobb számot írtak be?
4. Melyik és hányadik volt a legkisebb beírt pozitív egész szám?
5. Mennyi a negatív számok számok átlaga?

"""
elsoli = [] # Első feladat üres listája
masodik = [] # Második feladat üres listája
otodik = [] # Ötödik feladat üres listája
lista = [] # Alapprogram üres listája

print("Dolgozat feladat")
while True:
    egesz = int(input("Írd be az egész számokat, ha abba szeretnéd hagyni írj be 0-át! "))
    lista.append(egesz)
    if 0 in lista:
        break

print(lista)

# Első feladat
print("Első feladat:")

l = -15
u = -10

elso = len([i for i in lista if l <= i <= u])
elsoli.append(elso)

if elsoli[0] > 0:
    print("Van -10 és -15 közé eső szám!")
else:
    print("Nincs -10 és -15 közé eső szám!")

# Második feladat:
print("Második feladat:")

for i in lista:
    if i % 2 == 0 and i % 5 == 0:
        lista.index(i)
        masodik.append(i)
masodik.remove(int(0))
try:
    print(f"Az utolsó 2-vel és 5-el osztható szám indexe: {lista.index(masodik[-1])+1}.")
except IndexError:
    print("Nincs 2-vel és 5-el osztható szám a listában!")



# Harmadik feladat:
print("Harmadik feladat:")

harmadik = 20

# Megszámolja hány elem nagyobb mint 20

szamlalas = sum(1 for x in lista if x > harmadik)

print(f"{szamlalas} darab szám volt ami 20-nál nagyobb")

# Negyedik feladat:
print("Negyedik feladat:")

negy = max(lista)

print(f"A legnagyobb szám a listában {negy}, helye: {lista.index(negy)+1}")

# Ötödik feladat:
print("Ötödik feladat:")

for i in lista:
    if i < 0:
        lista.index(i)
        otodik.append(i)  
try:    
    atlag = sum(otodik) / len(otodik)
    print(f"A negatív számok átlaga: {atlag}")
except ZeroDivisionError:
    print("Nincs mínusz szám a listában!")
