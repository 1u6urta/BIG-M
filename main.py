def affichage_tab():  # Fonction D'affichage Du Tableau De Simplexe
    tab = [["" for _ in range(0)] for _ in range(nbrCon + 2)]  # Initialisation D'une Table Vide
    Tete_Tab = ["x" + str(ii + 1) for ii in range(nbrVar)] + ["e" + str(ii + 1) for ii in range(nbrnonT - nbrVar)]
    Tete_Tab += ["t" + str(ii + 1) for ii in range(nbrvarTotal - nbrnonT)] + ["B"]
    tab[0] = Tete_Tab  # Remplir La Tete Du Tableau ( x1 x2 .. xn e1 e2 .. en t1 t2 .. tn )
    for ii in range(nbrCon):
        # Remplir Les Variables De Bases Dans La 1ère Colonne Du Tableau
        tab[ii + 1].insert(0, VB[ii])
    tab[0].insert(0, "Base")  # Remplir Le Mot Base Dans La 1ère Case De La 1ère Colonne Du Tableau
    tab[-1].insert(0, "-z")  # Remplir Le Mot -z Dans La Dernière Case De La 1ère Colonne Du Tableau
    for ii in range(nbrCon):
        for jj in range(nbrvarTotal):
            Ai = str(A[ii][jj]) if A[ii][jj] < 0 else " " + str(A[ii][jj])
            tab[ii + 1].append(Ai)  # Remplir La Matrice A Comme Une Chaine De Caractère  Dans Le Tableau
        tab[ii + 1].append(str(B[ii]))  # Remplir Le Vecteur B Comme Une Chaine De Caractère  Dans Le Tableau
    if not BiG_M:  # Si La Méthode De Simplexe
        for ii in range(nbrvarTotal):
            tab[-1].append(str(ConfZ[ii]))  # Remplir Le Vecteur ConfZ Comme Une Chaine De Caractère  Dans Le Tableau
        tab[-1].append(str(B[nbrCon]))
        # Remplir B De La Fonction Objectif Comme Une Chaine De Caractère  Dans Le Tableau
    else:  # Si La Méthode De BiG-M
        for ii in range(nbrvarTotal):
            OPA = "+" if ConfZ[ii] > 0 and ConfM[ii] != 0 else ""
            BIGM = "" if ConfM[ii] == 0 else str(ConfM[ii]) + "M"
            Ci = "" if ConfZ[ii] == 0 and ConfM[ii] != 0 else str(ConfZ[ii])
            # La Concaténation De ConfM et La Lettre M et ConfZ
            tab[-1].append(BIGM + OPA + Ci)  # Remplir La Concaténation
    BIGM = "" if BM == 0 else str(BM) + "M"
    OPA = "+" if B[nbrCon] > 0 else ""
    Bi = "" if B[nbrCon] == 0 and BM != 0 else str(B[nbrCon])
    # La Concaténation De BM et La Lettre M et B De La Fonction Objectif
    tab[-1].append(BIGM + OPA + Bi)  # Remplir La Concaténation
    nbrCol = nbrvarTotal + 2  # nbrCol : Nombre De Colonne
    len_max_Col = [0] * nbrCol  # Initialisation De Liste len_max_Col
    # len_max_Col La Plus Grande Chaine De Caractère Dans Chaque Colonne de Tableau
    for ii in range(nbrCol):
        len_max_Col[ii] = max(len(tab[jj][ii]) for jj in range(nbrCon + 2))
        # Rechercher La Plus Grande Chaine De Caractère Dans La Colonne ii
    # Les Caractères - et | Pour Dessiner Le Cadre De La Table
    # Et Nous Avons utilisé La Liste len_max_Col Pour Bien Cadré
    print("\n\t-", end="")
    for ii in range(nbrCol):
        print("-" * (len_max_Col[ii] + 3), end="")
    print("\n\t|", end="")
    for ii in range(nbrCol):
        elem = tab[0][ii]
        print('', elem, ' ' * (len_max_Col[ii] - len(elem)) + '|', end="")
    print("\n\t-", end="")
    for ii in range(nbrCol):
        print("-" * (len_max_Col[ii] + 3), end="")
    for ii in range(1, nbrCon + 2):
        print("\n\t|", end="")
        for jj in range(nbrCol):
            elem = tab[ii][jj]
            print('', elem, ' ' * (len_max_Col[jj] - len(elem)) + '|', end="")
    print("\n\t-", end="")
    for ii in range(nbrCol):
        print("-" * (len_max_Col[ii] + 3), end="")


OP = []
A = []
ConfZ = []
B = []

maxomin = input("Maximise Ou Minimise (max ou min) : ")  # maxomin : max || min

nbrVar = int(input("Donnes Le Nombre De Variables Décision : "))  # nbrvar : Le Nombre De Variables Décision
for i in range(nbrVar):
    # Remplir Les Coefficients Des Variables Dans La Fonction Objectif Z
    print("Donnes Le Coefficient De La Variable Num ", i + 1, " Dans La Fonction Z : ", sep='', end="")
    ConfZ.append(int(input()))  # Stocker Les Coefficients Dans La Liste ConfZ (Vecteur)

nbrCon = int(input("Donnez Le Nombre de Contraintes : "))  # nbrCon : Le Nombre de Contraintes
for i in range(nbrCon):
    Line = []
    for j in range(nbrVar):
        print("Donnez Le Coefficient De La Variable Num ", j + 1, " Dans La Contraite Num ", i + 1, " : ", end="",
              sep='')
        Line.append(int(input()))
    A.append(Line)
    # Stocker Les Coefficients Des Variables De Chaque Contraite Dans La Liste imbriquée A ( Matrice )
    print("Donnez Les Inégalités ( <= , = , >= ) : ", end="", sep='')
    OP.append(input())  # Stocker Les Inégalités Dans La Liste OP
    print("Donnez La Valeur De Second Membre B", i + 1, " : ", end="", sep='')
    B.append(int(input()))  # Stocker Les Valeurs Des Second Membre Bi Dans La Liste B
B.append(0)  # Ajoutant Une Case Dans La Liste B Pour Le 0 De La Fonction Objectif  exemple -z + x1 + x2 = 0

Bn = []
# Si Il y a Un Second membre Bi il Changer La Contraite Num i
for i in range(nbrCon):
    if B[i] < 0:
        for j in range(nbrVar):
            A[i][j] = -A[i][j]
        B[i] = -B[i]
        if OP[i] == ">=":
            OP[i] = "<="
        elif OP[i] == "<=":
            OP[i] = ">="
        Bn.append(i)

# Affiche La Fonction Objectif
print("Donc ", maxomin, " Z = ", end="", sep='')
Tmp = 0
for i in range(nbrVar):
    if ConfZ[i] != 0:
        Tmp += 1
        print(ConfZ[i], "x", i + 1, " ", end="", sep='')
    if i + 1 == nbrVar:
        print("\n")
        continue
    if ConfZ[i + 1] > 0 and Tmp > 0:
        print("+", end="")

if len(Bn) > 0:
    pri = ["B" + str(i + 1) for i in Bn]
    print("\tLe Second membre ", pri, " Doit Etre Positif")

# Affiche Les Contraintes
print("Donc SC :")
for i in range(nbrCon):
    Tmp = 0
    print(" \t \t ", end="")
    for j in range(nbrVar):
        if A[i][j] != 0:
            Tmp += 1
            print(A[i][j], "x", j + 1, " ", end="", sep='')
        if j + 1 == nbrVar:
            print(OP[i], B[i], )
            continue
        if A[i][j + 1] > 0 and Tmp > 0:
            print("+", end="")

nbrvarTotal = nbrVar  # Le Nombre Des Variables Totales (  Décision + D'écart + D'excédent + Artificielles T )
nbrnonT = nbrVar  # Le Nombre Des Variables non Artificielles T (  Décision + D'écart + D'excédent )
VB = ["" for i in range(nbrCon)]  # Initialisation De La Liste Des Variables De Bases

for i in range(nbrCon):

    # Ajouter Les Variables D'écart
    if OP[i] == "<=":
        nbrvarTotal += 1  # Incrémentation Des Variables Totales
        nbrnonT += 1  # Incrémentation Des Variables non Artificielles T
        VB[i] = "e" + str(nbrnonT - nbrVar)  # Remplir La Liste Des Variables De Bases
        for j in range(nbrCon):
            if j == i:
                A[j].append(1)
            else:
                A[j].append(0)
        ConfZ.append(0)

    # Ajouter Les Variables D'excédent
    elif OP[i] == ">=":
        nbrvarTotal += 1  # Incrémentation Des Variables Totales
        nbrnonT += 1  # Incrémentation Des Variables non Artificielles T
        for j in range(nbrCon):
            if j == i:
                A[j].append(-1)
            else:
                A[j].append(0)
        ConfZ.append(0)

# Ajouter les variables Artificielles T
for i in range(nbrCon):
    if OP[i] == ">=" or OP[i] == "=":
        nbrvarTotal += 1  # Incrémentation Des Variables Totales
        VB[i] = "t" + str(nbrvarTotal - nbrnonT)  # Remplir La Liste Des Variables De Bases
        for j in range(nbrCon):
            if j == i:
                A[j].append(1)
            else:
                A[j].append(0)
        ConfZ.append(0)

input("\n\nVeuillez Cliqué sur n'importe quel touche ! Pour Résoudre Ce PL ")

BiG_M = (nbrvarTotal != nbrnonT)
# La Variable Boolean Si Le Nombre Des Variables Totales == Le Nombre Des Variables non Artificielles T
# Alors BiG_M = False ( Donc La Méthode Utilisée c'est Simplexe ) Sinon La Méthode Utilisée c'est BiG_M
ConfM = []  # Initialisation De La Liste Des Coefficients De BIG-M Dans La Fonction Objectif Z
BM = 0  # Initialisation De La Liste Des Coefficients De BIG-M Dans Le Vecteur Bi
if not BiG_M:
    print("\n\n \t\t La Méthode De Simplexe ")
else:
    print("\n\n \t\t La Méthode De BIG-M ")
    for i in range(nbrnonT):
        ConfM.append(0)  # Initialisation Des Coefficients De BIG-M Dans La Fonction Objectif Z à 0
    # Remplir La Liste Des Coefficients De BIG-M
    for i in range(nbrCon):
        if OP[i] == ">=" or OP[i] == "=":
            ConfM.append(0)
            for j in range(nbrnonT):
                if maxomin == "max":
                    ConfM[j] += A[i][j]
                else:
                    ConfM[j] -= A[i][j]
            if maxomin == "max":
                BM += B[i]
            else:
                BM -= B[i]

affichage_tab()  # L'Appel à La Fonction D' Affichage du Tableau De Simplexe pour k = 0

# Initialisation Des Variables
Cj = ConfZ[0]
CM = ConfM[0] if BiG_M else 0
indices_j = 0  # Indice De La Colonne Pivot
indices_i = 0  # Indice De La Ligne Pivot
MinBCP = B[0] / A[0][indices_j]  # Initialisation De B/CP
Pivot = 1  # Initialisation De Pivot
for i in range(nbrvarTotal):  # Rechercher La Colonne Pivot
    if not BiG_M:
        if maxomin == "max":
            if ConfZ[i] > Cj and ConfZ[i] > 0:  # Le Maximum Positif
                Cj = ConfZ[i]
                indices_j = i
        else:  # maxomin == "min"
            if ConfZ[i] < Cj and ConfZ[i] < 0:  # Le Minimum Négatif
                Cj = ConfZ[i]
                indices_j = i
    # Si BiG-M La Comparaison Des Coefficients M
    else:
        if maxomin == "max":
            # Le Maximum Positif Des Coefficients M
            if ConfM[i] > CM and ConfM[i] > 0:
                CM = ConfM[i]
                Cj = ConfZ[i]
                indices_j = i
            # Si il y a Deux Ou Plus Maximum Positifs Dans Les  Coefficients M  ( 2M   2M+1 )
            # On Compare Les Coefficients De Z Dans Ce Cas C'est 2M+1
            elif ConfM[i] == CM:
                if ConfZ[i] > Cj:
                    Cj = ConfZ[i]
                    indices_j = i
        else:
            # Le Minimum Négatif Le  Des Coefficients M
            if ConfM[i] < CM and ConfM[i] < 0:
                CM = ConfM[i]
                indices_j = i
            # Si il y a Deux Ou Plus Minimum négatifs Dans Les  Coefficients M  ( -2M   -2M-1 )
            # On Compare Les Coefficients De Z  Dans Ce  C'est -2M-1
            elif ConfM[i] == CM:
                if ConfZ[i] < Cj:
                    Cj = ConfZ[i]
                    indices_j = i

# Rechercher Un Minimum dans B/CP
for i in range(nbrCon):
    if (B[i] / A[i][indices_j]) < MinBCP and B[i] / A[i][indices_j] > 0:
        MinBCP = B[i] / A[i][indices_j]
        indices_i = i

# Rechercher Une Nouvelle Variable De Base
if indices_j < nbrVar:
    Le = 'x'
    Num = indices_j + 1
elif indices_j < nbrnonT:
    Le = 'e'
    Num = indices_j - nbrVar
else:
    Le = 't'
    Num = indices_j - nbrnonT
VHB = VB[indices_i]  # Nouvelle Variable Hors Base
VB[indices_i] = Le + str(Num)  # Nouvelle Variable De Base

Pivot = A[indices_i][indices_j]  # Le Pivot

print("\n\nNouvelle Variable De Base Est :", VB[indices_i], ", j = ", indices_j + 1)
print("Nouvelle Variable Hors De Base Est :", VHB, ", i = ", indices_i + 1)
print("Le Pivot Est : ", "A", indices_i + 1, indices_j + 1, " = ", Pivot, sep='')
input("\n\nVeuillez Cliqué Sur N'importe Quel Touche ! Pour Affiche Le Tableau De Simplexe Pour k = 1")

# La Procédure D'élimination De Gauss-Jordan
for j in range(nbrvarTotal):
    A[indices_i][j] /= Pivot
B[indices_i] /= Pivot
for i in range(nbrCon):
    if i != indices_i:
        Aij = A[i][indices_j]  # Aij De La Colonne Pivot
        for j in range(nbrvarTotal):
            A[i][j] -= A[indices_i][j] * Aij
        B[i] -= B[indices_i] * Aij

# La Procédure D'élimination De Gauss-Jordan Dans La Derniére Ligne
Aij = ConfZ[indices_j]  # Le Coefficient De La Colonne Pivot De La Derniére Ligne ( La Fonction Objectif Z )
Mij = ConfM[indices_j] if BiG_M else 0
# Le Coefficient BIG-M De La Colonne Pivot De La Derniére Ligne ( La Fonction Objectif Z )
for i in range(nbrnonT):
    if BiG_M:
        ConfM[i] -= A[indices_i][i] * Mij
    ConfZ[i] -= A[indices_i][i] * Aij
B[nbrCon] -= B[indices_i] * Aij
if BiG_M:
    BM -= B[indices_i] * Mij

affichage_tab()  # L'Apple à Fonction De Affichage Le Tableau De Simplexe pour k = 1

# Initialisation Des Variables
Cj = ConfZ[0]
CM = ConfM[0] if BiG_M else 0
indices_j = 0  # Indice De La Colonne Pivot
indices_i = 0  # Indice De La Ligne Pivot
MinBCP = B[0] / A[0][indices_j]  # Initialisation De B/CP
Pivot = 1  # Initialisation De Pivot
for i in range(nbrvarTotal):  # Rechercher La Colonne Pivot
    if not BiG_M:
        if maxomin == "max":
            if ConfZ[i] > Cj and ConfZ[i] > 0:  # Le Maximum Positif
                Cj = ConfZ[i]
                indices_j = i
        else:  # maxomin == "min"
            if ConfZ[i] < Cj and ConfZ[i] < 0:  # Le Minimum Négatif
                Cj = ConfZ[i]
                indices_j = i
    # Si BiG-M La Comparaison Des Coefficients M
    else:
        if maxomin == "max":
            # Le Maximum Positif Des Coefficients M
            if ConfM[i] > CM and ConfM[i] > 0:
                CM = ConfM[i]
                Cj = ConfZ[i]
                indices_j = i
            # Si il y a Deux Ou Plus Maximum Positifs Dans Les  Coefficients M  ( 2M   2M+1 )
            # On Compare Les Coefficients De Z Dans Ce Cas C'est 2M+1
            elif ConfM[i] == CM:
                if ConfZ[i] > Cj:
                    Cj = ConfZ[i]
                    indices_j = i
        else:
            # Le Minimum Négatif Le  Des Coefficients M
            if ConfM[i] < CM and ConfM[i] < 0:
                CM = ConfM[i]
                indices_j = i
            # Si il y a Deux Ou Plus Minimum négatifs Dans Les  Coefficients M  ( -2M   -2M-1 )
            # On Compare Les Coefficients De Z  Dans Ce  C'est -2M-1
            elif ConfM[i] == CM:
                if ConfZ[i] < Cj:
                    Cj = ConfZ[i]
                    indices_j = i

# Rechercher Un Minimum dans B/CP
for i in range(nbrCon):
    if (B[i] / A[i][indices_j]) < MinBCP and B[i] / A[i][indices_j] > 0:
        MinBCP = B[i] / A[i][indices_j]
        indices_i = i

# Rechercher Une Nouvelle Variable De Base
if indices_j < nbrVar:
    Le = 'x'
    Num = indices_j + 1
elif indices_j < nbrnonT:
    Le = 'e'
    Num = indices_j - nbrVar
else:
    Le = 't'
    Num = indices_j - nbrnonT
VHB = VB[indices_i]  # Nouvelle Variable Hors Base
VB[indices_i] = Le + str(Num)  # Nouvelle Variable De Base

Pivot = A[indices_i][indices_j]  # Le Pivot

print("\n\nNouvelle Variable De Base Est :", VB[indices_i], ", j = ", indices_j + 1)
print("Nouvelle Variable Hors De Base Est :", VHB, ", i = ", indices_i + 1)
print("Le Pivot Est : ", "A", indices_i + 1, indices_j + 1, " = ", Pivot, sep='')
