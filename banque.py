from os.path import \
    exists  # os.path est utilisé dans la fonction nouveau pour vérifier si une compte avec un nom d'utilisateur existe.
import os  # os utilisé pour supprimer un compte.


def nouveau(entre):
    """   Permet de créer un nouveau compte et fichier dans la base de données.
    """

    print("Bienvenue à la banque FrancoBanque!")
    while True:  # Boucle pour créer un nouveau compte.
        strnouveauutilisateur = input("Entrer votre nouveau nom d'utilisateur ici: ")
        if exists(
                strnouveauutilisateur) == False:  # Vérifie si le nom d'utilisateur entrée existe dans le système ou non. S'il existe, un message apparaît pour informer l'utilisateur que le nom d'utilisateur est déjà pris.
            strmotdepasse = input("Entrer votre nouveau mot de passe ici: ")
            print("Bienvenue à ton nouveau compte!")
            with open(strnouveauutilisateur,
                      'a') as database:  # Permet d'écrire le mot de passe et un nouveau compte dans le ficher de texte de l'utilisateur.
                database.write(strmotdepasse)
                database.write("\n0\n")
            return strnouveauutilisateur, True  # Retourne le nouveau nom d'utilisateur dans le programme, ainsi que de rendre la variable login vrai.
            break
        else:
            print("Nom d'utilisateur est déjà pris. Essayez encore. ")


def login(login):
    """ Fonction qui permet d'entrer dans un compte existante."""

    while login == False:
        try:  # Try et except permet d'éviter un crash si un nom d'utilisateur invalide est entré.
            strnomutil = input("Entrer votre nom utilisateur ici: ")
            strmotpas = input("Entrer votre mot de passe ici: ")
            with open(strnomutil, 'r') as log:
                if log.readline().split("\n")[
                    0] == strmotpas:  # Vérifie si le mot de passe est le même que celui de l'un qui est sauvegardé dans le texte fichier du compte.
                    print(f"Bienvenue à ton compte {strnomutil}! ")
                    return strnomutil, True
                else:
                    print("Mauvais mot de passe.")
                    strsortie = input(
                        "Voulez-vous sortir par la suite? (Q ou q pour oui: ")  # Permet de sortir du menu de login.
                    if strsortie.lower() == "q":  # Permet de retourner deux str vides pour éviter un crash du programme.
                        return "", ""
                        break
        except:
            print("Login a failli. Essayez encore avec un nouveau nom d'utilisateur. ")
            strsortie = input(
                "Voulez-vous sortir? (Q ou q pour quitter, entrer n'importe quel autre entrée pour continuer: ")
            if strsortie.lower() == "q":
                return "", ""  # Prévient que le programme fait un crash quand il retourne le nom d'utilisateur et rendre login vrai.
                break


def ajoute(fltajoute, intcarte, listvaleurs):
    """ Permet d'ajouter ou de retirer de l'argent d'un compte."""

    while True:
        print(""" 
              Voulez-vous ajouter ou enlever de l'argent? 
                          1. Ajouter
                          2. Enlever


                          """)
        intinpchoix = input("Choix: ")
        if intinpchoix == "1":  # Ajoute le montant voulue à la balance du compte.
            fltsomme = fltajoute + float(listvaleurs[intcarte])
            break
        elif intinpchoix == "2" and fltajoute < float(listvaleurs[
                                                          intcarte]):  # Soustraire le montant voulue du compte seulement si le compte a assez d'argent.
            fltsomme = float(listvaleurs[intcarte]) - fltajoute
            break
        else:
            print("Choix invalide. Essayez encore.")
    listvaleurs[intcarte] = str(f"{fltsomme}\n")  # La valeur du balance est mis à jour dans la liste des comptes.
    print(f"Succès! Voici votre somme d'argent: {fltsomme}")
    return listvaleurs  # Il est retourné au programme principale.


def Interet(strutil, intcarte):
    """ Fonction qui permet de calculer l'fltintérêt d'un mini-compte en particulier par l'entrée d'un taux d'fltintérêt, et le nombre d'années.
    """

    while True:
        try:
            print(""" Notez que la banque calcule l'intérêt 2 fois par année. """
                  )
            fltvalint = float(input("Entrer le taux d'intérêt que vous voulez calculer: "))
            intvaltemps = int(input("Entrer le nombre d'années que vous voulez calculer: "))
            if fltvalint > 0 and intvaltemps > 0 and fltvalint < 100:  # if pour valider le taux d'intérêt.
                with open(strutil, 'r') as calcinteret:
                    lstinteret = calcinteret.readlines()
                    fltintérêt = float(lstinteret[intcarte]) * (1 + (fltvalint / 2)) ** (
                                intvaltemps * 2)  # Calcule de l'intérêt.
                    return fltintérêt, intvaltemps  # Retourne l'intérêt et le temps au programme principale.
                break
            else:
                print("Une/deux des données sont invalides Essayez encore.")
        except:
            print("Donnée invalide. Essayez encore.")


def supprime(strnomutil):
    """ Permet de supprimer un compte au complet."""

    os.remove(strnomutil)


def ouvreacc(listcomptes):
    """ Permet de créer une nouvelle carte ou mini-compte dans le compte principale pour sauvegarder l'argent. Le nouveau mini-compte peut être créer en transférant de l'argent d'une compte existante au nouveau, ou de mettre directement de l'argent dans le nouveau compte.
    """

    print(""" Voulez-vous:  
        1. Enlever de l'argent d'une de vos comptes et de le mettre dans le nouveau compte. 
        2. Ajouter de l'argent directement dans le nouveau compte.

        """)
    strmenuchoix = input("Choix: ")
    if strmenuchoix == "1":  # Permet de créer un nouveau compte en retirant de l'argent d'un compte pour le mettre dans le nouveau.
        try:
            intaccchoix = int(input("Entrer le nombre du compte que vous voulez accéder: "))
            fltcombien = float(input("Combien d'argent que vous voulez retirer?: "))
            if float(listcomptes[
                         intaccchoix]) - fltcombien >= 0 and fltcombien > 0 and intaccchoix > 0:  # Permet de valider que l'utilisateur a assez d'argent pour créer le nouveau compte.
                fltnouvfonc = float(listcomptes[intaccchoix]) - fltcombien  # Nouveau valeur du compte existante.
                listcomptes[intaccchoix] = str(fltnouvfonc) + "\n"  # Changement la valeur du compte déductée.
                listcomptes.append(str(fltcombien) + "\n")  # Ajoute le nouveau compte à la fin du liste des comptes.
                print(f"Compte créé! Voici tes comptes:")
                return listcomptes  # Les return qui sont présents après les excepts et quelques elif et else sont présents pour éviter qu'une variable qui sera manipulé plus tard soit Nonetype. (Éviter un crash du programme.)

            elif intaccchoix < 0:  # Si le nombre du compte est négative.
                print("Le nombre du compte ne peut pas être négative.")
                return listcomptes
            else:  # Pas assez d'argent ou un nombre négative.
                print(
                    "Vous n'avez pas assez d'argent pour retirer pour votre nouveau compte ou vous avez entré un nombre négative. Réessayez encore. ")
                return listcomptes
        except:
            print("Donnée invalide. Essayez encore.")
            return listcomptes
    elif strmenuchoix == "2":  # elif utilisé si la personne veut ajouter de l'argent directement dans un compte.
        try:
            fltmontantdarg = float(input("Entrer le montant d'argent que vous voulez ajouter à votre nouveau compte: "))
            if fltmontantdarg > 0:  # Valide si l'argent entré est positive et non un nombre invalide.
                listcomptes.append(str(fltmontantdarg) + "\n")
                return listcomptes
            else:
                print("Nombre invalide. Essayez encore.")
                return listcomptes
        except:
            print("Entrée invalide. Essayez encore.")
            return listcomptes
    else:
        print("Entrée invalide. Essayez encore.")
        return listcomptes


def mdpchange(listcomptes):
    """ Permet de changer le mot de passe d'un compte. """

    while True:
        strnvmotdepasse = input("Quel serait votre nouveau mot de passe?: ")
        if strnvmotdepasse != "":  # Valider pour que le mot de passe ne soit pas vide.
            listcomptes[
                0] = strnvmotdepasse + "\n"  # Prend le premier ligne du texte fichier et la remplace. (ligne du mot de passe.)
            print(f"Votre mot de passe à été changé à {strnvmotdepasse}")
            return listcomptes
        else:
            print("Entrez un mot de passe valide.")


def changementindex(intorgchoix, listcomptes):
    """Fonction pour changer le nombre du compte sélectionné (par exemple: changement de compte 1 à compte 2.)
    """

    try:  # try et except est utilisé pour valider que l'entrée est un int, et non pas un str ou un float.
        intindremp = int(
            input("Quel compte/carte voulez-vous sélectionner (entrer le nombre de la carte que vous voulez)?: "))
        if intindremp > 0 and intindremp <= len(
                listcomptes) - 1:  # if utilisé pour valider si le nombre entrée est positive et que cette index est dans la liste.
            return intindremp
        else:
            print("Nombre invalide. Essayez encore.")
            return intorgchoix
    except:
        print("Donnée invalide. Essaye encore.")
        return intorgchoix



