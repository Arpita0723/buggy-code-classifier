import joblib

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

print("Enter your code snippet (press Enter twice to finish):")

# Multiline input
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

user_code = "\n".join(lines)

# Transform and predict
X_input = vectorizer.transform([user_code])
prediction = model.predict(X_input)[0]

if prediction == 1:
    print("\n🚫 The code is predicted to be BUGGY.")
else:
    print("\n✅ The code is predicted to be CLEAN.")
