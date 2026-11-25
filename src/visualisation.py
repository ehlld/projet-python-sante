import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np
import textwrap


def plot_pib_regions(df):
    plt.figure(figsize=(12, 7))
    plt.bar(df["Région"], df["PIB_par_habitant"])
    plt.title("PIB par habitant par région en 2023")
    plt.xlabel("Régions")
    plt.ylabel("PIB par habitant (€)")

    plt.xticks(rotation=75, ha="right")
    plt.tight_layout()
    plt.show()


def plot_carte_pib(pib_carte):

    url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions.geojson"

    regions = gpd.read_file(url)

    regions = regions.rename(columns={"nom": "Région"})

    carte = regions.merge(
        pib_carte,
        on="Région",
        how="left"
    )

    fig, ax = plt.subplots(figsize=(16, 16))
    carte.plot(column="PIB_par_habitant", legend=True, ax=ax)
    ax.set_title("PIB par habitant par région en 2023")
    ax.axis("off")

    plt.show()


def plot_regression(df, modele, variable_explicative, variable_expliquee, titre):

    fig, ax = plt.subplots(figsize=(10, 6))

    x = df[variable_explicative]
    y = df[variable_expliquee]

    # Nuage de points
    ax.scatter(x, y, label="Régions")

    # Droite de régression
    x_ligne = np.linspace(x.min(), x.max(), 100)

    y_ligne = (modele.params.iloc[0]+modele.params.iloc[1] * x_ligne)

    ax.plot(x_ligne, y_ligne)
    ax.set_title(titre)
    ax.set_xlabel("PIB par habitant (€)")
    ax.set_ylabel("\n".join(textwrap.wrap(variable_expliquee, width=35)))
    ax.legend()

    plt.tight_layout()
    plt.show()


def plot_etats_financiers(etats_financier):

    # Réorganiser les données : une ligne par région
    tableau = etats_financier.pivot(
        index="Région",
        columns="Catégorie",
        values="Montant 2023 (M€)"
    )

    # Récupérer les montants de chaque catégorie
    dram = tableau["DEPENSES DES REGIMES D'ASSURANCE MALADIE (hors contribution aux dépenses des ESMS pour personnes âgées et handicapées)"]

    fir = tableau["FONDS D'INTERVENTION REGIONAL (FIR)"]

    decaissement = tableau["DEPENSES DES REGIMES D'ASSURANCE MALADIE ET DE LA CAISSE NATIONALE DE SOLIDARITE POUR L'AUTONOMIE (décaissements)"]

    # Trier les régions selon les dépenses DRAM
    tableau = tableau.sort_values(
        by="DEPENSES DES REGIMES D'ASSURANCE MALADIE (hors contribution aux dépenses des ESMS pour personnes âgées et handicapées)",
        ascending=False
    )

    # Mettre à jour les montants après le tri
    dram = tableau["DEPENSES DES REGIMES D'ASSURANCE MALADIE (hors contribution aux dépenses des ESMS pour personnes âgées et handicapées)"]

    fir = tableau["FONDS D'INTERVENTION REGIONAL (FIR)"]

    decaissement = tableau["DEPENSES DES REGIMES D'ASSURANCE MALADIE ET DE LA CAISSE NATIONALE DE SOLIDARITE POUR L'AUTONOMIE (décaissements)"]

    regions = tableau.index

    x = np.arange(len(regions))
    width = 0.2

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.bar(x - width, dram, width, label="DRAM")
    ax.bar(x, fir, width, label="FIR")
    ax.bar(x + width, decaissement, width, label="CNSA (décaissements)")

    ax.set_xticks(x)
    ax.set_xticklabels(regions, rotation=45, ha="right")

    ax.set_ylabel("Dépenses (en millions d'euros)")
    ax.set_title("Comparaison des dépenses par région")

    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()
    plt.show()