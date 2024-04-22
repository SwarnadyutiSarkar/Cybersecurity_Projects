import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Generate sample data (normal and anomalous data points)
np.random.seed(42)
normal_data = np.random.normal(loc=0, scale=0.5, size=(100, 2))
anomalous_data = np.random.uniform(low=-3, high=3, size=(10, 2))

# Combine normal and anomalous data
data = np.vstack([normal_data, anomalous_data])

# Create an Isolation Forest model
clf = IsolationForest(contamination=0.05, random_state=42)

# Fit the model to the data
clf.fit(data)

# Predict anomalies (1 for normal data, -1 for anomalies)
predictions = clf.predict(data)

# Plot the data points and anomalies
plt.scatter(data[:, 0], data[:, 1], c=predictions, cmap='viridis')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Anomaly Detection using Isolation Forest')
plt.colorbar(label='Anomaly Score')
plt.show()
