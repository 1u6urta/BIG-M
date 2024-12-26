# BIG-M
BIG-M est une méthode du simplexe pour résoudre des problèmes d'optimisation linéaire
en utilisant soit la méthode standard du simplexe, soit l'approche de BIG-M pour traiter les contraintes d'égalité et d'inégalité 
≥
≥. Le programme est structuré pour :

Initialisation des paramètres :

Lecture des coefficients des variables décisionnelles.
Lecture des contraintes et des inégalités.
Transformation des contraintes pour s'assurer que les seconds membres 
𝐵
B sont positifs.
Préparation des tableaux :

Construction d'un tableau pour représenter les coefficients, les variables de base, les variables d'écart, les variables excédentaires et les variables artificielles si nécessaire.
Calcul des coefficients de la fonction objectif 
𝑍
Z, y compris les termes 
𝑀
M dans le cas de BIG-M.
Affichage :

Une fonction affichage_tab() affiche le tableau de simplexe avec un format bien cadré, facilitant la visualisation.
Pivotage :

Recherche de la colonne pivot en fonction des coefficients 
𝐶
𝑗
C 
j
​
  ou des termes 
𝑀
M dans BIG-M.
Calcul du rapport 
𝐵
/
𝐶
𝑃
B/CP pour identifier la ligne pivot.
Problèmes potentiels
Votre code semble incomplet ou coupé avant la fin du calcul du pivot. Voici quelques remarques pour le compléter :

Boucle principale :

Ajoutez la logique pour effectuer les itérations du simplexe en appliquant le pivotage et en mettant à jour les coefficients 
𝐴
A, 
𝐵
B, 
𝑍
Z, 
𝑀
M, etc.
Ajoutez une condition d'arrêt basée sur la convergence (tous les 
𝐶
𝑗
C 
j
​
  ou 
𝑀
M doivent être non positifs pour une maximisation, ou non négatifs pour une minimisation).
Gestion des erreurs :

Assurez-vous que la division par zéro est évitée lors du calcul de 
𝐵
/
𝐶
𝑃
B/CP.
Vérifiez la faisabilité initiale (par exemple, 
𝐵
≥
0
B≥0) pour éviter les résultats incorrects.
Documentation :

Commentez davantage les sections critiques du code pour améliorer la compréhension, surtout pour les variables comme VB, ConfZ, ConfM.
Optimisation et modularisation :

Divisez les grandes fonctions en sous-fonctions pour une meilleure lisibilité et réutilisabilité.
