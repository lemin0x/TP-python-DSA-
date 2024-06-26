#But du TP : Apprendre `a lire et  ́ecrire des fichiers texte via Python.

#files 

# def Affichier(fichier):
#     fichier = open(fichier , "r")
#     print(fichier.read())
#     fichier.close()

f= open("test.txt",mode="w" ,encoding="utf-8")

print(f.write())

f.close()