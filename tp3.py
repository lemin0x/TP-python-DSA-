#But du TP : Apprendre `a lire et  ́ecrire des fichiers texte via Python.

#files 

# def Affichier(fichier):
#     fichier = open(fichier , "r")
#     print(fichier.read())
#  
#   fichier.close()



##exo1
def afficher(fichier):
    fichier = open(fichier, "r")
    print(fichier.read())
    fichier.close()

def affichier(fichier):
    fichier = open(fichier, "r")
    chaine = fichier.readline()
    print(chaine)

    while chaine != "":
        chaine = fichier.readline()
        print(chaine)
    fichier.close()



def affichier(fichier):
   fichier = open(fichier, "r")
   chaine = fichier.readline()
   print(chaine)
   fichier.close
   return

##exo2


def nblingne(f):
    fichier = open(f, "r")
    i = 0
    chaine = fichier.readline()
    while chaine != "":
        i += 1
        chaine = fichier.readline()
    fichier.close()
    
    return i 

##ex03
from os import *
from os import chdir 
chdir("/Users/muhammed/")
print("bienvenue ...")
nomFichier = input("Veuillez entrer le nom du fichier ")
print("1.Ecrire")
print("2.lire")
choix = int(input(""))
if choix == 1:
    obFichier = open(nomFichier, "a")
    while 1:
        txt = input ("entrez votre texte: ")
        obFichier.write(txt)
        obFichier.write("\n")
        if txt == '':
            break
    obFichier.close()
else :
    try :
        oFi =open(nomFichier, "a")
        while 1 :
            lecture = oFi.readline()
            print(lecture)
            if lecture =='':
                break
        oFi.close()
    except :
        print("le nom du fichier que vous avez specifie n exist pas")

##exo4

def Crypatage(nomfichier):
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    oFi = open(nomfichier, "r")
    while True :
        lecture = oFi.readline()
        chaine = str (lecture)
        for charactere in chaine :
            if charactere == "\n":
                break
            indice = alph.find(charactere)
            pos = indice + 1
            if pos == 26:
                pos = 0
            res += alph[pos]
        f.oepn("cryptage.txt", "a")
        f.write(res)
        f.write("\n")
        res = ''
        if lecture == '':
            break
    f.close()
    oFi.close()

### ex05
with open("myFile.txt", "w") as file:
    file.write("Ligne numero 1\n") 
    file.write("Ligne numero 2\n") 
    file.write("Ligne numero 3\n") 
    file.write("Ligne numero 4\n") 
    file.write("Ligne numero 5\n")

# Lecture du fichier et modification de la troisieme ligne
with open("myFile.txt", "r") as file:
    lines = file.readlines()
# Modification de la troisieme ligne
lines[2] = "Desole ! Le contenu de cette ligne a ete change !\n"

# Reecriture du fichier avec la troisieme ligne modifiee
with open("myFile.txt", "w") as file:
    file.writelines(lines)
