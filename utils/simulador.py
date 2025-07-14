from sklearn.datasets import make_blobs
import pandas as pd

def simular_datos(n_samples=100, n_features=2, n_centers=3):
    X, y = make_blobs(n_samples=n_samples, centers=n_centers, n_features=n_features, random_state=42)
    columns = [f'Feature_{i+1}' for i in range(n_features)]
    return pd.DataFrame(X, columns=columns)
