from flask import Flask, render_template, request
import pandas as pd
from utils.clustering import (
    cargar_csv, normalizar_datos, calcular_linkage,
    asignar_clusters, generar_dendrograma, generar_scatter_plot,
    obtener_estadisticas_por_cluster, calcular_metricas_calidad,
    matriz_distancia_centroides
)
from utils.simulador import simular_datos

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/analisis')
def analisis():
    return render_template("analisis.html")

@app.route('/analizar_csv', methods=["POST"])
def analizar_csv():
    try:
        archivo = request.files["file"]
        method = request.form["method"]
        metric = request.form["metric"]
        n_clusters = int(request.form["n_clusters"])
        normalize = "normalize" in request.form

        df = cargar_csv(archivo)
        data = normalizar_datos(df, normalizar=normalize)
        linkage_matrix = calcular_linkage(data, method=method, metric=metric)
        cluster_labels = asignar_clusters(linkage_matrix, n_clusters)
        dendrograma = generar_dendrograma(linkage_matrix, n_clusters)
        scatter = generar_scatter_plot(data, cluster_labels)
        estadisticas = obtener_estadisticas_por_cluster(df, cluster_labels)
        metricas = calcular_metricas_calidad(data, cluster_labels)
        dist_matrix = matriz_distancia_centroides(df, cluster_labels)

        return render_template("resultados.html",
            datos=df.to_html(classes="table table-bordered", index=False),
            dendrograma=dendrograma,
            scatter=scatter,
            estadisticas=estadisticas,
            metricas=metricas,
            dist_matrix=dist_matrix
        )

    except Exception as e:
        return f"Error en análisis CSV: {str(e)}"

@app.route('/analizar_simulacion', methods=["POST"])
def analizar_simulacion():
    try:
        n_samples = int(request.form["n_samples"])
        n_features = int(request.form["n_features"])
        n_centers = int(request.form["n_centers"])
        method = request.form["method"]
        metric = request.form["metric"]
        n_clusters = int(request.form["n_clusters"])
        normalize = "normalize" in request.form

        df = simular_datos(n_samples=n_samples, n_features=n_features, n_centers=n_centers)
        data = normalizar_datos(df, normalizar=normalize)
        linkage_matrix = calcular_linkage(data, method=method, metric=metric)
        cluster_labels = asignar_clusters(linkage_matrix, n_clusters)
        dendrograma = generar_dendrograma(linkage_matrix, n_clusters)
        scatter = generar_scatter_plot(data, cluster_labels)
        estadisticas = obtener_estadisticas_por_cluster(df, cluster_labels)
        metricas = calcular_metricas_calidad(data, cluster_labels)
        dist_matrix = matriz_distancia_centroides(df, cluster_labels)

        return render_template("resultados.html",
            datos=df.to_html(classes="table table-bordered", index=False),
            dendrograma=dendrograma,
            scatter=scatter,
            estadisticas=estadisticas,
            metricas=metricas,
            dist_matrix=dist_matrix
        )

    except Exception as e:
        return f"Error en análisis simulado: {str(e)}"

@app.route('/conceptos')
def conceptos():
    return render_template("conceptos.html")

@app.route('/ayuda')
def ayuda():
    return render_template("ayuda.html")

if __name__ == '__main__':
    app.run(debug=True)
