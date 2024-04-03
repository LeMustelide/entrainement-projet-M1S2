# -*- coding: utf-8 -*-

# DEUXIEME PARTIE POUR CONSOLIDER



#============================== A propos de mots ==============================



def motAvecPusDeA(mot):

    cpta = 0
    cptb = 0

    for c in mot:
        if c == 'a':
            cpta += 1
        if c == 'b':
            cptb += 1

    if cpta > cptb:
        return True

    return False


#print(motAvecPusDeA("abababa"))


# renvoie tous les mots de longueur 30 et période 3 sur un alphabet
def motPeriodique(longueur, periode, alphabet):

    ensMotPeriodique=[]

    for l1 in alphabet:
        for l2 in alphabet:
            for l3 in alphabet:
                periode = ""
                periode.append(l1)
                preiode.append(l2)
                periode.append(l3)
                ensMotPeriodique.append(periode)

    for i in range(9):
        return False

    return True




def pref(mot):
    pref=""
    n=len(mot)
    for i in range((n//2)+1):
        if mot[i] == mot[n-i-1]:
            pref = pref + mot[i]
        else:
            return pref
    return pref

#print(pref("caaac"))

# envois si v > u et que u est prefixe de v et inverse de u suffixe de v
def troisiemeFonc(v,u):
    n=len(v)

    for i in range(len(u)):

        if v[i] != u[i]:
            return False

        if v[(n-i-1)] != u[i]:
            return False

    return True


#print(troisiemeFonc("abccba", "ab"))


def quatriemeFonc(u,v):

    mot=""
    for i in range(len(v)):
        if i%2 == 0:
            mot += v[i]
        if i%2 != 0:
            mot += u[i]

    return mot

#print(quatriemeFonc("emma", "marc"))


def trier(mot):
    ens=set()
    for c in mot:
        ens.add(c)
    return sorted(ens)

#print(trier("baceeeeeeeeeeeed"))

def combienMotif(mot, motif):

    cpt=0
    while len(mot) >= 3:
        if mot[:3] == motif:
            cpt += 1
        mot = mot[1:]
    return cpt

#print(combienMotif("bbaababaaaaaa", "aba"))


#========================= En dimension 2 ==============================

M=[['a','b','a'],
   ['b','b','a'],
   ['b','a','a']]

def matriceCarre(M):
    if len(M)== len(M[0]):
        return True
    return False

#print(matriceCarre(M))

def nbColonneKA(M,k):
    cpt = 0
    for i in range(len(M)):
        cpta = 0
        for j in range(len(M[0])):
            if M[j][i] == 'a':
                cpta += 1
        if cpta >= k:
            cpt += 1
            cpta = 0
    return cpt

#print(nbColonneKA(M, 2))

Mots=[['aa','a','a'],
   ['b','aab','ab'],
   ['b','ba','aabc']]
def prefMotAvant(M):
    for i in range(1,len(M)):
        for j in range(1,len(M[0])):
            pref = M[i-1][j-1]
            m = M[i][j]
            n = len(pref)
            print(n)
            print(pref)
            print(m)
            if pref != m[:n]:
                return False
    return True

#print(prefMotAvant(Mots))

S=[[1,1,1],
   [3,3,3],
   [2,2,2]]

def plusGrandeSommeLigne(M):
    ligne = 0
    cpt = 0
    for i in range(1,len(M)+1):
        c=0
        for j in range(len(M[0])):
            c+=M[i-1][j-1]
        if c>=cpt:
            cpt=c
            ligne = i
    return ligne

print(plusGrandeSommeLigne(S))

def pascal(n):
    M=[[] for i in range(n)]




#================================ Et des suites ===============================



















