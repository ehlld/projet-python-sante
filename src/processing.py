import pandas as pd

def prepare_pib_data(pib_brut):

    # Récupération des années : ligne 4, à partir de la deuxième colonne
    annees = pib_brut.iloc[3, 1:].tolist()

    # Récupération des données à partir de la ligne 5
    pib = pib_brut.iloc[4:, :len(annees) + 1].copy()

    # Renommer les colonnes
    pib.columns = ["Région"] + annees

    # Supprimer les lignes vides
    pib = pib.dropna(subset=["Région"])

    # Nettoyer les noms des régions
    pib["Région"] = pib["Région"].astype(str).str.strip()

    # Supprimer les agrégats nationaux
    regions_exclues = [
        "France métropolitaine hors île de France",
        "France métropolitaine",
        "Départements d'Outre-mer",
        "France",
        "Territoire extrarégional français",
        "Territoire économique de la France"
    ]

    pib = pib[~pib["Région"].isin(regions_exclues)].copy()

    # Convertir les données en valeurs numériques
    colonnes_annees = pib.columns[1:]

    for colonne in colonnes_annees:
        pib[colonne] = pd.to_numeric(pib[colonne], errors="coerce")

    return pib


def extract_pib_2023(pib):
    pib_2023 = pib[["Région", 2023.0]].copy()
    pib_2023 = pib_2023.rename( columns={2023.0: "PIB_par_habitant"} )
    return pib_2023


def prepare_pib_map(pib_2023):

    pib_carte = pib_2023.copy()

    pib_carte["Région"] = pib_carte["Région"].str.strip()

    pib_carte["Région"] = pib_carte["Région"].replace({
        "Guadeloupe (y compris Saint-Martin)": "Guadeloupe",
        "Mayotte*": "Mayotte"
    })

    regions_exclues = [
        "France métropolitaine",
        "France métropolitaine hors île de France",
        "Départements d'Outre-mer",
        "France",
        "Territoire économique de la France"
    ]

    pib_carte = pib_carte[
        ~pib_carte["Région"].isin(regions_exclues)
    ].copy()

    return pib_carte