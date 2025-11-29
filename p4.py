from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# 1. Load Data & Split (70% Train, 30% Test)
iris = load_iris()
X_tr, X_te, y_tr, y_te = train_test_split(iris.data, iris.target, test_size=0.3)

# 2. Initialize & Train (K=3) in one line
knn = KNeighborsClassifier(n_neighbors=3).fit(X_tr, y_tr)

# 3. Predict & Print Results
print(f"{'PRED':<5} | {'ACTUAL':<6} | STATUS")
print("-" * 25)
for p, a in zip(knn.predict(X_te), y_te):
    print(f"{p:<5} | {a:<6} | {'✅ Correct' if p == a else '❌ Wrong'}")