import matplotlib.pyplot as plt
import geopandas as gpd


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

    carte.plot(column="PIB_par_habitant", legend=True)
    ax.set_title("PIB par habitant par région en 2023")
    ax.axis("off")

    plt.show()
