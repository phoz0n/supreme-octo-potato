''''Afficher "Hello World!" à l'écran.'''
print("Hello World!")

'''Créer une variable pour stocker votre nom et afficher "Bonjour, [votre nom]!" à l'écran.'''
nom = "phozon"
print("Hello " + nom)

'''Créer une liste de nombres et afficher la somme de tous les nombres dans la liste.'''
nombres = [1,2,3,4,5,6]
somme = 0

for nomb in nombres:
    somme += nomb

nombres_str = ' '.join(map(str, nombres))
print("Voici la liste des nombres", nombres_str)
print("Résultat de l'addition de cette liste", somme)

'''Demander à l'utilisateur d'entrer un nombre et afficher si ce nombre est pair ou impair.'''
nombre_choisi = int(input("Entrez un nombre : "))
if nombre_choisi % 2 == 0:
    print(nombre_choisi, "est un nombre pair.")
else:
    print(nombre_choisi, "est un nombre impair.")

'''Créer une boucle qui affiche tous les nombres de 1 à 10.'''
print("Liste de 1 à 10:", end=" ")
for i in range(1,11):
    if i != 10:
        print(i, end=" ")
    else:
        print(i, end="\n")
        
'''Créer une fonction qui prend deux nombres en entrée et retourne leur somme.'''
def addition():
    a = int(input("Choisir 1er nombre: "))
    b = int(input("Puis choisir 2eme nombre: "))    
    somme = a + b
    return somme

resultat = addition()
print ("Résultat de l'addition", resultat)

'''Créer une fonction qui prend une liste en entrée et retourne la valeur maximale de la liste.'''
def valMax(liste):
    max_val = max(liste)
    return max_val

ma_liste = [1,24,3,9,5,6]
ma_liste_str = ' '.join(map(str, ma_liste))
resultat = valMax(ma_liste)
print("la valeur maximale de la liste", ma_liste_str, "est",  resultat)
