# supreme-octo-potato
## Des exercices proposés par chatgpt pour apprendre Python

Bien sûr, voici quelques exercices simples pour apprendre Python :

1. Afficher "Hello World!" à l'écran.

2. Créer une variable pour stocker votre nom et afficher "Bonjour, [votre nom]!" à l'écran.

3. Créer une liste de nombres et afficher la somme de tous les nombres dans la liste.

4. Demander à l'utilisateur d'entrer un nombre et afficher si ce nombre est pair ou impair.

5. Créer une boucle qui affiche tous les nombres de 1 à 10.

6. Créer une fonction qui prend deux nombres en entrée et retourne leur somme.

7. Créer une fonction qui prend une liste en entrée et retourne la valeur maximale de la liste.

8. Créer une classe pour représenter une voiture avec des attributs tels que la marque, le modèle et la couleur.

9. Créer une fonction qui prend un mot en entrée et retourne True si le mot est un palindrome (c'est-à-dire qu'il se lit de la même manière de gauche à droite et de droite à gauche), et False sinon.

10. Créer une boucle qui affiche tous les nombres premiers de 1 à 50.

Ces exercices simples peuvent vous aider à apprendre les bases de la programmation en Python. Bonne chance !

## Solutions
### Exercice 1 
```python
print("Hello World!")
```

### Exercice 2
```python
nom = "phozon"
print("Hello " + nom)
```

### Exercice 3
Pour réaliser l'exercice 3, vous pouvez suivre les étapes suivantes :

1. Créez une liste de nombres en Python en utilisant des crochets [ ] et en séparant les nombres par des virgules. Par exemple, [2, 4, 6, 8].

2. Initialisez une variable appelée "somme" à 0.

3. Utilisez une boucle for pour parcourir tous les nombres de la liste.

4. Ajoutez chaque nombre à la variable "somme".

5. Affichez la somme totale en utilisant la fonction print().

Voici un exemple de code Python pour réaliser cela :
```python
numbers = [2, 4, 6, 8] # Exemple de liste de nombres
sum = 0 # Initialisation de la variable somme

for num in numbers:
    sum += num # Ajout du nombre courant à la variable somme

print("La somme est :", sum) # Affichage de la somme totale
```

Dans cet exemple, la liste "numbers" contient les nombres 2, 4, 6 et 8. La boucle for parcourt chaque nombre de la liste et l'ajoute à la variable "sum". Finalement, la somme totale est affichée à l'aide de la fonction print().

Vous pouvez modifier cette exemple en remplaçant les nombres par votre propre liste de nombres.

### Exercice 4
Voici un indice pour réaliser l'exercice 4 :

1. Utilisez la fonction input() pour demander à l'utilisateur d'entrer un nombre.

2. Stockez le nombre entré par l'utilisateur dans une variable en utilisant la fonction int() pour convertir l'entrée en un nombre entier.

3. Utilisez une condition if pour vérifier si le nombre est pair ou impair.

4. Affichez un message à l'utilisateur en utilisant la fonction print() pour lui dire si le nombre est pair ou impair.

Voici un exemple de code Python pour réaliser cela :
```python
number = int(input("Entrez un nombre : ")) # Demander à l'utilisateur d'entrer un nombre

if number % 2 == 0:
    print(number, "est un nombre pair.") # Afficher un message si le nombre est pair
else:
    print(number, "est un nombre impair.") # Afficher un message si le nombre est impair

```
Dans cet exemple, la fonction input() est utilisée pour demander à l'utilisateur d'entrer un nombre. Le nombre entré par l'utilisateur est stocké dans la variable "number" en utilisant la fonction int() pour le convertir en un nombre entier. La condition if vérifie si le nombre est pair en utilisant l'opérateur modulo (%), qui renvoie le reste de la division du nombre par 2. Si le reste est égal à zéro, alors le nombre est pair, sinon il est impair. Finalement, un message est affiché à l'utilisateur pour lui indiquer si le nombre est pair ou impair.

### Exercice 5
voici un indice pour réaliser l'exercice 5 :

1. Utilisez une boucle for pour parcourir les nombres de 1 à 10.

2. À chaque itération de la boucle, utilisez la fonction print() pour afficher le nombre courant.

Voici un exemple de code Python pour réaliser cela :
```python
for i in range(1, 11):
    print(i)
```
Dans cet exemple, la boucle for utilise la fonction range() pour parcourir les nombres de 1 à 10 (en excluant le nombre 11). À chaque itération de la boucle, le nombre courant est affiché à l'aide de la fonction print(). Vous pouvez modifier les limites de la plage d'itération (par exemple, pour parcourir les nombres de 1 à 20) en modifiant les arguments de la fonction range().

### Exercice 6
 voici comment réaliser l'exercice 6 :

1. Définissez une fonction en utilisant le mot-clé def suivi du nom de la fonction et de deux paramètres.

2. À l'intérieur de la fonction, ajoutez les deux paramètres ensemble.

3. Utilisez le mot-clé return suivi du résultat pour renvoyer la somme des deux nombres.

Voici un exemple de code Python pour réaliser cela :
```python
def addition(a, b):
    somme = a + b
    return somme

# Appel de la fonction avec les nombres 2 et 3
resultat = addition(2, 3)
print(resultat) # Affiche 5

```
Dans cet exemple, une fonction appelée "addition" est définie avec deux paramètres, "a" et "b". À l'intérieur de la fonction, les deux paramètres sont ajoutés ensemble et stockés dans la variable "somme". Le mot-clé return est utilisé pour renvoyer la somme des deux nombres. Enfin, la fonction est appelée avec les nombres 2 et 3 et le résultat est stocké dans la variable "resultat", qui est affichée à l'aide de la fonction print().

Alternative avec input utilisateur: 

voici comment réaliser la même fonctionnalité, mais en utilisant les deux paramètres entrés par l'utilisateur :

```python
def addition():
    a = int(input("Entrez un nombre : "))
    b = int(input("Entrez un autre nombre : "))
    somme = a + b
    return somme

# Appel de la fonction
resultat = addition()
print(resultat)
```
Dans cet exemple, la fonction "addition" est définie sans aucun paramètre. À l'intérieur de la fonction, la fonction input() est utilisée deux fois pour demander à l'utilisateur d'entrer deux nombres, qui sont ensuite convertis en entiers à l'aide de la fonction int(). Les deux nombres sont ensuite ajoutés ensemble et stockés dans la variable "somme". Le mot-clé return est utilisé pour renvoyer la somme des deux nombres.

Enfin, la fonction est appelée sans aucun argument et le résultat est stocké dans la variable "resultat", qui est affichée à l'aide de la fonction print().

### Exercice 7
voici comment réaliser l'exercice 7 :

1. Définissez une fonction en utilisant le mot-clé def suivi du nom de la fonction et d'un paramètre.

2. À l'intérieur de la fonction, utilisez la fonction max() pour trouver la valeur maximale de la liste.

3. Utilisez le mot-clé return suivi de la valeur maximale pour renvoyer la valeur maximale de la liste.

Voici un exemple de code Python pour réaliser cela :

```python
def valeur_maximale(liste):
    max_val = max(liste)
    return max_val

# Appel de la fonction avec une liste
ma_liste = [1, 5, 3, 8, 2]
resultat = valeur_maximale(ma_liste)
print(resultat) # Affiche 8
```
Dans cet exemple, une fonction appelée "valeur_maximale" est définie avec un paramètre "liste". À l'intérieur de la fonction, la fonction max() est utilisée pour trouver la valeur maximale de la liste et stocker cette valeur dans la variable "max_val". Le mot-clé return est utilisé pour renvoyer la valeur maximale de la liste.

Enfin, la fonction est appelée avec une liste de nombres, le résultat est stocké dans la variable "resultat", qui est affichée à l'aide de la fonction print().

