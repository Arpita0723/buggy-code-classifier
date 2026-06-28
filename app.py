from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    code = request.form["code"]

    if code.strip() == "":
        return render_template(
            "index.html",
            prediction="Please enter some Python code.",
            confidence=""
        )

    # Convert input to TF-IDF features
    code_vector = vectorizer.transform([code])

    # Predict class
    prediction = model.predict(code_vector)[0]

    # Prediction probability
    probabilities = model.predict_proba(code_vector)[0]
    confidence = max(probabilities) * 100

    return render_template(
        "index.html",
        prediction=prediction.upper(),
        confidence=f"{confidence:.2f}%"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)