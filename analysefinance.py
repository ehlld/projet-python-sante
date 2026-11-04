import matplotlib.pyplot as plt
import numpy as np
from projet import generate_etats_financiers_regionaux


def trace_graph():
    etats_financier = generate_etats_financiers_regionaux()

    # Extract regions
    regions = [row[0] for row in etats_financier[1:]]

    # Extract financial data (correct column indexes)
    dram = [row[1] for row in etats_financier[1:]]
    fir = [row[9] for row in etats_financier[1:]]
    decaissement = [row[11] for row in etats_financier[1:]]

    sorted_data = sorted(
        zip(regions, dram, fir, decaissement),
        key=lambda row: row[1],
        reverse=True
    )

    # Unpack sorted data
    regions, dram, fir, decaissement = zip(*sorted_data)
    print("Number of regions:", len(regions))

    x = np.arange(len(regions))
    width = 0.2

    fig, ax = plt.subplots(figsize=(16, 8))

    ax.bar(x - 1*width, dram, width, label="DEPENSES DES REGIMES D'ASSURANCE MALADIE")
    ax.bar(x, fir, width, label="FIR")
    ax.bar(
        x + 1*width, decaissement, width,
        label="DEPENSES DES REGIMES D'ASSURANCE MALADIE \
        ET DE LA CAISSE NATIONALE DE SOLIDARITE POUR L'AUTONOMIE")

    ax.set_xticks(x)
    ax.set_xticklabels(regions, rotation=45, ha="right")

    ax.set_ylabel("Dépenses (en millions d'euros)")
    ax.set_title("Comparaison des dépenses par région")

    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()
    print("Number of bars:", len(ax.patches))
    # Save before closing
    fig.savefig("graphique_financier.png", dpi=300, bbox_inches="tight")

    print("Graphique enregistré !")
    plt.close(fig)


if __name__ == "__main__":
    trace_graph()
