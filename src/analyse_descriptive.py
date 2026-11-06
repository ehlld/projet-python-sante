def classement_regions(df, variable):
    return df.sort_values(by=variable, ascending=False)