def classement_regions(df, variable):
    return df.sort_values(by=variable, ascending=False)


def moyenne_depenses_par_region(etats_financiers_regionaux):
    moyenne_depenses_region = etats_financiers_regionaux.groupby("Région")[
        "Montant 2023 (M€)"
    ].mean().reset_index()

    return moyenne_depenses_region