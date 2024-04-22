import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def threat_detection_with_ml(data_file):
    """Train and evaluate a threat detection model using ML."""
    try:
        # Load data
        data = pd.read_csv(data_file)
        
        # Prepare features and labels
        X = data.drop('label', axis=1)
        y = data['label']
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Initialize and train ML model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        print(f"Threat detection model accuracy: {accuracy}")
    except Exception as e:
        print(f"Error training and evaluating threat detection model: {e}")

if __name__ == "__main__":
    data_file = "threat_data.csv"  # Replace with the path to the threat data file
    threat_detection_with_ml(data_file)
