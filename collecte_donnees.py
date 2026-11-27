import pandas as pd
import openpyxl as op


URL_BASE_SAE = "data/SAE_2023/Liste_variables_SAE_2023.xlsx"

URL_TAUX_PAUVRETE = "https://static.data.gouv.fr/resources/taux-de-pauvrete/20261104-151329/taux-de-pauvrete-region.csv"

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


CORRESPONDANCE_DEPARTEMENT_REGION = [
    ("01", "Auvergne-Rhône-Alpes"),
    ("02", "Hauts-de-France"),
    ("03", "Auvergne-Rhône-Alpes"),
    ("04", "Provence-Alpes-Côte d'Azur"),
    ("05", "Provence-Alpes-Côte d'Azur"),
    ("06", "Provence-Alpes-Côte d'Azur"),
    ("07", "Auvergne-Rhône-Alpes"),
    ("08", "Grand Est"),
    ("09", "Occitanie"),
    ("10", "Grand Est"),
    ("11", "Occitanie"),
    ("12", "Occitanie"),
    ("13", "Provence-Alpes-Côte d'Azur"),
    ("14", "Normandie"),
    ("15", "Auvergne-Rhône-Alpes"),
    ("16", "Nouvelle-Aquitaine"),
    ("17", "Nouvelle-Aquitaine"),
    ("18", "Centre-Val de Loire"),
    ("19", "Nouvelle-Aquitaine"),
    ("2A", "Corse"),
    ("2B", "Corse"),
    ("21", "Bourgogne-Franche-Comté"),
    ("22", "Bretagne"),
    ("23", "Nouvelle-Aquitaine"),
    ("24", "Nouvelle-Aquitaine"),
    ("25", "Bourgogne-Franche-Comté"),
    ("26", "Auvergne-Rhône-Alpes"),
    ("27", "Normandie"),
    ("28", "Centre-Val de Loire"),
    ("29", "Bretagne"),
    ("30", "Occitanie"),
    ("31", "Occitanie"),
    ("32", "Occitanie"),
    ("33", "Nouvelle-Aquitaine"),
    ("34", "Occitanie"),
    ("35", "Bretagne"),
    ("36", "Centre-Val de Loire"),
    ("37", "Centre-Val de Loire"),
    ("38", "Auvergne-Rhône-Alpes"),
    ("39", "Bourgogne-Franche-Comté"),
    ("40", "Nouvelle-Aquitaine"),
    ("41", "Centre-Val de Loire"),
    ("42", "Auvergne-Rhône-Alpes"),
    ("43", "Auvergne-Rhône-Alpes"),
    ("44", "Pays de la Loire"),
    ("45", "Centre-Val de Loire"),
    ("46", "Occitanie"),
    ("47", "Nouvelle-Aquitaine"),
    ("48", "Occitanie"),
    ("49", "Pays de la Loire"),
    ("50", "Normandie"),
    ("51", "Grand Est"),
    ("52", "Grand Est"),
    ("53", "Pays de la Loire"),
    ("54", "Grand Est"),
    ("55", "Grand Est"),
    ("56", "Bretagne"),
    ("57", "Grand Est"),
    ("58", "Bourgogne-Franche-Comté"),
    ("59", "Hauts-de-France"),
    ("60", "Hauts-de-France"),
    ("61", "Normandie"),
    ("62", "Hauts-de-France"),
    ("63", "Auvergne-Rhône-Alpes"),
    ("64", "Nouvelle-Aquitaine"),
    ("65", "Occitanie"),
    ("66", "Occitanie"),
    ("67", "Grand Est"),
    ("68", "Grand Est"),
    ("69", "Auvergne-Rhône-Alpes"),
    ("70", "Bourgogne-Franche-Comté"),
    ("71", "Bourgogne-Franche-Comté"),
    ("72", "Pays de la Loire"),
    ("73", "Auvergne-Rhône-Alpes"),
    ("74", "Auvergne-Rhône-Alpes"),
    ("75", "Île-de-France"),
    ("76", "Normandie"),
    ("77", "Île-de-France"),
    ("78", "Île-de-France"),
    ("79", "Nouvelle-Aquitaine"),
    ("80", "Hauts-de-France"),
    ("81", "Occitanie"),
    ("82", "Occitanie"),
    ("83", "Provence-Alpes-Côte d'Azur"),
    ("84", "Provence-Alpes-Côte d'Azur"),
    ("85", "Pays de la Loire"),
    ("86", "Nouvelle-Aquitaine"),
    ("87", "Nouvelle-Aquitaine"),
    ("88", "Grand Est"),
    ("89", "Bourgogne-Franche-Comté"),
    ("90", "Bourgogne-Franche-Comté"),
    ("91", "Île-de-France"),
    ("92", "Île-de-France"),
    ("93", "Île-de-France"),
    ("94", "Île-de-France"),
    ("95", "Île-de-France"),
]


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

    habitants_region_epure = habitants_region_brut[["Nom de la région", "Population totale"]]\
        .rename(columns={"Nom de la région": "Région"})
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
        on="Région")

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
    chemin = "/home/onyxia/work/projet-python-sante/data/SAE_2023/MCO_2023r.csv"
    mco = pd.read_csv(chemin, sep=";", encoding="latin-1")
    return mco


def epure_mco():
    habitants_region = extract_habitants_region()

    mco_brut = extract_mco_sae()
    mco_epure = mco_brut[["FI", "LIT_MED"]].dropna()
    mco_epure["FI"] = mco_epure["FI"].str[:2]
    df_correspondance = pd.DataFrame(
        CORRESPONDANCE_DEPARTEMENT_REGION,
        columns=["Code_departement", "Région"]
    )
    mco_epure = mco_epure.rename(columns={"FI": "Code_departement"})
    df_correspondance["Code_departement"] = df_correspondance["Code_departement"].astype(str)
    mco_region = mco_epure.merge(
        df_correspondance,
        on="Code_departement",
    ).drop(columns="Code_departement")
    mco_fusion_instances_region = (
        mco_region.groupby("Région", as_index=False)
        ["LIT_MED"]
        .sum()
    )
    mco_nombre_habitants = mco_fusion_instances_region.merge(
        habitants_region,
        on="Région")
    mco_nombre_habitants['ratio'] = mco_nombre_habitants["LIT_MED"] /\
        mco_nombre_habitants["Population totale"]
    return mco_nombre_habitants


def extract_dictionnaire_sae():
    chemin = "/home/onyxia/work/projet-python-sante/data/SAE_2023/Liste_variables_SAE_2023.xlsx"
    dictionnaire = pd.read_excel(chemin, sheet_name=None)
    return dictionnaire


def pauvrete():
    pauvrete_brut = pd.read_csv(URL_TAUX_PAUVRETE, sep=",", encoding="utf-8")
    pauvrete_epure = pauvrete_brut[["libelle_region", "valeur"]].dropna()
    pauvrete_epure = pauvrete_epure[~pauvrete_epure["libelle_region"].isin(["La Réunion"])]
    return pauvrete_epure
