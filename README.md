# Impact du niveau de richesse des régions sur le financement des structures hospitalières

## Objectif du projet
Ce projet vise à étudier les liens entre le niveau de richesse des régions de France et ses ressources hospitalières et à comparer les différentes régions.

## Plan
### 1. Récupération et traitement des données
Données utilisées :
- INSEE - PIB régional par habitant
- Agences régionales de santé (ARS) - Données financières des établissements de santé
- SAE 2023 : données statistiques sur les établissements de santé, notamment les données MCO (Médecine, Chirurgie et Obstétrique).

### 2. Analyse descriptive
Cette partie vise à décrire et visualiser les principales caractéristiques économiques et hospitalières des régions françaises.
Les analyses portent notamment sur :
- La comparaison du PIB par habitant entre les régions.
- L'étude des dépenses et des données financières hospitalières régionales.
- La représentation géographique des disparités économiques.

### 3. Étudier les relations entre richesse et ressources hospitalières
Dans cette partie, on propose d’effectuer une régression entre ces deux variables. L’objectif sera de déterminer si les différences de richesse sont associées à des différences de ressources hospitalières, sans présumer d’un lien de causalité.


### 4. Identifier des profils de territoires ou d’établissements (potentielle partie 4)
Dans cette dernière partie, on souhaite répondre à aux questions suivantes : Peut-on identifier différents profils d’établissements hospitaliers en fonction de leurs dépenses, de leurs ressources et des caractéristiques socio-économiques de leur territoire ? Ces profils présentent-ils des disparités géographiques ?
Pour celà, on envisage de faire un clustering à partir des données hspitalières afin d’identifer les différeents “profils” des hôpitaux puis de cartographier les résultats pour pouvoir effectuer une comparaison au niveau des régions.
Pour celà on s’appuye sur le dataset de l’année 2024 par exemple : https://data.drees.solidarites-sante.gouv.fr/explore/assets/708_bases-statistiques-sae/

## Organisation du projet : 

- projet-python-sante/
  - data/
    - MCO_2023r.csv         :   données pour la partie 4
    - Liste Variables.xlsx  :   données sur les nom ds varibles de la base de données MCO
  - src/
    - processing.py         :   préparation et traitement des données
    - visualisation.py      :   analyses statistiques descriptives
    - analyse_descriptive.py:   création des graphiques et des cartes ((Matplotlib, GeoPandas, Cartiflette))
    - regression.py         :   méthode de régression (statsmodels)
    - kmeans.py             :   méthode de clustering (sklearn.cluster)
  - projet.py               :   récupération et préparation des données
  - projet.ipynb            :   notebook présentant les analyses, les visualisations et les résultats du projet
  - README.md