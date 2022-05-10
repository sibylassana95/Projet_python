# Demande à l'utilisateur d'entrer un nombre
n = int(input("Entrez un nombre: "))
if (n % 2) == 0:
    print("{0} est Paire".format(n))
else:
    print("{0} est Impaire".format(n))
