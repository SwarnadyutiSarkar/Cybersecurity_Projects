from sklearn.ensemble import IsolationForest

def train_ml_model():
    """Train ML model for anomaly detection."""
    # Replace with actual training data and feature extraction logic
    X_train = [[1], [2], [3], [5], [10], [20]]
    
    # Initialize and train Isolation Forest model
    model = IsolationForest(contamination=0.01)
    model.fit(X_train)
    
    return model

def detect_anomaly(model, data):
    """Detect anomaly using ML model."""
    return model.predict(data)

if __name__ == "__main__":
    # Train ML model
    model = train_ml_model()
    
    # Test anomaly detection
    data = [[4], [15], [25]]
    predictions = detect_anomaly(model, data)
    
    print(f"Anomaly predictions: {predictions}")
