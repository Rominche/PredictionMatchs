import numpy as np
np.random.seed(7)
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.utils.validation import column_or_1d
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

def erreur_commise (valeurs_reelles, valeurs_predites):
    erreur = 0
    taille = valeurs_reelles.shape[0]  # nombre de valeurs incluses
    for i in range(0, taille):
        erreur = erreur+abs(valeurs_reelles[i]-valeurs_predites[i])
    return erreur


donnees_data_frame = pd.read_csv('../db/data2015_2016.csv', delimiter=" ")
donnees_ensemble_total = donnees_data_frame.values

donnees_data_frame2 = pd.read_csv('../db/data2012_2015.csv', delimiter=" ")
donnees_ensemble_total2 = donnees_data_frame2.values

nombre_lignes_base = donnees_ensemble_total.shape[0]
nombre_colonnes_base = donnees_ensemble_total.shape[1]

nombre_lignes_base2 = donnees_ensemble_total2.shape[0]
nombre_colonnes_base2 = donnees_ensemble_total2.shape[1]

x_train = donnees_ensemble_total2[0:nombre_lignes_base2, 1:nombre_colonnes_base2 - 4]
y_train = donnees_ensemble_total2[0:nombre_lignes_base2, nombre_colonnes_base2 - 1:]

x_test = donnees_ensemble_total[0:nombre_lignes_base, 1:nombre_colonnes_base - 4]
y_test = donnees_ensemble_total[0:nombre_lignes_base, nombre_colonnes_base - 1:]

# normalisation :
scaler = StandardScaler (with_mean=True, with_std=True)
scaler.fit (x_train)

#arbre de décision - importation de la classe
from sklearn.tree import DecisionTreeClassifier

### on veut un arbre de hauteur 2
#mon_arbre = DecisionTreeClassifier(max_depth=6)

#apprentissage
#mon_arbre.fit(x_train,y_train)

### pour avoir une belle grosse figure
from matplotlib.pyplot import figure
figure(figsize=(8,8))

# arbre de décision - importation de la classe
from sklearn.tree import DecisionTreeClassifier

from sklearn import tree

#tree.plot_tree(mon_arbre, filled=True, impurity=False, proportion=True, rounded=True)
#plt.show()

# arbre de décision - importation de la classe
from sklearn.tree import DecisionTreeClassifier

max_depth_courante = 1

while (max_depth_courante < 11):
    # while (max_depth_courante<30) and (not early_stopping) :
    mon_arbre = DecisionTreeClassifier(max_depth=max_depth_courante)

    mon_arbre.fit(x_train, y_train)

    y_predit_train = mon_arbre.predict(x_train)
    y_predit_test = mon_arbre.predict(x_test)

    if max_depth_courante == 1:  # premier point à ajouter :
        tableau_erreurs_train = np.array(100 - metrics.accuracy_score(y_train, y_predit_train) * 100)
        tableau_erreurs_test = np.array(100 - metrics.accuracy_score(y_test, y_predit_test) * 100)
    else:
        tableau_erreurs_train = np.append(tableau_erreurs_train,
                                          100 - metrics.accuracy_score(y_train, y_predit_train) * 100)
        tableau_erreurs_test = np.append(tableau_erreurs_test,
                                         100 - metrics.accuracy_score(y_test, y_predit_test) * 100)

    max_depth_courante = max_depth_courante + 1

#tree.plot_tree (mon_arbre, filled=True, impurity=False, proportion=True, rounded=True)
#plt.show()

tableau_erreurs_train = np.insert(tableau_erreurs_train, 0, 44.5)
tableau_erreurs_test = np.insert(tableau_erreurs_test, 0, 44.5)
plt.plot(tableau_erreurs_train, label="train")
plt.plot(tableau_erreurs_test, label="test")
plt.legend()
plt.title("Taux d'erreur avec hauteur variant de 1 à 10")
plt.xlim(1, 10)
plt.show()

#taux d'erreur
print ("\n\n===================\n")

y_predit_test = mon_arbre.predict (x_test)

#evaluation : taux d'erreur = 0.07

err = (1.0 - metrics.accuracy_score(y_test, y_predit_test))*100
print ("Erreur = ", round(err,2), "%")
print ("\n\n===================\n")