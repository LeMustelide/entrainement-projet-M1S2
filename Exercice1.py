import random

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
    for m in range(2, n-1):
        if n%m == 0 :
            return "n'est pas premier"
    return "est premier"

# print(question2_1_4(79))

def question2_1_5(m, n):
    while m%n == 0:
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
        result += i*k
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
    compteur = {} # création d'un dictionnaire
    for e in tab:
        compteur[e] = compteur.get(e, 0) + 1 # pour chaque élément de e je rajoute un a la valeur du compteur pour la clef e, soit je fait la somme du nombre d'individu par type
    return max(compteur.items(), key=lambda x: x[1]) # je retourne l'item ayant la valeur la plus élevé

# print(question2_2_5([1,1,2,3,5,]))

def question2_2_6(tab):
    return len(question2_2_4(tab)) != len(tab)

# print(question2_2_6([12,12,24]))

def question2_2_7(k, n):
    tab = [random.randint(0,n) for _ in range(k)]
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
    return {key: random.randint(0,20) for key in tab}

# print(question2_3_3(["mourc", "enzo"]))


# 2.4

class graph:
    sommets = [] #sommets = [A,B,C]
    arêtes = [{}] # arêtes = [{A,B},{B,C}]

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
G.set_arêtes([{"A", "B"}, {"B", "C"}, {"C", "D"}])

print(question2_4_1(G))

# retourne le degre maximal du graphe
def question2_4_2(graph):
    degre = 0
    for sommet in graph.sommets:
        degre = max(degre, sum([1 for arête in graph.arêtes if sommet in arête]))
    return degre

print(question2_4_2(G))

# retourne la liste des sommets directement connectés à x
def question2_4_3(graph, x):
    sommet_connexe = []
    for arête in graph.arêtes:
        if x in arête:
            sommet_connexe.append(arête - {x})
    return sommet_connexe

print(question2_4_3(G, "B"))

# verifie la connectivité du graphe
# def question2_4_4(graph):
#     if question2_4_1(graph):
#         return False
#     liste_sommets = graph.sommets
#     for sommet in graph.sommets:
#         sommet_parcouru = [sommet]
        
        

        
# print(question2_4_4(G))

# Question inutilement complexe

# Jamais je ferais de langage et automate JAMAIS