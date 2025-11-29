import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score

# 0. Setup: Create a dummy .csv file for the demonstration
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
pd.DataFrame(X).to_csv("data.csv", index=False)

# 1. Load Data
data = pd.read_csv("data.csv")

# 2. Run Algorithms
# K-Means: Hard clustering (assigns point to nearest centroid)
km_labels = KMeans(n_clusters=4).fit_predict(data)

# EM (Gaussian Mixture): Soft clustering (probabilistic assignment)
em_labels = GaussianMixture(n_components=4).fit_predict(data)

# 3. Compare Quality (Silhouette Score: closer to 1 is better)
print(f"K-Means Score: {silhouette_score(data, km_labels):.3f}")
print(f"EM (GMM) Score: {silhouette_score(data, em_labels):.3f}")

# 4. Conclusion
diff = silhouette_score(data, em_labels) - silhouette_score(data, km_labels)
print(f"Result: {'EM' if diff > 0 else 'K-Means'} performed better by {abs(diff):.3f}")