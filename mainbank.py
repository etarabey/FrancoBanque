# TS3 Module et fonctions
""" Nom: Elias Tarabey

Le programme est un système bancaire. Il permet à l'utilisateur de créer des comptes, de créer des cartes (mini-comptes) dans le compte principale, ajouter ou de retirer de l'argent des comptes, de calculer l'intérêt, de changer le mot de passe, ou de même quitter le compte. Les comptes sont sauvegardés dans un fichier de texte, avec le mot de passe, ainsi que les comptes créés. Ceci permet que l'utilisateur sera capable de rentrer dans son compte après qu'il ferme le programme. Le programme peut être utile pour sauvegarder ou retirer de l'argent et pour calculer le profit de l'intérêt de l'utilisateur.
"""

import banque  # Module de banque pour performer les opérations du menu ci-dessous.

while True:  # Boucle principale du programme.
    intcompteind = 1  # Carte (compte de l'utilisateur) sélectionné.
    lstcomptes = []  # Liste de toutes les comptes.
    login = False  # Variable booléen qui tourne True une fois la personne entre dans son compte.
    exit = False  # Utilisé pour sortir du programme au complet.
    print(""" Bienvenue à FrancoBanque! 

        1. Créez un nouveau compte. 
        2. Login
        3. Quitter"""
          )  # Mini-menu pour choisir de créer ou d'entrer dans un compte.
    strchoixlog = input("Choix: ")
    if strchoixlog == "1":  # if pour créer un nouveau compte.
        strutil, login = banque.nouveau(
            login)  # Appel à la fonction de créer une nouvelle compte.
        with open(
                strutil, 'r'
        ) as strchoix:  # Utilisé pour créer une liste de toutes les comptes de l'utilisateur.
            for nombre in strchoix:
                if nombre.split(
                        "\n"
                )[
                    0] != "":  # Le split est utilisé pour enlever "\n" pour que les lignes vides ne soient pas dans la liste des comptes.
                    lstcomptes.append(nombre)
    elif strchoixlog == "2":  # if utilisé pour faire appel à la fonction pour entrer dans un compte.
        strutil, login = banque.login(login)
        if strutil != "":  # Utilisé pour éviter un erreur après que l'utilisateur a utilisé l'option de quitter.
            with open(strutil, 'r') as strchoix:
                for nombre in strchoix:
                    if nombre.split("\n")[0] != "":
                        lstcomptes.append(nombre)
    elif strchoixlog == "3":
        print("Merci pour avoir utilisé le système de FrancoBanque!")
        break
    else:
        print("Choix invalide. Essayez encore.")
    while login:  # Boucle de l'utilisateur.

        with open(
                strutil, 'w'
        ) as nouveauacc:  # Utilisé pour écrire dans le fichier de texte de l'utilisateur, et pour le mettre à mise à jour.
            for t in range(len(lstcomptes)):
                if t == len(lstcomptes) - 1:
                    nouveauacc.write(f"{lstcomptes[t]}\n")
                else:
                    nouveauacc.write(lstcomptes[t])
        for intcompteindex in range(
                1, len(lstcomptes)
        ):  # Boucle for utilisé pour donner les comptes de l'utilisateur et leur balance.
            strvarcompte = lstcomptes[intcompteindex].split("\n")[
                0]  # Le split est utilisé pour éviter d'imprimer "\n".
            print(f"Compte {intcompteindex}: {strvarcompte} dollars")
        print(f""" 
          Bienvenue à ton compte
          1. Ajouter/Retirer de l'argent. 
          2. Calculer l'intérêt 
          3. Supprimer ce compte 
          4. Créer une carte (pour épargner ton argent) 
          5. Changer ton mot de passe.
          6. Changement de carte sélectionné.
          Q. Quitter ton compte
          F. Fermer le programme 

      Carte sélectionné: {intcompteind}


          """)
        strchoix = input("Choix: ")
        if strchoix == "1":  # if utilisé pour chercher la fonction pour ajouter ou enlever de l'argent d'un compte.
            try:
                fltmonnaieajoute = float(
                    input("Entrez combien d'argent que vous voulez ici: "))
                if fltmonnaieajoute > 0:  # if vérifie si le nombre donnée est positive.
                    lstcomptes = banque.ajoute(fltmonnaieajoute, intcompteind,
                                               lstcomptes)
                else:
                    print("Donnez un nombre réel pour l'argent.")
            except:
                print("Choix invalide. Essayez encore.")
        elif strchoix == "2":  # elif utilisé pour calculer l'intérêt d'un compte.
            Interet, temps = banque.Interet(strutil, intcompteind)
            print(
                f"L'intérêt calculée pendant {temps} années est de {round(Interet, 2)} dollars."
            )
        elif strchoix == "3":  # Supprime le compte.
            banque.supprime(strutil)
            print(f"Votre compte {strutil} a été supprimé")
            login = False  # Permet de revenir au mini-menu.
        elif strchoix == "4":  # Ouvrir un nouveau compte bancaire.
            lstcomptes = banque.ouvreacc(lstcomptes)
        elif strchoix == "5":  # Permet de changer le mot de passe du compte de l'utilisateur.
            lstcomptes = banque.mdpchange(lstcomptes)
        elif strchoix == "6":  # Permet de changer le compte sélectionné.
            intcompteind = banque.changementindex(intcompteind, lstcomptes)
        elif strchoix.lower(
        ) == "q":  # Permet de quitter le compte de l'utilisateur.
            login = False
            print(
                "Merci pour avoir utilisé le système de FrancoBanque et à la prochaine!"
            )
        elif strchoix.lower(
        ) == "f":  # Permet de quitter le programme principale.
            print(
                "Merci pour avoir utilisé le système de FrancoBanque et à la prochaine!"
            )
            exit = True  # Valeur booléen pour sortir du programme au complet devient vrai.
            break
        else:
            print("Choix invalide. Essayez encore.")
    if exit:
        break
