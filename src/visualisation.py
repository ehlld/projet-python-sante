import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np
import textwrap
from cartiflette import carti_download


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

    regions = carti_download(
        values=["France"],
        crs=4326,
        borders="REGION",
        vectorfile_format="geojson",
        simplification=50,
        filter_by="FRANCE_ENTIERE",
        source="EXPRESS-COG-CARTO-TERRITOIRE",
        year=2022
    )
    # Garder uniquement les régions métropolitaines pour une image plus grande
    regions = regions[regions["INSEE_REG"] >= 11]

    regions = regions.rename( columns={"LIBELLE_REGION": "Région"})

    carte = regions.merge(
        pib_carte,
        on="Région",
        how="left"
    )

    fig, ax = plt.subplots(figsize=(16, 16))

    carte.plot(
        column="PIB_par_habitant",
        legend=True,
        ax=ax
    )

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


def plot_etats_financiers(tableau):

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

    ax.set_ylabel("Dépenses (en euro) par habitant")
    ax.set_title("Comparaison des dépenses par région")

    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()
    plt.show()


def visualiser_clusters_departements(mco_selection):
    repartition_departements = mco_selection.groupby(
        ["Departement", "Cluster"]
    ).size().unstack(fill_value=0)

    repartition_departements.plot(
        kind="bar",
        stacked=True,
        figsize=(15, 6)
    )

    plt.title("Répartition des établissements par département et par cluster")
    plt.xlabel("Département")
    plt.ylabel("Nombre d'établissements")
    plt.legend(title="Cluster")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def visualiser_clusters_carte(mco_selection):
   
    carte_departements = carti_download(
        values=["France"],
        crs=4326,
        borders="DEPARTEMENT",
        vectorfile_format="geojson",
        simplification=50,
        filter_by="FRANCE_ENTIERE",
        source="EXPRESS-COG-CARTO-TERRITOIRE",
        year=2022
    )
    repartition = mco_selection.groupby(
        ["Departement", "Cluster"]
    ).size().unstack(fill_value=0)

    carte = carte_departements.merge(
        repartition,
        left_on="INSEE_DEP",
        right_index=True,
        how="left"
    )

    clusters = repartition.columns
    carte[clusters] = carte[clusters].fillna(0)

    # Séparer la métropole et les départements d'outre-mer
    carte_metropole = carte[
        ~carte["INSEE_DEP"].astype(str).str.startswith("97")
    ]

    carte_outremer = carte[
        carte["INSEE_DEP"].astype(str).str.startswith("97")
    ]

    for cluster in clusters:

        fig, axes = plt.subplots(
            1, 2,
            figsize=(22, 12),
            gridspec_kw={"width_ratios": [3, 1]}
        )

        # Carte de la métropole
        carte_metropole.plot(
            column=cluster,
            cmap="Blues",
            legend=True,
            edgecolor="black",
            linewidth=0.4,
            ax=axes[0]
        )

        axes[0].set_title(
            f"France métropolitaine - Cluster {cluster}",
            fontsize=16
        )
        axes[0].axis("off")

        # Carte de l'outre-mer
        carte_outremer.plot(
            column=cluster,
            cmap="Blues",
            legend=False,
            edgecolor="black",
            linewidth=0.4,
            ax=axes[1]
        )

        axes[1].set_title(
            "Départements d'outre-mer",
            fontsize=14
        )
        axes[1].axis("off")

        plt.tight_layout()
        plt.show()
