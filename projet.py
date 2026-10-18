import pandas as pd

# import matplotlib as mp


insee_url = "https://www.insee.fr/fr/statistiques/fichier/8391986/PIB_REG_fr.xlsx"
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

pib = pd.ExcelFile(insee_url)
pib_2023 = pd.read_excel(
    pib, "PIB par habitant", usecols="A,AI",
    skiprows=[0, 1, 2, 3, 17, 18], skipfooter=9)
pib_2023 = pd.DataFrame.to_csv(pib_2023)
# print(pib_2023)

auvergne_pib = pd.ExcelFile(auvergne_url)
auvergne_financier = pd.read_excel(
    auvergne_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
auvergne_financier = pd.DataFrame.to_csv(auvergne_financier)
# print(auvergne_financier)

pays_loire_pib = pd.ExcelFile(pays_loire_url)
pays_loire_financier = pd.read_excel(
    pays_loire_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
pays_loire_financier = pd.DataFrame.to_csv(pays_loire_financier)

bourgogne_pib = pd.ExcelFile(bourgogne_url)
bourgogne_financier = pd.read_excel(
    bourgogne_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
bourgogne_financier = pd.DataFrame.to_csv(bourgogne_financier)

bretagne_pib = pd.ExcelFile(bretagne_url)
bretagne_financier = pd.read_excel(
    bretagne_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
bretagne_financier = pd.DataFrame.to_csv(bretagne_financier)

centre_loire_pib = pd.ExcelFile(centre_loire_url)
centre_loire_financier = pd.read_excel(
    centre_loire_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
centre_loire_financier = pd.DataFrame.to_csv(centre_loire_financier)

corse_pib = pd.ExcelFile(corse_url)
corse_financier = pd.read_excel(
    corse_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
corse_financier = pd.DataFrame.to_csv(corse_financier)

grand_est_pib = pd.ExcelFile(grand_est_url)
grand_est_financier = pd.read_excel(
    grand_est_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
grand_est_financier = pd.DataFrame.to_csv(grand_est_financier)

guadeloupe_pib = pd.ExcelFile(guadeloupe_url)
guadeloupe_financier = pd.read_excel(
    guadeloupe_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
guadeloupe_financier = pd.DataFrame.to_csv(guadeloupe_financier)

guyane_pib = pd.ExcelFile(guyane_url)
guyane_financier = pd.read_excel(
    guyane_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
guyane_financier = pd.DataFrame.to_csv(guyane_financier)

nord_pib = pd.ExcelFile(nord_url)
nord_financier = pd.read_excel(
    nord_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
nord_financier = pd.DataFrame.to_csv(nord_financier)

idf_pib = pd.ExcelFile(idf_url)
idf_financier = pd.read_excel(
    idf_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
idf_financier = pd.DataFrame.to_csv(idf_financier)

reunion_pib = pd.ExcelFile(reunion_url)
reunion_financier = pd.read_excel(
    reunion_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
reunion_financier = pd.DataFrame.to_csv(reunion_financier)

martinique_pib = pd.ExcelFile(martinique_url)
martinique_financier = pd.read_excel(
    martinique_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
martinique_financier = pd.DataFrame.to_csv(martinique_financier)

mayotte_pib = pd.ExcelFile(mayotte_url)
mayotte_financier = pd.read_excel(
    mayotte_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
mayotte_financier = pd.DataFrame.to_csv(mayotte_financier)

normandie_pib = pd.ExcelFile(normandie_url)
normandie_financier = pd.read_excel(
    normandie_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
normandie_financier = pd.DataFrame.to_csv(normandie_financier)

aquitaine_pib = pd.ExcelFile(aquitaine_url)
aquitaine_financier = pd.read_excel(
    aquitaine_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
aquitaine_financier = pd.DataFrame.to_csv(aquitaine_financier)

occitanie_pib = pd.ExcelFile(occitanie_url)
occitanie_financier = pd.read_excel(
    occitanie_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
occitanie_financier = pd.DataFrame.to_csv(occitanie_financier)

paca_pib = pd.ExcelFile(paca_url)
paca_financier = pd.read_excel(
    paca_pib, "Etat financier Financeur", usecols="D:F",
    skiprows=lambda x: x not in [5, 6, 14, 22, 25, 31, 34, 39, 40, 42])
paca_financier = pd.DataFrame.to_csv(paca_financier)

print(paca_financier)