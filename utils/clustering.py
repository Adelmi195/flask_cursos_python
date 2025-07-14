import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Soluciona error del hilo principal en servidores sin GUI
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from scipy.spatial.distance import pdist, squareform
import io
import base64

def cargar_csv(file):
    df = pd.read_csv(file)
    df = df.select_dtypes(include=[np.number]).dropna()
    if df.empty:
        raise ValueError("El archivo no contiene columnas numéricas válidas.")
    return df

def normalizar_datos(df, normalizar=True):
    if normalizar:
        scaler = StandardScaler()
        return scaler.fit_transform(df)
    return df.values

def calcular_linkage(data, method='ward', metric='euclidean'):
    if method == 'ward':
        return linkage(data, method='ward')
    return linkage(data, method=method, metric=metric)

def asignar_clusters(linkage_matrix, n_clusters):
    return fcluster(linkage_matrix, n_clusters, criterion='maxclust')

def generar_dendrograma(linkage_matrix, n_clusters):
    fig, ax = plt.subplots(figsize=(10, 6))
    dendrogram(
        linkage_matrix,
        ax=ax,
        truncate_mode='level',
        p=30,
        show_leaf_counts=True,
        leaf_font_size=8,
        orientation='top'
    )
    if n_clusters > 1:
        alturas = sorted(linkage_matrix[:, 2])
        corte = alturas[-(n_clusters - 1)]
        ax.axhline(y=corte, color='red', linestyle='--', alpha=0.7, label=f'{n_clusters} clusters')
        ax.legend()

    ax.set_title("Dendrograma", fontsize=14)
    ax.set_xlabel("Índices o tamaños de cluster")
    ax.set_ylabel("Distancia")
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

def generar_scatter_plot(data, cluster_labels):
    fig, ax = plt.subplots(figsize=(10, 6))
    x = data[:, 0]
    y = data[:, 1]
    unique_labels = np.unique(cluster_labels)
    colors = plt.cm.tab10(np.linspace(0, 1, len(unique_labels)))
    for i, label in enumerate(unique_labels):
        mask = cluster_labels == label
        ax.scatter(x[mask], y[mask], c=[colors[i]], label=f"Cluster {label}", s=50)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Scatter Plot por Cluster")
    ax.legend()
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

def obtener_estadisticas_por_cluster(df, cluster_labels):
    df_copy = df.copy()
    df_copy["Cluster"] = cluster_labels
    resumen = {}

    for label in np.unique(cluster_labels):
        cluster_data = df_copy[df_copy["Cluster"] == label].drop(columns="Cluster")
        resumen[f"Cluster {label}"] = {
            "tamaño": len(cluster_data),
            "media": cluster_data.mean().to_dict(),
            "std": cluster_data.std().to_dict(),
            "min": cluster_data.min().to_dict(),
            "max": cluster_data.max().to_dict()
        }

    return resumen

def calcular_metricas_calidad(scaled_data, cluster_labels):
    silhouette = silhouette_score(scaled_data, cluster_labels)
    calinski = calinski_harabasz_score(scaled_data, cluster_labels)
    return {
        "silhouette": silhouette,
        "calinski": calinski
    }

def matriz_distancia_centroides(df, cluster_labels):
    df_copy = df.copy()
    df_copy["Cluster"] = cluster_labels
    centroids = []

    for label in np.unique(cluster_labels):
        centroid = df_copy[df_copy["Cluster"] == label].drop(columns="Cluster").mean().values
        centroids.append(centroid)

    dist_matrix = squareform(pdist(np.array(centroids)))
    return dist_matrix

def realizar_clustering(df):
    linkage_matrix = calcular_linkage(normalizar_datos(df))
    dendrograma = generar_dendrograma(linkage_matrix, n_clusters=2)  # valor por defecto para visualización básica
    return dendrograma
