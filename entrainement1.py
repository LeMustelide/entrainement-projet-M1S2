# -*- coding: utf-8 -*-


#   PREMIERE PARTIE

import random 

#============================= A propos des nombres ===========================
    
# fonct qui renvoie en string n en base k

def nEnBaseK(nombre, base):
    resultat = ""
    nombre = int(nombre)
    while nombre > 0:
        reste = nombre % base
        if reste < 10:
            resultat = str(reste) + resultat
        else:
            resultat = chr(reste + 55) + resultat
        nombre = nombre // base
    return resultat

#print(question2_1_1(2, 10))
#print(question2_1_1(2, 2))
#print(question2_1_1(11, 16))
    
# fonct qui renvoie si une string s contient que des chiffres entre 0 et k
def sContient(s,k):
    for c in s:
        if int(c) > k or int(c) < 0:
            return False
    return True

#print(sContient("3612", 4))

# fonct qui renvoie si la string est un entier en base k
def estEnBaseK(s,k):
    if nEnBaseK(int(s), k):
        return True
    return False

# fonct qui retourne vrai si n est premier
def premier(n):
    for m in range(2, n-1):
        if n%m == 0 :
            return "n'est pas premier"
    return "est premier"

# fonct renvoie si n est une puissance de m
def puissance(n,m):
    while m%n == 0:
        m /= n

    return m == 1


#============================= A propos des listes ============================

# fonction qui calcule la somme de tous les nb de la liste
def sommenb(L):
    res=0
    for nb in L:
        res+=nb
    return res

# fonction qui retourne la liste L avec chaque nb multipliés par k
def multiParK(L,k):
    for i in range(len(L)):
        L[i]=L[i]*k
    return L


# fonction qui retourne une liste des longeur des string de la liste L
def longPosI(L):
    res=[0 for i in range(len(L))]
    for i in range(len(L)):
        res[i]=len(L[i])
    return res
def longPosI2(L):
    res=[]
    for i in range(len(L)):
        res=len(L[i])
    return res


# fonction qui renvoie la liste L avec une seule occurence de chaque nb
def uneOcc(L):
    ens=set()
    M=[]
    for nb in L:
        if nb not in ens:
            ens.add(nb)
            M.append(nb)
    return M 

def question2_2_4(tab):
    return list(set(tab))

# fonct qui retourne l'élément le plus présent dans la liste 


# fonction qui retorune true si la liste contient un (ou des) doublon(s)
def unDoublon(L):
    ens=set()
    for nb in L:
        if nb not in ens:
            ens.add(nb)
        else: 
            return True
    return False

# fonct qui genere une liste est qui renvoie si celle-ci contient au moins un doublon
def genereListe(n,k):
    L=[random.randint(0,n) for i in range(n)]

    if unDoublon(L)==True:
        return 1
    else:
        return 0


#for i in range(1000):
    #genereListe(23, 365)


#========================== A propos des dictionnaires ========================

d = { 1 : 2, 2 : 8, 3 : 5}

def couples(D):
    L=[]
    for i in D.items():
            L.append(i)
    return L
#print(couples(d))

J= {"Enzo":[0+0+0], "Marc":[10+4], "Valentin": [10+9], "Corentin":[10+7]}

def scoreInfAK(D,k):
    joueur = []
    for j,s in D.items():
        if s<k:
            joueur.append(j)          
    return joueur
#print(scoreInfAK(J,5))

def scoreTotal(D):
    d = {}
    for j,listeS in D.items():
        total=0
        for i in listeS:
            total+=i
        d[j]=total
#scoreTotal(J)
#print(J)

L=["Enzo","Marc","Corentin","Valentin","Mathilde"]
def notesRnd(L):
    D={}
    for e in L:
        note =random.randint(0, 20)
        D[e]=note
    return D
#print(notesRnd(L))


#============================= A propos des graphes ===========================


sommets=[1,2,3,4,5,6]
arretes=[(1,3),(3,1),(2,3),(3,2),(4,5),(5,4)]

"""fonct qui retourne true s'il y a au moins un sommet isolé dans le graphe"""
def sommetIsole(S,A):
    ens=set()
    for i,j in A:
        if i not in ens:
            ens.add(i)
        if j not in ens:
            ens.add(j)
            
    for som in S:
        if som not in ens:
            return True
    
    return False

#print(sommetIsole(sommets,arretes))

"""fonct qui retorune le degré max """
def degMax(S,s):
    
    res=0
    i=0
    for p,q in S:
        if p==s or q==s:
            res+=1
        i+=1
    
    return res

#S=[(1,2),(1,4),(2,3),(4,1)]
#print(degMax(S, 1))

"""fonct qui renvoie un chemin entre les sommets x et y"""

# renoie l'ensemble des voisins du sommet s
def listeVoisins(G,s):
    
    v = set()
    voisins=[]
    for s1,s2 in G:
        if s1 == s:
            if s2 not in v:
                v.add(s2)
                voisins.append(s2)
        if s2 == s:
            if s1 not in v:
                v.add(s1)
                voisins.append(s1)
    return voisins
#print(listeVoisins(arretes, 3))

def recChemin(G,x,y,voisinsVus):
    if x not in voisinsVus:
        voisinsVus.add(x)
        for v in listeVoisins(G, x):
            if v == y:
                return True
            recChemin(G, v, y, voisinsVus)
    

def chemin(G,x,y):
    voisinsVus={}
    voisins = listeVoisins(x)
    
    
    return True


"""fonct qui renvoie si le graphe est connexe"""
def connexe(S,G):
    
    
    return True


"""fonct qui retourne la liste des couples(sommet,distance) pour les sommets"""
#dans la composante connexe ( Dijkstra )





#========================== A propose des automates ===========================


# Une structure de donnée qui peut correspondre à une automate serait le 
#dictionnaire avec pour clé les états et pour valeur un couple (étiquette, état)

E=[(1,0),(2,0),(3,0),(4,0),(5,1)]
A=[(1,2,"a"),(1,3,"b"),(2,1,"b"),(2,3,"b"),(3,4,"b"),(4,5,"b")]


# fonct qui retourne s'il existe une transition entre un état et un autre avec 
#une étiquette donnée
def transition(A,etat,etiq):
    for e1,e2,e in A:
        if e1 == etat and e==etiq:
            return e2     
    return etat
#print(transition(A, 2, "b"))

def etatSortant(E,e):
    for etat,b in E:
        if etat == e:
            if b == 0:
                return False
            return True

# fonct qui retourne vrai si le mot est reconnu par l'automate
# par defaut je pense que mon état entrant est l'état numéro 1
def appartient(A,E,mot):
    c = 1
    for e in mot:
        if transition(A,c,e)!=e:
            c=transition(A,c,e)
    if etatSortant(E, c):
        return True
    return False


#print(appartient(A, E, "abbbb"))

# fonct qui retourne si le langage de A est vide
def langageEstVide(E):
    for etat,b in E:
        if b == True:
            return True
    return False

# fonct de minimisation d'un automate






