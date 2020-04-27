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
    def __init__(self):
		self.nom = "Dupont"

	def solde(self):
		return "1000"


compte1 = compteBancaire()
compte2 = compteBancaire()
compte3 = compteBancaire()
print(compte1.solde(), compte2.solde(), compte3.solde())

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