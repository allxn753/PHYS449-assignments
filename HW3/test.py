import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
import numpy as np

# Assuming X contains features and y contains labels
# X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

k_values = range(1, 21, 2)  # Test odd k values from 1 to 19
validation_accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k, metric='hamming')
    
    # Using cross-validation for more robust evaluation
    scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy') 
    validation_accuracies.append(np.mean(scores))

# Plotting k vs validation accuracy
plt.figure(figsize=(10, 6))
plt.plot(k_values, validation_accuracies, marker='o')
plt.title('KNN Classifier: k vs Validation Accuracy (Hamming Distance)')
plt.xlabel('Number of Neighbors (k)')
plt.ylabel('Validation Accuracy')
plt.grid(True)
plt.xticks(k_values)
plt.show()

# Find optimal k
optimal_k_index = np.argmax(validation_accuracies)
optimal_k = k_values[optimal_k_index]
print(f"Optimal k: {optimal_k}")