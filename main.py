#devoir réalisé par Jade VINSON en classe de DIGBD 3ème année

#importation de la bibliotheque RE pour supprimer tous les espaces d'une chaîne de caractères
import re
#REMARQUE : Ce programme accepte toutes les chaînes qui sont formées exclusivement d'une combinaison arbitraire de "at", "ta", "gc" ou "cg"
# Et pour la séquence, ce programme accepte toutes les chaînes qui sont formées exclusivement de "a", "t", "g" et/ou "c"
# et contenant que 2 caractères



#saisie de la chaîne et de la séquence uniquement en STRING
chaine = str(input("Entrez la chaîne : "))
sequence = str(input("Entrez la séquence : "))

#suppression de tous les espaces AVANT & APRES & DEDANS
chaine = re.sub("\s+","",chaine)
sequence = re.sub("\s+","",sequence)

#mise de tous les caractères en minuscules
chaine = chaine.lower()
sequence = sequence.lower()

#comptage de la longueur de la chaîne de caractères rentrée soit le nombre de caractères de la chaîne
longueur = len(chaine)
longueurSequence = len(sequence)


#vérification CHAINE: vérifie si la chaîne entrée n'est pas vide et si la chaîne contient AU MOINS 2 caractères
while chaine is None or longueur <= 1:
    #si la chaine est vide
    # on demande à l'utilisateur de mettre une chaîne jusqu'à ce qu'elle soit remplie
    if chaine is not None:
        chaine = input("\nChaîne vide.\n"
                       "Une chaîne doit contenir AU MOINS 2 caractères.\n"
                       "Veuillez entrer une chaîne d'ADN : ")
    #la chaîne est trop longue
    # on demande à l'utilisateur de mettre une chaîne jusqu'à ce qu'elle soit superieure à 2
    else:
        chaine = input("\nChaîne pas assez longue.\n"
                       "Une chaîne doit contenir AU MOINS 2 caractères.\n"
                       "Veuillez entrer une chaîne d'ADN : ")

    #suppression de tous les espaces AVANT & APRES & DEDANS
    chaine = re.sub("\s+", "", chaine)
    # mise de tous les caractères en minuscules
    chaine = chaine.lower()
    # comptage de la longueur de la chaîne de caractères rentrée soit le nombre de caractères de la chaîne
    longueur = len(chaine)


#vérification SEQUENCE: vérifie si la séquence ne contient que 2 caractères et si les caracteres ne sont QUE des "a", "t", "g" et/ou "c"

#initialisation de la variable compteur
compteurHorsADNSequence = 0
#on parcourt la séquence pour compter le nombre de caracteres qui n'est pas un "a" ni un "t" ni un "g" ni un "c"
for i in sequence:
    # si la lettre parcourue n'est pas un "a" ni un "t" ni un "g" ni un "c"
    # on ajoute 1 au compteur
    if i not in ("a", "t", "g", "c"):
        compteurHorsADNSequence = compteurHorsADNSequence + 1


#tant que le compteur n'est pas égal à 0 demande à l'utilisateur d'entrer une nouvelle séquence
while compteurHorsADNSequence != 0:
    #la séquence contient des caracteres HORS "a", "t", "g" et/ou "c"
    # on demande à l'utilisateur de rentrer une nouvelle séquence
    sequence = input("\nSéquence invalide.\n"
                     "La séquence doit contenir UNIQUEMENT 2 caractères et être composée que des caractères \"a\", \"t\", \"g\" et/ou \"c\".\n"
                     "Veuillez entrer une séquence valide : ")
    #initialisation du compteur à 0
    compteurHorsADNSequence = 0

    # on parcourt la séquence pour compter le nombre de caracteres qui n'est pas un "a" ni un "t" ni un "g" ni un "c"
    for i in sequence:
        # si la lettre parcourue n'est pas un "a" ni un "t" ni un "g" ni un "c"
        # on ajoute 1 au compteur
        if i not in ("a", "t", "g", "c"):
            compteurHorsADNSequence = compteurHorsADNSequence + 1

    # comptage de la longueur de la chaîne de caractères rentrée soit le nombre de caractères de la sequence
    longueurSequence = len(sequence)
    compteurHorsADNSequence = compteurHorsADNSequence
    #tant que la longueur de la séquence n'est pas EGALE à 2
    # on redemande tant que la séquence ne fait pas deux caractères
    while longueurSequence != 2:
        if longueurSequence <= 1:
            sequence = input("\nSéquence trop courte.\n"
                             "La séquence doit contenir strictement 2 caractères.\n"
                             "Veuillez entrer une séquence avec uniquement 2 caractères : ")
            #initialisation à 0 du compteur
            compteurHorsADNSequence = 0
            #on parcourt la séquence caractère par caractère
            for i in sequence:
            # si la lettre parcourue n'est pas un "a" ni un "t" ni un "g" ni un "c"
            # on ajoute 1 au compteur
                if i not in ("a", "t", "g", "c"):
                    compteurHorsADNSequence = compteurHorsADNSequence + 1
            longueurSequence = len(sequence)

        elif longueurSequence > 2:
            sequence = input("\nSéquence trop longue.\n"
                             "La séquence doit contenir strictement 2 caractères.\n"
                             "Veuillez entrer une séquence plus courte : ")
            compteurHorsADNSequence = 0
            for i in sequence:
                # si la lettre parcourue n'est pas un "a" ni un "t" ni un "g" ni un "c"
                # on ajoute 1 au compteur
                if i not in ("a", "t", "g", "c"):
                    compteurHorsADNSequence = compteurHorsADNSequence + 1
            longueurSequence = len(sequence)

        compteurHorsADNSequence = compteurHorsADNSequence
        # suppression de tous les espaces AVANT & APRES & DEDANS
        sequence = re.sub("\s+", "", sequence)
        # mise de tous les caractères en minuscules
        sequence = sequence.lower()
        longueurSequence = len(sequence)


#fonction VALIDE : vérifie que la saisie est valide
# si la saisie est formée exclusivement d'une combinaison arbitraire de "at", "ta", "gc" ou "cg"
# ET si la saisie est formée uniquement des caractères "a", "t", "g" et/ou "c"
# renvoie vrai si la saisie est valide, faux sinon.
def valide(chaine):
    chaine = str(chaine)

    #compteur de la position lorsque la chaîne est parcourue
    compteur = 0

    #compteur pour indiquer si il y a des caractères hors "a", "t", "g" et/ou "c"
    compteurHorsADN = 0
    #compteur pour indiquer si la lettre a été parcourue
    compteurC = 0
    compteurG = 0
    compteurA = 0
    compteurT = 0
    #compteur pour indiquer les couples formés parcourus
    compteurCG = 0
    compteurGC = 0
    compteurAT = 0
    compteurTA = 0

    #on parcourt la chaîne entrée, caractère par caractère
    for i in chaine:

        #si la lettre parcourue n'est pas un "a" ni un "t" ni un "g" ni un "c"
        # on ajoute 1 au compteur
        if i not in ("a", "t", "g", "c"):
            compteurHorsADN = compteurHorsADN + 1

        #si la lettre parcourue est c
        if i == "c":
            compteurC = 1
            # si le compteur de G est à 1 et que la lettre précédent le C est un G alors
            if compteurG == 1 and str(chaine[compteur - 1]) == "g":
                compteurCG = compteurCG + 1
                compteurC = 0
                compteurG = 0

        if i == "g":
            compteurG = 1
            # si le compteur de C est à 1 et que la lettre précédent le G est un C alors
            if compteurC == 1 and str(chaine[compteur - 1]) == "c":

                compteurGC = compteurGC + 1
                compteurC = 0
                compteurG = 0

        if i == "a":
            compteurA = 1
            # si le compteur de T est à 1 et que la lettre précédent le  est un C alors
            if compteurT == 1 and str(chaine[compteur - 1]) == "t":
                #on ajoute 1 au compteur AT
                compteurAT = compteurAT + 1
                compteurA = 0
                compteurT = 0

        if i == "t":
            compteurT = 1
            # si le compteur de C est à 1 et que la lettre précédent le G est un C alors
            if compteurA == 1 and str(chaine[compteur - 1]) == "a":
                compteurTA = compteurGC + 1
                compteurA = 0
                compteurT = 0

        #compteur de la position actuelle sur la chaîne de caractères
        # On ajoute 1 a chaque passage dans la boucle
        compteur = compteur + 1

    # verification de si la chaîne est valide si elle contient
    # AUCUN caractère HORS "a", "t", "g" et/ou "c"

    if compteurHorsADN == 0:
        # AU MOINS UNE combinaison CG OU GC OU AT OU TA
        if compteurCG >= 1 or compteurGC >= 1 or compteurAT >= 1 or compteurTA >= 1:
            return 1
    else:
        #si le compteur de caracteres HORS est égal ou supérieur à 1 la saisie est fausse
        if compteurHorsADN >= 1:
            print("La chaîne n'est pas valide.\n"
                  "Il y a ", compteurHorsADN, "caractères qui ne sont pas des \"a\", \"t\", \"c\" et/ou \"g\".\n"
                        "Veuillez entrer une chaîne qui ne contient que des \"a\", \"t\", \"c\" et/ou \"g\".")
        # retourne faux si la fonction n'est pas valide
            return 0

#fonction SAISIE si la saisie est VALIDE
# execute ma fonction proportion
def saisie(chaine,sequence):
    #vérifie si la chaine est valide, le 1 est une référence au return de la fonction VALIDE
    if valide(chaine) == 1:
        #execution de la fonction PROPORTION
        proportion(chaine, sequence)
        #le return demandée par la consigne pour fonction SAISIE mais ne va pas pour l'option d'affichage
        #return chaine
    else:
        print("La chaîne est invalide car elle ne contient aucune combinaison \"at\", \"ta\", \"gc\" ou \"cg\".")
        return 0

#fonction PROPORTION prend deux paramètres, la chaîne et la séquence
# retourne la proportion de séquence dans la chaîne
def proportion(chaine, sequence):
    compteur = 0

    compteur1 = 0
    compteur2 = 0
    compteur12 = 0
    compteur21 = 0

    #on met dans deux variables différentes
    # le premier et le deuxième caractère de la séquence
    premiereSequence = str(sequence[0])
    deuxiemeSequence = str(sequence[1])

    #on parcourt la chaîne de caractères saisie par l'utilisateur
    # un à un, caractère par caractère
    for i in chaine:

        #si le caractère parcourue est le même que premier caractère de la séquence
        # on met le compteur à 1
        if i == premiereSequence:
            compteur1 = 1

        # si le caractère parcourue est le même que le deuxième caractère de la séquence
        # on met le compteur à 1
        if i == deuxiemeSequence:
            compteur2 = 1
            # si le compteur de la premiere sequence est à 1 et que le caractère précédent le même que  le premier caractère de la séquence
            if compteur1 == 1 and str(chaine[compteur - 1]) == premiereSequence:
                #on ajoute 1 au compteur
                compteur12 = compteur12 + 1
                compteur1 = 0
                compteur2 = 0

        # compteur de la position actuelle sur la chaîne de caractères
        # On ajoute 1 a chaque passage dans la boucle
        compteur = compteur + 1

    #calcul du pourcentage en fonction du nombre d'occurrences par rapport à la longueur de la chaine
    pourcentageSequence = (compteur12 * 100) / longueur
    #on arrondit le pourcentage au centième
    pourcentageSequence = round(pourcentageSequence, 2)
    print("Il y a ", pourcentageSequence, "% de \"", sequence, "\" dans votre chaîne.")
    #return print("Il y a ", pourcentageSequence, "% de \"", sequence, "\" dans votre chaîne.")
    return pourcentageSequence

#print(saisie(chaine,sequence))

resultat = saisie(chaine,sequence)
print(resultat)