import statsmodels.api as sm


def regression_lineaire(df, variable_explicative, variable_expliquee):
    X = df[[variable_explicative]]
    X = sm.add_constant(X)
    y = df[variable_expliquee]

    modele = sm.OLS(y, X).fit()
    return modele


def plusieurs_regressions(df, variable_explicative, variables_expliquees):
    resultats = {}
    for variable in variables_expliquees:
        modele = regression_lineaire(df, variable_explicative, variable)
        resultats[variable] = modele
    return resultats


def tableau_resultats(resultats):
    lignes = []
    for variable, modele in resultats.items():
        lignes.append({
            "Variable expliquée": variable,
            "R²": modele.rsquared,
            "R² ajusté": modele.rsquared_adj,
            "Coefficient PIB": modele.params.iloc[1],
            "Constante": modele.params.iloc[0],
            "p-value": modele.pvalues.iloc[1]
        })
    return lignes