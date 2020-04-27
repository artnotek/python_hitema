def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb
    de 1*nb à max*nb

    (max >= 0)"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1
table(3, 10)

class compteBancaire:
    def __init__(self, nom, solde):
        self.nom = nom
        self.solde = solde


    # def solde(self):
    #     return "1000"

    def ajoutsolde(self, somme):
        self.solde = self.solde + somme

    def retrait(self, somme):
        self.solde = self.solde - somme

    def affichersolde(self):
        return self.solde


# class UneClasse:
#     def methode(self):
#         print('un truc')
#
#
# ex = UneClasse()
# ex.methode()

compte1 = compteBancaire('jean', 2000)
compte2 = compteBancaire('dupont2', 1000)
compte3 = compteBancaire('dupont3', 1000)

compte1.ajoutsolde(200)
compte1.retrait(724)
print(compte1.nom, compte1.solde, 'soldat actuel : '+ compte1.affichersolde())

# jupiter est un IDE serveur, et les fichiers sotn des calepins

mot = "lac"
print(mot)
# le point dans le 1 représente un slice
# [1:] => coupe le contenu avant le caratère 1 donc mot = ac
# b + ac = bac
mot = "b" + mot[1:]
print(mot)

# self = this

# init = construct

