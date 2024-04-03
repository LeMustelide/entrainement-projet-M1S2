import random
import string


## 2.1
def question2_1_1(nombre, base):
    """Convertit un nombre de base 10 en base donnée"""
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


# print(question2_1_1(2, 10))

def question2_1_2(s, k):
    """Test si la chaine de caractère s ne contient que des chiffres de 0 à k-1"""
    if not s.isnumeric():
        return False
    for i in range(len(s)):
        if int(s[i]) >= k:
            return False
    return True


# print(question2_1_2("125s", 6))

def question2_1_3(s, k):
    if question2_1_2(s, k):
        return question2_1_1(s, k)


# print(question2_1_3("40", 2))

def question2_1_4(n):
    for m in range(2, n - 1):
        if n % m == 0:
            return "n'est pas premier"
    return "est premier"


# print(question2_1_4(79))

def question2_1_5(m, n):
    while m % n == 0:
        m /= n

    return m == 1


# print(question2_1_5(8,2))

## 2.2

def question2_2_1(tab):
    result = 0
    for e in tab:
        result += e
    return result


# print(question2_2_1([1,2,3,4]))

def question2_2_2(l, k):
    result = 0
    for i in l:
        result += i * k
    return result


# print(question2_2_2([2,2,4], 10))

def question2_2_3(tab):
    result = []
    for str in tab:
        result.append(len(str))
    return result


# print(question2_2_3(["a","ab","abs","test","fin"]))

def question2_2_4(tab):
    return list(set(tab))


# print(question2_2_4([123,23,123]))

def question2_2_5(tab):
    compteur = {}  # création d'un dictionnaire
    for e in tab:
        compteur[e] = compteur.get(e,
                                   0) + 1  # pour chaque élément de e je rajoute un a la valeur du compteur pour la clef e, soit je fait la somme du nombre d'individu par type
    return max(compteur.items(), key=lambda x: x[1])  # je retourne l'item ayant la valeur la plus élevé


# print(question2_2_5([1,1,2,3,5,]))

def question2_2_6(tab):
    return len(question2_2_4(tab)) != len(tab)


# print(question2_2_6([12,12,24]))

def question2_2_7(k, n):
    tab = [random.randint(0, n) for _ in range(k)]
    return int(question2_2_6(tab))


# print("question 2_2_7 : ")
# print(question2_2_7(2,2))

def question2_2_8(k, n, nb):
    avg = 0
    for _ in range(nb):
        avg += question2_2_7(k, n) / nb
    return avg


# print(question2_2_8(200, 365, 1000))

# si la valeur de K est haute alors le resultat sera plus proche de 1 est inversement


# 2.3

def question2_3_1(d):
    return list(d.items())


# print(question2_3_1({1:"r", 2:"t"}))

def question2_3_2(d, k):
    return {key: value for key, value in d.items() if value >= k}


# print(question2_3_2({"mourc": 100, "enzo": 300}, 200))

def question2_3_3(d):
    d = {key: sum(value) for key, value in d.items()}


# print(question2_3_3({"mourc": [4, 6], "enzo": [10, 20]})) # none car la fonction ne retourne rien

def question2_3_3(tab):
    # return {key: [random.randint(0,20) for _ in range(10)] for key in tab} # version pour plusieur notes
    return {key: random.randint(0, 20) for key in tab}


# print(question2_3_3(["mourc", "enzo"]))


# 2.4

class graph:
    sommets = []  # sommets = [A,B,C]
    arêtes = [()]  # arêtes = [(A,B),(B,C)]

    def set_sommets(_self, sommets):
        _self.sommets = sommets

    def set_arêtes(_self, arêtes):
        _self.arêtes = arêtes


# retourner True si au moins un sommet n’est relié à aucun autre, False sinon
def question2_4_1(graph):
    for sommet in graph.sommets:
        for arête in graph.arêtes:
            if sommet in arête:
                break
        else:
            return True
    return False


G = graph()

G.set_sommets(["A", "B", "C", "D"])
G.set_arêtes([("A", "B"), ("B", "C"), ("C", "D")])


# print(question2_4_1(G))


# retourne le degre maximal du graphe
def question2_4_2(graph):
    degre = 0
    for sommet in graph.sommets:
        degre = max(degre, sum([1 for arête in graph.arêtes if sommet in arête]))
    return degre


# print(question2_4_2(G))


# retourne la liste des sommets connectés à x
def question2_4_3(graph, x):
    adj_list = {sommet: [] for sommet in graph.sommets}

    for sommet1, sommet2 in graph.arêtes:
        adj_list[sommet1].append(sommet2)
        adj_list[sommet2].append(sommet1)

    def dfs(sommet, visited):
        visited.add(sommet)
        for voisin in adj_list[sommet]:
            if voisin not in visited:
                dfs(voisin, visited)

    visited = set()
    dfs(x, visited)

    return visited


G.set_sommets(["A", "B", "C", "D", "E"])
G.set_arêtes([("A", "B"), ("B", "C"), ("C", "A"), ("E", "D")])


# print(question2_4_3(G, "B"))


# verifie la connectivité du graphe
def question2_4_4(graph):
    # Cette ligne initialise une liste d'adjacence vide pour chaque sommet du graphe.
    # Une liste d'adjacence est une façon de représenter un graphe où chaque clé (sommet) a une liste de sommets connectés (voisins).
    adj_list = {sommet: [] for sommet in G.sommets}
    # print(adj_list) # = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': []}

    # Cette boucle parcourt chaque paire de sommets dans la liste des arêtes.
    # Pour chaque paire (sommet1, sommet2), elle ajoute sommet2 à la liste des voisins de sommet1, et vice versa.
    # Cela construit effectivement la structure du graphe dans la liste d'adjacence, représentant les connexions entre sommets.
    for sommet1, sommet2 in G.arêtes:
        adj_list[sommet1].append(sommet2)
        adj_list[sommet2].append(sommet1)

    # Cette fonction interne 'dfs' réalise un parcours en profondeur du graphe.
    # Elle prend un sommet et un ensemble de sommets visités comme paramètres.
    def dfs(sommet, visited):
        # Marque le sommet actuel comme visité en l'ajoutant à l'ensemble visited.
        visited.add(sommet)
        # Pour chaque voisin du sommet actuel dans la liste d'adjacence,
        # si ce voisin n'a pas encore été visité, la fonction s'appelle récursivement avec ce voisin.
        for voisin in adj_list[sommet]:
            if voisin not in visited:
                dfs(voisin, visited)

    # Initialise un ensemble vide pour garder une trace des sommets visités.
    visited = set()
    # Commence le parcours en profondeur (DFS) à partir du premier sommet de la liste des sommets du graphe.
    # Cela permet de visiter tous les sommets connectés à ce sommet de départ.
    dfs(G.sommets[0], visited)

    # Après avoir effectué le DFS, si le nombre de sommets visités est égal au nombre total de sommets,
    # cela signifie que le graphe est connexe (il est possible d'atteindre n'importe quel sommet à partir de n'importe quel autre sommet).
    # La fonction retourne True si le graphe est connexe, et False sinon.
    return len(visited) == len(G.sommets)


# print(question2_4_4(G))

def question2_4_5(graphe, depart):
    # Construction de la liste d'adjacence avec des poids
    liste_adjacence = {sommet: [] for sommet in graphe.sommets}
    for (u, v, poids) in graphe.arêtes:
        liste_adjacence[u].append((v, poids))
        liste_adjacence[v].append((u, poids))  # Pour un graphe non orienté

    # Initialisation des distances
    distances = {sommet: float('infinity') for sommet in graphe.sommets}
    distances[depart] = 0

    # Ensemble des sommets non visités
    non_visites = set(graphe.sommets)

    while non_visites:
        # Sélection du sommet non visité le plus proche
        sommet_courant = min(non_visites, key=lambda sommet: distances[sommet])

        non_visites.remove(sommet_courant)

        # Mise à jour des distances pour chaque voisin
        for voisin, poids in liste_adjacence[sommet_courant]:
            nouvelle_distance = distances[sommet_courant] + poids
            if nouvelle_distance < distances[voisin]:
                distances[voisin] = nouvelle_distance

    # Filtrage et retour sous forme de liste de couples (sommet, distance)
    return [(sommet, distance) for sommet, distance in distances.items() if distance != float('infinity')]


G.set_sommets(["A", "B", "C", "D", "E", "F", "G"])
G.set_arêtes([("A", "B", 3), ("B", "E", 4), ("C", "D", 1), ("B", "D", 5), ("F", "G", 2), ("A", "F", 10)])


# print(question2_4_5(G, "B"))


# 2.5

class Etat:
    name = ""
    transitions = []  # [(2,"a")] soit "2" l'état d'arrivé et "a" le symbole de la transition

    def set_transitions(_self, transitions):
        _self.transitions = transitions

    def set_name(_self, name):
        _self.name = name

    def is_accessible_via(self, letter):  # retourne les etat accessible en passant par un lettre
        etats = []
        for transition in self.transitions:
            if transition[1] == letter:
                etats.append(transition[0])
        return etats

    def is_accessible(self, state):  # Verifie si des transitions existe bien entre l'etat courant et le paramètre

        visited = set()

        def dfs(state, visited):
            visited.add(state)
            for voisin in state.transitions:
                if voisin[0] not in visited:
                    dfs(voisin[0], visited)

        dfs(self, visited)

        return state in visited

    def get_transition_by_letter(self,letter):
        for transition in self.transitions:
            if transition[1] == letter:
                return transition

    def get_alphabet(self):
        alpha = []
        for transition in self.transitions:
            if transition[1] not in alpha:
                alpha.append(transition[1])
        return alpha

class Automate:
    etats = []

    entrees = []  # liste des états d'entrée
    sorties = []  # liste des états de sortie

    def set_etats(_self, etats):
        _self.etats = etats

    def set_entrees(_self, entrees):
        _self.entrees = entrees

    def set_sorties(_self, sorties):
        _self.sorties = sorties


automate = Automate()

etat3 = Etat()
etat3.set_name("3")
etat3.set_transitions([(etat3, "a"), (etat3, "b")])

etat2 = Etat()
etat2.set_name("2")
etat2.set_transitions([(etat3, "b")])

etat1 = Etat()
etat1.set_name("1")
etat1.set_transitions([(etat2, "a")])

automate.set_etats([etat1, etat2, etat3])
automate.set_entrees([etat1])
automate.set_sorties([etat3])


# Pour un automate fini A et un mot u sur son alphabet, tester si u est dans le langage de A
def question2_5_2(automate, u):
    def scan(start, word):
        if len(word) == 0 and start in automate.sorties:
            return True
        results = start.is_accessible_via(word[0])
        for result in results:
            return scan(result, word[1:])
        if len(results) == 0:
            return False

    for entre in automate.entrees:
        return scan(entre, u)


# print(question2_5_2(automate, "ab"))


# Pour un automate fini A, tester si le langage de A est vide
def question2_5_3(automate):
    if len(automate.sorties) == 0 or len(automate.entrees) == 0:
        return False
    for entree in automate.entrees:
        for sortie in automate.sorties:
            if entree.is_accessible(sortie):
                return False
    return True

etat3 = Etat()
etat3.set_name("3")
etat3.set_transitions([(etat3, "a"), (etat3, "b")])

etat2 = Etat()
etat2.set_name("2")

etat1 = Etat()
etat1.set_name("1")
etat1.set_transitions([(etat2, "a")])

automate.set_etats([etat1, etat2, etat3])
automate.set_entrees([etat1])
automate.set_sorties([etat3])

# print(question2_5_3(automate))

# Implementation de l’algorithme de minimisation d’un automate fini
def question2_5_4(automate):
    ensembles = []
    ensembles.append(list(set(automate.etats) - set(automate.sorties)))
    ensembles.append(automate.sorties)


    def ensemble_update(ensembles):
        map = [] # [(1, "a", 5, 1)]
        for ensemble in ensembles:
            for i in range(len(ensemble)):
                for transition in ensemble[i].transitions:
                    map.append((ensemble[i].name,transition[1],transition[0].name,get_id_ensemble_by_etat(transition[0], ensembles)))
        return map

    def get_id_ensemble_by_etat(etat, ensembles):
        for ensemble in ensembles:
            if etat in ensemble:
                return ensembles.index(ensemble)


                #if ensemble[i].get_transition_by_letter()
    return ensemble_update(ensembles)
    # return [[y.name for y in x] for x in ensembles]


automate = Automate()
etat1 = Etat()
etat1.set_name("1")

etat2 = Etat()
etat2.set_name("2")

etat3 = Etat()
etat3.set_name("3")

etat4 = Etat()
etat4.set_name("4")

etat5 = Etat()
etat5.set_name("5")

etat6 = Etat()
etat6.set_name("6")

etat1.set_transitions([(etat2,"b"),(etat5,"a")])
etat2.set_transitions([(etat1,"b")])
etat3.set_transitions([(etat4,"a"),(etat2,"b")])
etat4.set_transitions([(etat5,"b"),(etat6,"b")])
etat5.set_transitions([(etat5,"a"),(etat6,"b")])
etat6.set_transitions([(etat3,"b"),(etat4,"a")])

automate.set_etats([etat1, etat2, etat3, etat4,etat5,etat6])
automate.set_entrees([etat1])
automate.set_sorties([etat4,etat5,etat6])

print(question2_5_4(automate))
def question3_1_1(mot):

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
def question3_1_2(alphabet):

    ensMotPeriodique=[]

    for l1 in alphabet:
        for l2 in alphabet:
            for l3 in alphabet:
                periode = ""
                periode += l1
                periode += l2
                periode += l3
                ensMotPeriodique.append(periode*10)

    return ensMotPeriodique

# print(question3_1_2(["a","b"]))

#  pour un mot v, retourner le plus grand mot u tel que u est un préfixe de v et le miroir de
# u (noté u) est un suffixe de v
def question3_1_3(mot):
    pref=""
    n=len(mot)
    for i in range((n//2) if n%2 == 0 else (n//2)+1):
        if mot[i] == mot[n-i-1]:
            pref = pref + mot[i]
        else:
            return pref
    return pref

# print(question3_1_3("caaaac"))

# pour deux mots u et v de même longueur, retourner le mot contenant les caractères de u
# dans l’ordre aux positions impaires et ceux de v aux positions paires
def taktaktakquestion3_1_4(u,v):
    if len(u) != len(v):
        return False

    mot=""
    for i in range(len(v)):
        if i%2 == 0:
            mot += v[i]
        if i%2 != 0:
            mot += u[i]

    return mot

#  print(question3_1_4("emma", "marc"))

# pour un mot u, retourner la liste ordonnée lexicographiquement des caractères sans doublon

def question3_1_5(u):
    return sorted(set(u))

# print(question3_1_5("aaaaaccbjkkd"))

#  pour un mot u sur l’alphabet {a, b}, retourner le motif de longueur 3 le plus présent dans
# u. Par exemple, aba est présent 3 fois dans abababbaaba.

def question3_1_6(u):
    maxnb = 0
    result = ""
    def nb(mot, motif):
        cpt = 0
        while len(mot) >= 3:
            if mot[:3] == motif:
                cpt += 1
            mot = mot[1:]
        return cpt

    alphabet=list(set(u))
    for l1 in alphabet:
        for l2 in alphabet:
            for l3 in alphabet:
                periode = ""
                periode += l1
                periode += l2
                periode += l3
                tempnb = nb(u,periode)
                if tempnb >= maxnb:
                    maxnb=tempnb
                    result=periode

    return result

# print(question3_1_6("abababbaaba"))

#========================= En dimension 2 ==============================
m=[['a','a','b'],
   ['a','b','b']]

## pour une matrice M et un entier k, retourner le nombre de colonnes de M contenant au
# moins k fois le caractère ’a’
def question3_2_2(mat, k):
    counterCol = 0
    for col in range(len(mat[0])):
        countera = 0
        for ligne in range(len(mat)):
            if mat[ligne][col] == "a":
                countera += 1
        if countera >= k:
            counterCol += 1

    return counterCol

# print(question3_2_2(m,2))

# pour une matrice de mots, vérifier que pour chaque i > 0 et j > 0, le mot en position
# (i; j) a pour préfixe le mot en position (i - 1; j - 1)

def question3_2_3(m):
    for i in range(1, len(m)):
        for j in range(1, len(m[0])):
            pref = m[i - 1][j - 1]
            mot = m[i][j]
            n = len(pref)
            if pref != mot[:n]:
                return False
    return True


m=[['ta','to','toc'],
   ['tic','tac','toc']]

# print(question3_2_3(m))

# pour une matrice d’entiers, retourner i tel que la somme des éléments de la ligne i soit la
# plus grande parmi toutes les lignes
def question3_2_4(m):
    maxS = 0
    ligneR = 0
    for ligne in m:
        if maxS <= sum(ligne):
            maxS=sum(ligne)
            ligneR = ligne

    return m.index(ligneR)

m=[[1,2,13],
   [4,5,6]]

#print(question3_2_4(m))



def question3_2_5(n):
    res = [[0 for _ in range(n)] for _ in range(n)]
    res[0] = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(1, n):
            res[i][j] = res[i-1][j-1]+res[i][j-1]

    return res
#print(question3_2_5(5))

# pour une matrice M de mots, retourner la matrice de même taille contenant en position
# (i; j) la taille du mot en position (i; j) de M
def question3_2_5(m):
  return [[len(mot) for mot in line] for line in m]
    # m2 = []
    # lignes = [ligne for ligne in m]
    # for i in range(len(m)):
    #     taillemotligne = [len(mot) for mot in lignes[i]]
    #     m2.append(taillemotligne)
    # return m2

m=[['ta','to','toc'],
   ['tic','tac','toc']]

# print(question3_2_5(m))

# calculer le n-ième terme de la suite de Fibonacci donnée par u0 = 0, u1 = 1 et uk+2 =
# uk+1 + uk
def question3_3_1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return question3_3_1(n-2)+question3_3_1(n-1)

# print(question3_3_1(10))

# on note f la fonction qui à un entier pair k associe k=2 et à un entier impair k associe
# 3  k + 1. On appelle suite de Syracuse de k la suite k; f(k); f(f(k)); f(f(f(k))); : : : . On
# arrête la suite lorsqu’un des termes vaut 1.

def question3_3_2_1(k):
    tab = []

    def syra(k, tab):
        tab.append(k)
        if k == 1 or k == 0:
            return
        if k%2 == 0:
            syra(k//2, tab)
        else:
            syra(3*k+1, tab)

    syra(k, tab)
    return tab

# print(question3_3_2_1(10))

# Pour un entier n, calculer le plus petit entier k tel que la suite de Syracuse de k est
# de longueur au moins n.

def question3_3_2_2(n):
    res = 0
    i = 0
    while res < n:
        res = len(question3_3_2_1(i))
        i += 1
    return i-1

# print(question3_3_2_2(10))

# Montrer que pour tout k  50, la suite de Syracuse de k est finie (on tombe sur 1
# après un nombre fini d’étapes). Remarque : Savoir si toute suite de Syracuse est finie
# est une célèbre question ouverte.
def question3_3_2_3(k):
    for i in range(1,k):
        res = question3_3_2_1(i)
        if res[len(res)-1] != 1:
            print(res)
            return False
    return True

# print(question3_3_2_3(50))

# pour un mot u sur l’alphabet fa; b; c; : : : ; zg, remplacer en partant de la première lettre
# toute occurrence de deux lettres consécutives de l’alphabet par deux fois la lettre suivante.
# Exemple : ’efrhabdj’ devient ’ggrhccdj’.

def question3_3_3(mot):
    motList = list(mot)
    motListinit = list(mot)
    alphabet = list(string.ascii_lowercase)

    for i in range(len(motList)-1):
        indexLetter = alphabet.index(motListinit[i])
        indexNextLetter = alphabet.index(motListinit[i+1])
        if indexLetter+1 == indexNextLetter:
            motList[i] = alphabet[indexNextLetter+1]
            motList[i+1] = alphabet[indexNextLetter+1]

    return motList

# print(question3_3_3("efrhabdj"))

# pour un mot u appliquer la transformation précédente sur u puis sur l’image de u, etc. . .,
# jusqu’à obtenir un mot égal à son image. Exemple : ’efrhabdj’ devient ’ggrhccdj’ qui
# devient ’ggrhceej’.

def question3_3_4(u):
    currentRes = question3_3_3(u)
    previusRes = ""
    while currentRes != previusRes:
        previusRes = currentRes
        currentRes = question3_3_3(previusRes)

    return currentRes

# print(question3_3_4("efrhabdj"))
