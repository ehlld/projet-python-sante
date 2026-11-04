import pandas as pd


def print_table(table):
    for row in table:
        formatted_row = [
            str(value)[:7] + "..." if len(str(value)) > 10 else str(value)
            for value in row
        ]
        print(" | ".join(formatted_row))


def url_to_data(url):
    line_of_url = [4, 5, 6, 14, 22, 25, 31, 34, 39, 40, 42]
    pib_url = pd.ExcelFile(url)
    pib_financier = pd.read_excel(
        pib_url, "Etat financier Financeur", usecols="D:F",
        skiprows=lambda x: x not in line_of_url)
    return (pib_financier)


def generate_etats_financiers_regionaux():
    # insee_url = "https://www.insee.fr/fr/statistiques/fichier/8391986/PIB_REG_fr.xlsx"
    auvergne_url = "https://www.ars.sante.fr/media/161664/download?inline"
    pays_loire_url = "https://www.ars.sante.fr/media/161666/download?inline"
    bourgogne_url = "https://www.ars.sante.fr/media/161669/download?inline"
    bretagne_url = "https://www.ars.sante.fr/media/161667/download?inline"
    centre_loire_url = "https://www.ars.sante.fr/media/161668/download?inline"
    corse_url = "https://www.ars.sante.fr/media/161653/download?inline"
    grand_est_url = "https://www.ars.sante.fr/media/161652/download?inline"
    guadeloupe_url = "https://www.ars.sante.fr/media/161655/download?inline"
    guyane_url = "https://www.ars.sante.fr/media/161654/download?inline"
    nord_url = "https://www.ars.sante.fr/media/161656/download?inline"
    idf_url = "https://www.ars.sante.fr/media/161657/download?inline"
    reunion_url = "https://www.ars.sante.fr/media/161658/download?inline"
    martinique_url = "https://www.ars.sante.fr/media/161659/download?inline"
    mayotte_url = "https://www.ars.sante.fr/media/161661/download?inline"
    normandie_url = "https://www.ars.sante.fr/media/161660/download?inline"
    aquitaine_url = "https://www.ars.sante.fr/media/161663/download?inline"
    occitanie_url = "https://www.ars.sante.fr/media/161662/download?inline"
    paca_url = "https://www.ars.sante.fr/media/161665/download?inline"

    tableau_url = [
        auvergne_url, pays_loire_url, bourgogne_url, bretagne_url,
        centre_loire_url, corse_url, grand_est_url, guadeloupe_url,
        guyane_url, nord_url, idf_url, reunion_url, martinique_url,
        mayotte_url, normandie_url, aquitaine_url, occitanie_url,
        paca_url]

    tableau_regions = [
        "Auvergne-Rhônes-Alpes", "Pays de la Loire", "Bourgogne-Franche-Comté", "Bretagne",
        "Centre-Val de Loire", "Corse", "Grand Est", "Guadeloupe", "Guyane", "Hauts-de-France",
        "Île-de-France", "La Réunion", "Martinique", "Mayotte", "Normandie",
        "Nouvelle-Aquitaine", "Occitanie", "Provence-Alpes-Côte d'Azur"]

    tableau_financier = []

    # pib = pd.ExcelFile(insee_url)
    # pib_2023 = pd.read_excel(
    #     pib, "PIB par habitant", usecols="A,AI",
    #     skiprows=[0, 1, 2, 3, 17, 18], skipfooter=9)

    for i in range(len(tableau_url)):
        tableau_financier.append(url_to_data(tableau_url[i]))

    name_of_columns = tableau_financier[0].columns
    etats_financier_regionaux = []
    tableau_temporaire = ["Region"]
    for name in tableau_financier[0][name_of_columns[0]]:
        tableau_temporaire.append(name)
        tableau_temporaire.append(name + " (en %)")

    etats_financier_regionaux.append(tableau_temporaire)

    for i in range(len(tableau_financier)):
        tableau_temporaire = []
        tableau_temporaire.append(tableau_regions[i])
        for row in tableau_financier[i].itertuples(index=False, name=None):
            tableau_temporaire.append(row[1])
            tableau_temporaire.append(row[2])
        etats_financier_regionaux.append(tableau_temporaire)

    return (etats_financier_regionaux)


if __name__ == "__main__":
    # generate_etats_financiers_regionaux()
    print_table(generate_etats_financiers_regionaux())
