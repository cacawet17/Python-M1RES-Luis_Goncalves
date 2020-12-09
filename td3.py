# -*- coding: utf-8 -*-
"""TD3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jnJiDeXjTBPbXiHe1WN0yXxrfGZ03Ej9
"""

#Exercice1

print("# * 1 * #")

n = input("Entrer un nombre: ")
for i in range(1,11):
	print(n*i)


print("# * 2 * #")

n = input("Entrer un nombre: ")
for i in range(1,11):
	print(n*i,)


print("\n")
print("# * 3 * #")

n = input("Entrer un nombre: ")
for i in range(n):
	print("Table de", i+1, ":",)
	for j in range(1,11):
		print((i+1)*j,)
	print("\n")


print("\n")
print("# * 4 * #")

n = input("Entrer un nombre: ")
for i in range(n):
	print(""(i+1))


print("# * 5 * #")

n = input("Entrer un nombre: ")
for i in range(n):
	print(" "((n-1)-i) + (" "(i+1))[:2(i+1)-1] + " "*((n-1)-i))

#Exercice2

print("# * 1 * #")

jours = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mois = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

mj = []
for i in range(12):
	mj.append((mois[i], jours[i]))

print(mj)


print("# * 2 * #")

annee = []
for x in mj:
	for y in range(x[1]):
		annee.append(str(y+1) + " " + x[0])

print(annee)


print("# * 3 * #")

annee2 = []
jours_semaine = ["Monday", "Tueday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for x in range(365):
	annee2.append(jours_semaine[x%7] + " " + annee[x])
	
print(annee2)


print("# * 4 * #")

dico_annee = {}
for i in range(365):
	dico_annee[annee[i]] = jours_semaine[i%7]

print(dico_annee)


print("# * 5 * #")

print(dico_annee["28 October"])

#Exercice3

print("# * 1 * #")

nb = 0
liste_notes = []
while nb < 3:
	note = input("Entrer une note: ")
	liste_notes.append(note)
	nb += 1

mini = min(liste_notes)
maxi = max(liste_notes)
moy = 0
for n in liste_notes:
	moy += n
moy = float(moy)/len(liste_notes)

print("Note minimale:", mini)
print("Note maximale:", maxi)
print("Moyenne:", moy)



print("# * 2 * #")

nb_notes = input("Combien de notes voulez-vous entrer? ")
nb = 0
liste_notes = []
while nb < nb_notes:
	note = input("Entrer une note: ")
	liste_notes.append(note)
	nb += 1

mini = min(liste_notes)
maxi = max(liste_notes)
moy = 0
for n in liste_notes:
	moy += n
moy = float(moy)/len(liste_notes)

print("Note minimale:", mini)
print("Note maximale:", maxi)
print("Moyenne:", moy)



print("# * 3 * #")

liste_notes = []
note = input("Entrer une note (taper fin pour terminer la saisie): ")
while note != "fin":
	liste_notes.append(float(note))
	note = input("Entrer une note (taper fin pour terminer la saisie): ")

mini = min(liste_notes)
maxi = max(liste_notes)
moy = 0
for n in liste_notes:
	moy += n
moy = float(moy)/len(liste_notes)

print("Note minimale:", mini)
print("Note maximale:", maxi)
print("Moyenne:", moy)

# Exercice 4


from random import *
n1 = randint(0,100)
n2 = -1

while n2 != n1:
	n2 = input("Esssayer de deviner le nombre: ")
	if n2 < n1:
		print("plus haut...")
	elif n2 > n1:
		print("plus bas...")
print("Correct!")