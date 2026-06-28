# 🐞 Buggy Code Classifier

A Machine Learning-based web application that classifies Python code snippets as **Buggy** or **Clean** using **TF-IDF Vectorization** and **Logistic Regression**. The project also provides a simple Flask web interface for real-time predictions.

---

## 📌 Features

- 🧠 Machine Learning-based Bug Classification
- 📝 Automatically Generated Python Code Dataset
- ⚖️ Balanced Dataset (Clean & Buggy Code)
- 🔍 TF-IDF Feature Extraction
- 🤖 Logistic Regression Classifier
- 🌐 Flask Web Interface
- 💾 Model Serialization using Joblib
- ⚡ Real-Time Prediction with Confidence Score

---

## 🛠️ Tech Stack

- Python
- Scikit-learn
- Pandas
- Flask
- Joblib

---

## 📂 Project Structure

```text
buggy_code_classifier/
│
├── prepare_dataset.py      # Generates synthetic dataset
├── train_model.py          # Trains the ML model
├── predict.py              # Command-line prediction
├── app.py                  # Flask web application
│
├── dataset.csv
├── model.pkl
├── vectorizer.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── screenshots/
│   ├── homepage.png
│   ├── clean_prediction.png
│   ├── buggy_prediction.png
│   └── training_results.png
│
└── README.md
```

---

## 📊 Dataset

- **Total Samples:** 5000
- **Classes:** Clean, Buggy
- Synthetic Python code snippets generated with multiple realistic bug patterns.

---

## 🤖 Machine Learning Pipeline

```
Dataset
      │
      ▼
TF-IDF Vectorizer
      │
      ▼
Logistic Regression
      │
      ▼
Prediction
```

---

## 📈 Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | **96.8%** |
| Cross Validation Accuracy | **96.66%** |

---


## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Arpita0723/buggy-code-classifier.git
```

Move into the project directory

```bash
cd buggy-code-classifier
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open your browser and visit

```text
http://127.0.0.1:5000
```

---

## 💻 Example Prediction

### Input

```python
for i in range(5)
    print(i)
```

### Output

```
Prediction : BUGGY
Confidence : 95.66%
```

---

## 🔮 Future Improvements

- Support multiple programming languages.
- Improve dataset with additional real-world bug patterns.
- Compare multiple ML models (e.g., SVM, Random Forest).
- Integrate transformer-based models such as CodeBERT.
- Develop a VS Code extension for live bug detection.

---

## 👩‍💻 Author

**Arpita Singh**

B.Tech, Computer Science and Engineering  
Indian Institute of Technology (BHU), Varanasi

GitHub: https://github.com/Arpita0723