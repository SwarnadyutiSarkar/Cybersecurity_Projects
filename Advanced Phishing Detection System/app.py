from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load('phishing_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    features = vectorizer.transform([text])
    prediction = model.predict(features)[0]
    
    return jsonify({'phishing': bool(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
