# a = int(input("entrer un nombre :"))
# b = int(input("entrer un nombre :"))
# c = int(input("entrer un nombre :"))

# if a < b and a < c :
#     print("le plus petit nombre est a: ", a)
# elif a < b and a > c:
#     print("le plus petit nombre est c: ", c)
# else :
#     print("le plus petit nombre est b: ", b)


# hd = int(input("Entrez l'heure de depart: "))
# md = int(input("Entrez la minuite de depart: "))

# ha= int(input("entrez l'heure de l'arrive: "))
# ma= int(input("entrez la minuite de l'arrive: "))
# duree_h = ha - hd
# duree_m = md - ma 
# if duree_m < 0:
#     duree_m = 60 + duree_m
#     duree_h -= 1
# if duree_h < 0:
#     duree_h = 24 + duree_h
# print("la duree de l'avion est :",duree_h,"heure et", duree_m, "minuite" )


# a = int(input("entrer un nombre :"))
# b = int(input("entrer un nombre :"))
# c = 1

# while b  != 0:
#     if b % 2 == 1:
#         c = c * a
#     a = a * a
#     b = b // 2
# print(c) 


# n = int(input("Entrez un nonbre reelle"))

# if n == 0 :
#     print("Tous les nombres relles est diviseurs par 0")
# for diviseur in range (1, n+1):
#     if n % diviseur == 0 :
#         print(diviseur)
# from math import sqrt

# import math
# n = int(input("entrez un nombre reelle: "))
# rac = math.sqrt(n)
# diviseur = 2
# while n % diviseur != 0 and diviseur < rac:
#     diviseur += 1
# if (diviseur > rac) :
#     print("le nombre est premier")
# else:
#     print("le nombre n'EST PAS PREMIER")

# import numpy as np

# #enregistrement 

# class Fiche :
#    def __init__(self):
#         self.Num = 0
#         self.Nom = ""
#         self.preNom = ""
#         # self.dateNaissance = ""


# Tab = np.array([Fiche() for _ in range(3)], dtype=object)

# eleve = Fiche

# def saisir(eleve):
#     eleve.Num = int(input("entrez le nombre de l'eleve: "))
#     eleve.Nom = str(input("Entrez le nom de l'eleve: "))
#     eleve.preNom = str(input("Entrez son prenom:  "))
# def affichage(eleve):
#     print("Num", eleve.Num)
#     print("Nom", eleve.Nom)
#     print("Prenom Nom", eleve.preNom)

# # saisir(Tab[0])
# # affichage(Tab[0])

# for i in range(0, 5):
#     saisir(Tab[i])


# def factorielle(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorielle(n-1)

# y=factorielle(5)
# print(y)

# def fabonacci(n):
#     if n <=1 :
#         return n 
#     else:
#         return fabonacci(n-1) + fabonacci(n-2)
    
# x = fabonacci(6)
# print(x)

# def sumD(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + sumD(n//10)
# z = sumD(12345)
# print(z) 


# def f(n):
#     if n == 0:
#         return 0 
#     else :
#         return n % 10 + f(n//10)
# print(f(123))

#output 1: 3 + f12 + 2 + f1 + 1 + f


# def f(n):
#     if n == 0 :
#         return 1
#     else :
#         return n * f(n-1)

# def f(str):
#     if str == "":
#         return 0
#     else :
#         return 1 + f(str[1:])
# print(f("bonjour"))

#TD1

def f(chaine):
    if chaine == "":
        return ""
    else :
        return f(chaine[1:] )+ chaine[0]

print(f("bonjour"))

def produit(a,b):
    # if b == 0:
    #     return 0
    # else :
    #     return a + produit(a,b-1) 
    resultat = 0
    for _ in range (b):
        resultat += a
    return resultat
    
print(produit(5,3))

def Binaire(n):
    if n > 1:
        Binaire(n//2)
    print(n%2, end="")
Binaire(13)
print()


def somme(l):
    if not l:
        return 0
    else :
        return l[0] + somme(l[1:])

lst = [1, 2, 3, 4, 5] 
print(somme(lst))


# def conct(lst1, lst2):
#     if not lst1:
#         return lst2[:]
#     elif not lst2:
#         return lst1[:]
#     else:
#         e = lst1.pop(0)
#         lst2.append(e)
#         conct(lst1, lst2)
#         # return lst2


# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# conct(lst1 , lst2) 
# print(lst2)


def conct(lst1, lst2):
    if not lst1:
        return lst2[:]
    elif not lst2:
        return lst1[:]
    else :
        e = lst1.pop()
        lst2.append(e)
        conct(lst1, lst2)
        return lst2

lst1 = [1, 2, 3]
lst2 = []
y = conct(lst1 , lst2) 
print(y)


def triangle1(n):
    if n == 0 :
        return 0
    else :
        print("*"*n)
        return n + triangle1(n-1)

        
triangle1(6)


def summeD(n):
    if n < 10:
        return n
    else :
        return n % 10 + summeD(n//10)
nombre = -123
print(summeD(nombre))