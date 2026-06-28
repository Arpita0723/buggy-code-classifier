import joblib

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

print("=" * 60)
print("      Buggy Code Classifier")
print("=" * 60)

print("\nEnter your Python code.")
print("Press Enter twice to finish.\n")

lines = []

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

code = "\n".join(lines)

if not code.strip():
    print("\nNo code entered!")
    exit()

# Transform
code_vector = vectorizer.transform([code])

# Predict
prediction = model.predict(code_vector)[0]

# Confidence
probabilities = model.predict_proba(code_vector)[0]

classes = model.classes_

confidence = max(probabilities) * 100

print("\n" + "=" * 60)
print("Prediction :", prediction.upper())
print(f"Confidence : {confidence:.2f}%")
print("=" * 60)