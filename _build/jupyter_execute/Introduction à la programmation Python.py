#!/usr/bin/env python
# coding: utf-8

# # Introduction à la programmation Python
# Nous verrons les points suivants :
# 1. Les types de données simples
# 2. Les types de données composées
# 3. Les variables et identificateurs
# 4. Les structures de contrôle
# 5. Les fonctions
# 6. Le calcul scientifique
# 
# Dans tout langage de programmation, nous avons d'une part les **données** (ou **objets** ou **valeurs**), et d'autre part des **opérations** sur ces données.
# 
# Une donnée a un **type** qui est l'ensemble auquel appartient cette donnée. Donc un type permet de représenter un certain nombre de données.

# ## Les types de données simples

# ### Les entiers (integer ou int)
# Les entiers en Python sont semblables aux entiers relatifs en maths, donc l'ensemble $\mathbb{Z}$.
# 
# Le type entier (int) permet de représenter tous les nombres entiers relatifs (potentiellement une infinité)

# In[1]:


1


# In[2]:


-2


# In[3]:


-244555555


# In[4]:


type(-2)


# In[5]:


type(2124455882555)


# In[6]:


type(212445588255555555555555555555555555555)


# In[7]:


1 + 1 # addition


# In[8]:


2 - 1 # soustraction


# In[9]:


2 * 10 # multiplication


# In[10]:


5/2 # Division réelle


# In[11]:


5 // 2 # Division entière


# In[12]:


5 % 2 # Reste de la division entière


# In[13]:


6 % 2 # Reste de la division entière


# In[14]:


2 ** 10 # Puissance


# ### Les nombres à virgule flottante (float)
# Les flottants en Python sont semblables aux nombres réels en maths, donc l'ensemble $\mathbb{R}$.

# In[15]:


1.5


# In[16]:


-21.657787


# In[17]:


# Notation scientifique : xEa est équivalent à x * 10^a
2.5e3   # ou 2.5E3


# In[18]:


type(-21.657787)


# In[19]:


2.


# In[20]:


# Le module `math' contient de nombreuses fonctions sur les nombres et constantes 
import math


# In[21]:


math.pi


# In[22]:


math.e


# In[23]:


math.sqrt(25)   # racine carrée


# In[24]:


math.log(1)   # logarithme de base e, càd le logarithme népérien


# In[25]:


math.log(2)


# In[26]:


math.log(10**3, 10)   # logarithme de base 10


# In[27]:


math.exp(math.log(2))


# In[28]:


math.pow(2, 10)    # Elévation à la puissance


# In[29]:


math.sin(math.pi / 6)   # Sinus


# In[30]:


math.__dir__()   # La méthode __dir__() affiche les fonctions et constantes contenues dans un module


# ### Les chaînes de caractères (string ou str)
# Un string est une suite *ordonnée* de caractères alphanumériques et/ou spéciaux, délimitée par des guillemets (simples, doubles ou triples).

# In[31]:


"Python est un langage"


# In[32]:


"""Python est un langage"""


# In[33]:


'''Python est un langage'''


# In[34]:


"Python 3.0 & Java"


# In[35]:


'''L'école est "vitale"'''


# In[36]:


"Python 3.0 " + "&" + " Java"   # Concaténation


# In[37]:


"Python" * 5


# In[38]:


"Python"[0]  # Extraction de caractères


# In[39]:


"Python"[1]


# In[40]:


len("Python")


# In[41]:


"Python"[5]


# In[42]:


"Python"[-1]


# In[43]:


# Extraction de sous-chaîne. Syntaxe : chaine[a:b]
# `a' est la position initiale, et `b' est la position finale mais n'est pas incluse.
# Càd que [a:b] peut être vu comme un intervalle fermé en `a' et ouvert en `b': [a, b[
"Python"[2:6]


# In[44]:


"Python"[2:5]


# In[45]:


"Python"[2:]


# In[46]:


"Python"[:5]


# In[47]:


"Python"[:]


# In[48]:


"Python est un langage"[2::2]


# In[49]:


"Python est un langage".upper()  


# In[50]:


'PYTHON EST UN LANGAGE'.lower()


# In[51]:


'PYTHON EST UN LANGAGE'.startswith('PY')


# In[52]:


'PYTHON EST UN LANGAGE'.startswith('py')


# In[53]:


'PYTHON EST UN LANGAGE'.endswith('LANGAGE')


# In[54]:


'PYTHON EST UN LANGAGE'.endswith('langage')


# In[55]:


type('PYTHON EST UN LANGAGE')


# ### Le type booléen (bool)
# Un booléen est une valeur de vérité (vrai ou faux).<br>
# Le type booléen ne permet de représenter que 2 valeurs: **`True`** et **`False`**.

# In[56]:


True


# In[57]:


False


# In[58]:


type(True)


# In[59]:


False and True


# In[60]:


True and True


# In[61]:


True or False


# In[62]:


False or False


# In[63]:


True and (True or False)


# **Les conditions**
# 
# Une `condition` (ou `prédicat` ou `assertion`) est une expression Python dont la valeur est un booléen (True ou False).

# In[64]:


1 < 0


# In[65]:


2 >= 0


# In[66]:


1 == 1


# In[67]:


not True


# In[68]:


not False


# In[69]:


not(True)


# In[70]:


not(False)


# In[71]:


not(1 == 1)


# In[72]:


not(1 == 1) and 6 % 2 == 0


# ### Le type NoneType

# In[73]:


None


# In[74]:


type(None)


# ## Les types de données composées

# ### La liste (list)
# Une liste est une suite *ordonnée* d'éléments de tout type séparés par une virgule. La liste est délimitée par des *crochets*.

# In[75]:


[1, 2, "Python"]


# In[76]:


[1, 2, "Python", [0, -1]]


# In[77]:


type([1, 2, "Python"])


# In[78]:


[1, 2, "Python", [0, -1]] + ["test", "OK"]


# In[79]:


["test", "OK"] * 3


# In[80]:


[1, 2, "Python", [0, -1]][-1]


# In[81]:


[['Janvier', 20],
 ['février', 100]]


# ### Le tuple
# Un tuple est une suite *ordonnée* d'éléments de tout type séparés par une virgule. Le tuple est délimité par des *parenthèses*. La différence fondamentale entre un tuple et une liste est que le premier est **non mutable** et le dernier **mutable**.

# In[82]:


(1, 2, 3)


# In[83]:


type((1, 2, 3))


# ### Le dictionnaire (dict)
# Un dictionnaire est une suite *non ordonnée* d'éléments de la forme **clé:valeur** séparés par une virgule. Le dict est délimité par des *accolades*. La clé est de type non mutable (int, str, tuple) et la valeur est de tout type.

# In[84]:


{'Janvier': 20,
 'Février': 100,
 'Mars': 10.5}


# In[85]:


type({'Janvier': 20,
 'Février': 100,
 'Mars': 10.5})


# In[86]:


{'Janvier': 20, 'Février': 100, 'Mars': 10.5}['Janvier']


# **Personne**
# - Nom
# - Prenoms
# - Age
# - Niveau
# 
# Nom : "N'GORAN"<br>
# Prenoms: "Arnold"<br>
# Age : 31<br>
# Niveau : "PhD"<br>

# In[87]:


{"Nom": "N'GORAN", "Prénoms": "Arnold", 'Âge': 31, "Niveau": "PhD"}


# In[88]:


{"Nom": "N'GORAN", "Prénoms": "Arnold", 'Âge': 31, "Niveau": "PhD"}['Âge']


# In[89]:


{"Nom": "N'GORAN", "Prénoms": "Arnold", 'Âge': 31, "Niveau": "PhD"}["Prénoms"]


# In[90]:


{"Nom": "N'GORAN", "Prénoms": "Arnold", 'Âge': 31, "Niveau": "PhD"}.keys()


# In[91]:


{"Nom": "N'GORAN", "Prénoms": "Arnold", 'Âge': 31, "Niveau": "PhD"}.values()


# In[92]:


{"Nom": "N'GORAN", "Prénoms": "Arnold", 'Âge': 31, "Niveau": "PhD"}.items()


# ## Les variables et identificateurs
# Une variable est juste une **étiquette** (ou **libellé**) qu'on donne à une valeur (ou donnée).
# Une variable a un **identificateur** et une valeur.
# Un identificateur Python doit satisfaire les règles suivantes :
# - il est composé de caractères alphanumériques
# - il ne doit pas commencer par un chiffre ou par un opérateur Python
# - il ne doit pas comporter de caractères spéciaux (à l'exception de l'underscore) et d'opérateurs Python
# - il est sensible à la casse (majuscule et/ou minuscule)
# - il ne doit pas être un mot clé Python (e.g.: True , False, for, in, while, ...)

# **Identificateurs valides**: nom, Nom, NOM, liste_eleve, voiture1, int2float
# 
# **Identificateurs non valides**: 1nom, liste-eleve, liste/eleve, liste_élève, while, type

# In[93]:


langage = 'Python' # Assignation ou attribution ou affectation d'une valeur à un identificateur 


# In[94]:


langage


# In[95]:


langage * 2


# In[96]:


langage[0]


# Les types `str` et `tuple` ne sont pas **mutables**, càd que les données de ces types ne sont pas *modifiables sur place*.

# In[97]:


type(langage)


# In[98]:


langage[0] = 'p'


# In[9]:


vect = (1, -1, 2)


# In[10]:


vect[1] = 0   # On obtient une erreur car une donnée de type tuple ne peut pas être modifiée sur place.


# In[12]:


lst = [1, -1, 2]


# In[13]:


lst[1] = 0


# In[14]:


lst


# In[15]:


d = {'lang': 'Python', 'author': 'Guido Van Rossum', 'ver': '11.0'}


# In[16]:


d['ver']


# In[17]:


d['ver'] = '10.3'


# In[18]:


d


# ## Les structures de contrôle de flux
# Par défaut, l'interpréteur Python exécute le code de façon **séquentielle**, càd de haut en bas et de gauche à droite, sans faire de **sauts** ni de **répétition**.
# Les structures de contrôle de flux modifient cet état de fait. 

# ### Les structures conditionnelles : la structure if
# **Syntaxe**:
# ```
# if condition_1:
#     bloc_code_1
# elif condition_2:
#     bloc_code_2
# ...
# else:
#     bloc_code_defaut
# ```    

# In[6]:


# 1er cas : x est impair
x = 17
if x == 0:
    print(x, 'est un nombre nul')
elif x % 2 == 0:
    print(x, 'est un nombre pair')
else:
    print(x, 'est un nombre impair')


# In[7]:


# 2ème cas : x est pair
x = 20
if x == 0:
    print(x, 'est un nombre nul')
elif x % 2 == 0:
    print(x, 'est un nombre pair')
else:
    print(x, 'est un nombre impair')


# In[8]:


# Dernier cas : x est nul
x = 0
if x == 0:
    print(x, 'est un nombre nul')
elif x % 2 == 0:
    print(x, 'est un nombre pair')
else:
    print(x, 'est un nombre impair')


# ### Les boucles
# Une `boucle` permet de répéter l'exécution d'un code un certain nombre de fois.

# ### La boucle for
# **Syntaxe**:
# ```
# for [variable] in [sequence]:
#     bloc_code
# ```
# - **`[variable]`** est une variable quelconque qui prend sucessivement des valeurs dans [sequence].
# - **`[sequence]`** est une suite d'éléments (str, list, tuple, ...)

# In[24]:


for i in [1, 2, 3]:
    print(i)


# In[28]:


s = 'Python est un langage'
pos = 0
for c in s:
    print(pos, ':', c)
    pos = pos + 1


# In[30]:


pos = 0
depart = 10
for c in s:
    if pos >= depart:
        print(pos, ':', c)
    pos = pos + 1


# ### La boucle while
# **Syntaxe**:
# ```
# while [condition]:
#     bloc_code
# ```

# In[32]:


# boucle infinie
#while True:
#    print(1)


# In[33]:


n = 5
while n <= 8:
    print(n)
    n = n + 1


# In[ ]:


for i in [1, 2, 3]:
    print(i)


# In[36]:


lst = ["a", "z", "b"]
n = len(lst)
pos = 0
while pos < n:
    print(lst[pos])
    pos += 1


# In[37]:


lst = ["a", "z", "b"]
n = len(lst)
pos = 0
while pos < n:
    print(pos, ':', lst[pos])
    pos += 1


# In[40]:


list(enumerate(["a", "z", "x"]))  # retourne un générateur


# In[42]:


for i in enumerate(["a", "z", "x"]):
    print(i)


# In[45]:


x, y = (1, 2)  # dépaquetage


# In[44]:


print(x)
print(y)


# In[46]:


for idx, val in enumerate(["a", "z", "x"]):
    print(idx, ':', val)


# In[48]:


lst_lettres = ["zero", "un", 'deux', 'trois']
lst_chiffres = [0, 1, 2, 3, 4, 5, 6]
for l, c in zip(lst_lettres, lst_chiffres):
    print(l, ':', c)


# In[50]:


list(range(5))


# In[51]:


list(range(2, 5))


# In[52]:


list(range(3, 10, 2))


# In[53]:


for i in range(5):
    print(i)


# ## Les fonctions
# Les `fonctions` Python sont un peu comme les fonctions mathématiques : *Elles ont un nom, prennent des paramètres (ou variables) entre parenthèses, et retournent une valeur*. Contrairement aux fonctions mathématiques, les fonctions Python peuvent ne pas prendre de paramètres, et ne pas retourner de valeurs.
# 
# Les fonctions constituent une structure très importante en programmation. Ce sont une **abstraction** des langages, en ce sens qu'elles permettent d'identifier un bloc de code par un nom, et utiliser ce nom autant de fois qu'on veut, et obtenir des résultats différents selon les paramètres qu'on passe à la fonction.
# 
# **Syntaxe**:
# 
# **définition de la fonction:**
# ```
# def [nom_de_la_fonction](param_1, param_2, ...):
#     bloc_code
#     [return [variable]]
# ```
# 
# **appel de la fonction:**
# ```
# nom_de_la_fonction(arg_1, arg_2, ...)
# ```

# In[54]:


# Définition de la fonction
def somme2(a, b):
    return a + b


# In[55]:


# Appel de la fonction
somme2(1, -1)


# In[56]:


def afficher(x):
    print(x)


# In[57]:


afficher(10)


# In[58]:


afficher('Python est un langage')


# In[59]:


x = afficher('Python')


# In[60]:


x


# In[61]:


type(x)


# In[62]:


y = somme2(10, 15)


# In[63]:


y


# In[64]:


type(25)


# In[65]:


def zero_param():
    return True


# In[66]:


zero_param()


# **La fonction factorielle**
# $$n! = 1\times 2\times 3\times \cdots \times n$$
# $$0! = 1$$

# In[67]:


def factorielle(n):
    if n == 0:
        facto = 1
    else:
        facto = 1
        for i in range(1, n+1): # => [1, 2, 3, ..., n]
            facto = facto * i
    return facto


# In[68]:


factorielle(0)


# In[69]:


factorielle(1)


# In[70]:


factorielle(5)


# In[71]:


factorielle(6)


# In[72]:


factorielle(10)


# In[73]:


factorielle(100)


# **La fonction combinaison de p dans n**
# 
# $$C_{n}^p = \frac{n!}{p!(n-p)!}$$

# In[74]:


def combinaison(n, p):
    return factorielle(n) / (factorielle(p) * factorielle(n-p))


# In[75]:


combinaison(4, 2)


# In[76]:


combinaison(3, 2)


# In[77]:


combinaison(3, 0)


# **Détermination des racines d'une fonction du 2nd degré**
# 
# $$f(x) = ax^2 + bx + c\ \ (a\neq 0)$$
# 
# Discriminant : $\Delta = b^2 - 4ac$
# - Si $\Delta < 0$, $f(x)$ n'admet pas de racines.
# - Si $\Delta > 0$, $f(x)$ admet deux racines distinctes :
# 
# $$x_1 = \frac{-b-\sqrt{\Delta}}{2a}$$
# $$x_2 = \frac{-b+\sqrt{\Delta}}{2a}$$
# 
# - Si $\Delta = 0$, $f(x)$ admet une racine double :
# 
# $$x_0 = \frac{-b}{2a}$$

# In[80]:


def racines2nddegre(a, b, c):
    from math import sqrt
    delta = b**2 - 4 * a * c
    if delta < 0:
        print('La fonction {0}x^2 + {1}x + {2} n\'admet pas de racines'.format(a, b, c))
    elif delta > 0:
        x_1 = (-b - sqrt(delta)) / (2 * a)
        x_2 = (-b + sqrt(delta)) / (2 * a)
        print('La fonction {0}x^2 + {1}x + {2} admet deux racines disctinctes :'.format(a, b, c))
        print('--------')
        print('x_1 =', x_1)
        print('x_2 =', x_2)
        return (x_1, x_2)
    else:
        x_0 = -b / (2 * a)
        print('La fonction {0}x^2 + {1}x + {2} admet une racine double :'.format(a, b, c))
        print('--------')
        print('x_0 =', x_0)
        return x_0


# In[81]:


racines2nddegre(2, -1, -6) # x_1 = -1.5, x_2 = 2


# In[82]:


racines2nddegre(2, -3, 9/8) # x_0 = 3/4 = 0.75


# In[83]:


racines2nddegre(1, 1, 1) # aucune racine


# In[84]:


def somme_liste(lst):
    # Retourne la somme des éléments de la liste
    # passée en argument
    somme = 0
    for elt in lst:
        somme += elt
    return somme


# In[85]:


lst = [12, -1, 5, 3, 0, 20, 31, 40, 8]


# In[86]:


sum(lst)


# In[87]:


somme_liste(lst)


# In[88]:


def moy_liste(lst):
    return somme_liste(lst) / len(lst)


# In[89]:


moy_liste(lst)


# In[90]:


def somme3(a, b=0):
    return a + b


# In[91]:


somme3(1, 2)


# In[92]:


somme3(1)


# In[94]:


somme2(1, 2)


# ## Le calcul scientifique

# ### Le module numpy
# **Numpy** est un module qui permet de faire de l'algèbre linéaire (manipulation de `matrices` et des `tables multidimensionnelles`).

# In[97]:


import numpy as np  # pip install numpy


# In[98]:


v = np.array([1, 3, 2])


# In[99]:


v


# In[100]:


type(v)  # N dimensional array


# In[101]:


v.shape


# In[102]:


mat = np.array([[1, 3, 2],
                [0, -1, 5],
                [2, 1, 4]])


# In[103]:


type(mat)


# In[104]:


mat.shape


# In[106]:


np.ones([3, 5])  # génération d'une matrice composée de 1


# In[107]:


np.zeros([3, 5]) # génération d'une matrice nulle


# In[110]:


id_3 = np.eye(3) # génération d'une matrice identité


# In[113]:


mat


# In[114]:


id_3


# In[112]:


mat * id_3  # produit de matrices composante par composante de même index


# In[115]:


np.matmul(mat, id_3)   # produit matriciel


# In[119]:


# produit scalaire de 2 vecteurs x = [x1, x2, ..., xN] et y = [y1, y2, ..., yN]
# x1 * y1 + x2 * y2 + ... + xN * yN
x = np.array([1, 2, 0, 5])
y = np.array([-1, 5, 0, 2])
np.dot(x, y)


# In[120]:


x * y


# ### Le module pandas
# **Pandas** est un module développé au-dessus de Numpy. La structure de base de pandas est la `DataFrame` (ou table de données). Pandas est né de la volonté d'émuler les tableurs (type Excel et OpenOffice) dans Python.
# 
# Une dataframe est un array avec des *étiquettes* pour les colonnes et des *index* pour les lignes.

# In[121]:


import pandas as pd


# In[122]:


df = pd.DataFrame({'langages': ['Python', 'C', 'JavaScript', 'Lisp'],
                  'ver': ['10.3', '15', '6', '2']})


# In[123]:


df


# In[124]:


df.values  # Affiche les données de la dataframe, donc la matrice.


# In[125]:


df.shape  # dimension de la dataframe (nombre de lignes, nombre de colonnes)


# In[126]:


df.columns  # affiche les en-têtes ou étiquettes des colonnes


# In[127]:


df.index  # affiche les index des lignes


# In[128]:


df1 = pd.DataFrame({'langages': ['Python', 'C', 'JavaScript', 'Lisp'],
                  'ver': ['10.3', '15', '6', '2']},
                  index=['a', 'b', 'c', 'd'])


# In[129]:


df1


# In[9]:


df2 = df1.copy()  # crée une copie de la dataframe `df1'


# In[132]:


df2 is df1  # `is' est un opérateur qui teste l'identifie de 2 données. 


# In[133]:


df3 = df1


# In[134]:


df3 is df1


# In[135]:


df2


# In[136]:


df2.index = range(4)


# In[137]:


df2


# In[138]:


df2.rename(columns={'ver': 'version'})


# In[139]:


df2


# In[140]:


df2.rename(columns={'ver': 'version'}, inplace=True)


# In[141]:


df2


# In[143]:


df2.head(2)  # affiche les 2 premières lignes de la dataframe


# In[144]:


df2.tail()  # affiche les 5 dernières lignes de la dataframe


# In[145]:


df2.tail(2)


# In[146]:


df2.describe()  # affiche quelques statistiques descriptives liées à de la dataframe


# In[147]:


# Lecture d'un fichier de type CSV sous forme de dataframe
df_nba = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")


# In[148]:


df_nba.shape


# In[149]:


df_nba


# In[151]:


df_nba.dtypes  # affiche le type de chaque colonne de la dataframe


# In[152]:


# On extraie quelques colonnes de la dataframe
# `df_nba' est également une dataframe
df_nba = df_nba[['Number', 'Age', 'Weight', 'Salary']] 


# In[153]:


df_nba.head()


# In[154]:


df_nba.describe()


# In[156]:


# La méthode info() donne quelques infos sur la dataframe, 
# notamment son type, le nombre de ses lignes et de des colonnes,
# le type et nombre de valeurs non nulles de chaque colonne
# et la mémoire utilisée par la dataframe
df_nba.info()


# In[157]:


df_nba


# Une **`série`** est une dataframe composée d'une seule colonne (en dehors de la colonne des index).

# In[10]:


# La variable `salary' est obtenue en extrayant la colonne `Salary'. C'est donc une série.
salary = df_nba['Salary']


# In[159]:


type(salary)


# In[160]:


type(df_nba)


# In[161]:


salary


# In[162]:


salary.isna()  # Check les valeurs nulles de la colonne


# In[163]:


sum(salary.isna())


# In[165]:


salary.sum()  # Calcule la somme des valeurs de la colonne


# In[166]:


salary.plot()


# In[167]:


salary.hist(bins=10)


# In[168]:


mat


# In[169]:


mat_df = pd.DataFrame(data=mat, columns=['A', 'B', 'C'])


# In[170]:


mat_df


# In[171]:


mat_df_avec_index = pd.DataFrame(data=mat, columns=['A', 'B', 'C'], index=['a', 'b', 'c'])


# In[172]:


mat_df_avec_index


# In[173]:


A = [1, 3, 2]
B = [0, -1, 5]
C = [2, 1, 4]


# In[174]:


df_lst = pd.DataFrame({'A': A, 'B': B, 'C': C})


# In[175]:


df_lst


# In[176]:


df_lst = pd.DataFrame(data=zip(A, B, C))


# In[177]:


df_lst


# In[179]:


mat_2 = np.array([A, B, C])


# In[182]:


mat_2


# In[183]:


mat_2.T


# In[189]:


import datetime
start = datetime.datetime(2011, 1, 1)
end = datetime.datetime(2012, 1, 1)
rng = pd.date_range(start, end, freq="D")
ts = pd.Series(np.random.randn(len(rng)), index=rng)


# In[190]:


rng


# Une série dont les valeurs des index sont des dates (avec temps) est appelée **`série temporelle`** ou **`série chronologique`**.

# In[191]:


# La variable `ts' est une série temporelle.
ts


# In[192]:


ts.index


# In[193]:


ts.plot()


# In[ ]:




