import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Sample data
data = {
    'text': [
        'Your account has been suspended. Click here to reactivate.',
        'Congratulations! You have won a $1000 gift card.',
        'Your invoice is attached. Please review.',
        'Update your account information.',
        'Meeting at 10 AM tomorrow in Conference Room 1.'
    ],
    'label': [1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Feature extraction
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model and vectorizer
joblib.dump(model, 'phishing_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
