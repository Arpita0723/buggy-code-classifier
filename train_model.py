import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
# Load dataset
df = pd.read_csv("dataset.csv")

print("Dataset Loaded Successfully")
print("Total Samples:", len(df))

# Features and labels
X = df["code"]
y = df["label"]

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
# TF-IDF vectorization
vectorizer = TfidfVectorizer(
    lowercase=False,
    ngram_range=(1, 2),
    max_features=10000,
    token_pattern=r"\S+"
)
# Train model
model = LogisticRegression(
    max_iter=1000,
    random_state=42
)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model.fit(X_train_tfidf, y_train)

# Evaluate
y_pred = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nClassification Report")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))


scores = cross_val_score(
    model,
    vectorizer.fit_transform(X),
    y,
    cv=5
)

print("\nCross Validation Accuracy:", scores.mean())


# Save model and vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nModel Saved Successfully")
