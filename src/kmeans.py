import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def methode_coude(donnees):
    inerties = []
    for k in range(1, 11):
        modele = KMeans(n_clusters=k, random_state=42, n_init=10)
        modele.fit(donnees)
        inerties.append(modele.inertia_)

    plt.plot(range(1, 11), inerties, marker="o")
    plt.xlabel("Nombre de clusters")
    plt.ylabel("Inertie")
    plt.title("Méthode du coude")
    plt.show()


def appliquer_kmeans(donnees, n_clusters):

    modele = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = modele.fit_predict(donnees)

    return clusters