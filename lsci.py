from sklearn.datasets import load_iris
iris = load_iris()
print("Feature names:")
print(iris.feature_names)
print("\nFirst five records:")
print(iris.data[:5])