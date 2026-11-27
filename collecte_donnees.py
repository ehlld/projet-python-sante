import pandas as pd
import openpyxl as op


URL_HABITANTS_REGIONS = "https://www.insee.fr/fr/statistiques/fichier/8680726/ensemble.xlsx"

URL_PIB_REGIONS = "https://www.insee.fr/fr/statistiques/fichier/8391986/PIB_REG_fr.xlsx"

URL_REGIONS = {
    "Auvergne-Rhône-Alpes": "https://www.ars.sante.fr/media/161664/download?inline",
    "Pays de la Loire": "https://www.ars.sante.fr/media/161666/download?inline",
    "Bourgogne-Franche-Comté": "https://www.ars.sante.fr/media/161669/download?inline",
    "Bretagne": "https://www.ars.sante.fr/media/161667/download?inline",
    "Centre-Val de Loire": "https://www.ars.sante.fr/media/161668/download?inline",
    "Corse": "https://www.ars.sante.fr/media/161653/download?inline",
    "Grand Est": "https://www.ars.sante.fr/media/161652/download?inline",
    "Guadeloupe": "https://www.ars.sante.fr/media/161655/download?inline",
    "Guyane": "https://www.ars.sante.fr/media/161654/download?inline",
    "Hauts-de-France": "https://www.ars.sante.fr/media/161656/download?inline",
    "Île-de-France": "https://www.ars.sante.fr/media/161657/download?inline",
    "La Réunion": "https://www.ars.sante.fr/media/161658/download?inline",
    "Martinique": "https://www.ars.sante.fr/media/161659/download?inline",
    "Mayotte": "https://www.ars.sante.fr/media/161661/download?inline",
    "Normandie": "https://www.ars.sante.fr/media/161660/download?inline",
    "Nouvelle-Aquitaine": "https://www.ars.sante.fr/media/161663/download?inline",
    "Occitanie": "https://www.ars.sante.fr/media/161662/download?inline",
    "Provence-Alpes-Côte d'Azur": "https://www.ars.sante.fr/media/161665/download?inline",
}

URL_BASE_SAE = "data/SAE_2023/Liste_variables_SAE_2023.xlsx"

URL_TAUX_PAUVRETE = "https://www.insee.fr/fr/statistiques/fichier/7941411/RPM2024-F21.xlsx"


def insee_pib():
    url_pib_region = pd.ExcelFile(URL_PIB_REGIONS)
    pib_region_brut = pd.read_excel(
        url_pib_region,
        sheet_name="PIB par habitant",
        header=3,
        index_col=None)

    pib_region_brut = pib_region_brut.rename(columns={"Unnamed: 0": "Région"})
    pib_region_epure = pib_region_brut[["Région", "2023"]]
    pib_region_epure["Région"] = pib_region_epure["Région"].str.strip()
    pib_region_epure = pib_region_epure.replace({"Guadeloupe (y compris Saint-Martin)": "Guadeloupe", "Mayotte*": "Mayotte"})
    pib_region_epure = pib_region_epure[pib_region_epure["Région"].isin(URL_REGIONS.keys())]
    return pib_region_epure


def url_to_data(url, region=None):
    url_excel = pd.ExcelFile(url)
    excel_brut = pd.read_excel(
        url_excel,
        sheet_name="Etat financier Financeur",
        skiprows=3)

    excel_epure = excel_brut.iloc[[1, 21, 27], 3:5]
    excel_epure = excel_epure.set_axis(["Catégorie", "Montant 2023 (M€)"], axis="columns")

    if region is not None:
        excel_epure["Région"] = region

    return (excel_epure)


def extract_habitants_region():
    excel_habitants_region = pd.ExcelFile(URL_HABITANTS_REGIONS)
    habitants_region_brut = pd.read_excel(
        excel_habitants_region,
        "Régions",
        header=7)

    habitants_region_epure = habitants_region_brut[["Nom de la région", "Population totale"]]
    return habitants_region_epure


def generate_etats_financiers_regionaux():
    tableau_financier = [url_to_data(url, region=region) for region, url in URL_REGIONS.items()]
    df_finances_regionales = pd.concat(tableau_financier, ignore_index=True)

    return df_finances_regionales


def generate_finances_regionales():
    df_finances_regionales = generate_etats_financiers_regionaux()

    habitants_region = extract_habitants_region()

    df_finances_regionales = df_finances_regionales.merge(
        habitants_region,
        left_on="Région",
        right_on="Nom de la région")

    df_finances_regionales = df_finances_regionales.drop(
        columns=["Nom de la région"])

    df_finances_regionales['ratio'] = df_finances_regionales["Montant 2023 (M€)"] * 1000 /\
        df_finances_regionales["Population totale"]

    # Réorganiser les données : une ligne par région
    df_pivot = df_finances_regionales.pivot(
        index="Région",
        columns="Catégorie",
        values="ratio"
    )
    return df_pivot



    # name_of_columns = tableau_financier[0].columns
    # etats_financier_regionaux = []
    # tableau_temporaire = ["Region"]
    # for name in tableau_financier[0][name_of_columns[0]]:
    #     tableau_temporaire.append(name)
    #     tableau_temporaire.append(name + " (en %)")

    # etats_financier_regionaux.append(tableau_temporaire)

    # for i in range(len(tableau_financier)):
    #     tableau_temporaire = []
    #     tableau_temporaire.append(tableau_regions[i])
    #     for row in tableau_financier[i].itertuples(index=False, name=None):
    #         if (i == 0):
    #             print(row)
    #         tableau_temporaire.append(row[1])
    #         tableau_temporaire.append(row[2] * 100)
    #     etats_financier_regionaux.append(tableau_temporaire)

    # return (etats_financier_regionaux)

    #if __name__ == "__main__":
    #   generate_etats_financiers_regionaux()
    #   print_table(generate_etats_financiers_regionaux())


def extract_pib_brut():
    insee_url = "https://www.insee.fr/fr/statistiques/fichier/8391986/PIB_REG_fr.xlsx"
    pib_brut = pd.read_excel(insee_url, sheet_name="PIB par habitant", header=None)
    return pib_brut


def extract_mco_sae():
    chemin = "data/SAE_2023/MCO_2023r.csv"
    mco = pd.read_csv(chemin, sep=";", encoding="latin-1")
    return mco


def extract_dictionnaire_sae():
    chemin = "data/SAE_2023/Liste_variables_SAE_2023.xlsx"
    dictionnaire = pd.read_excel(chemin, sheet_name=None)
    return dictionnaire