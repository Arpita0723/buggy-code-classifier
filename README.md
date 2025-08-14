Buggy Code Classifier
This project is a machine learning-based classifier that detects buggy vs. clean Python code snippets using TF-IDF vectorization and Logistic Regression.

Features
Automatically detects common Python bugs (missing colons, bad indentation, etc.)

Classifies code as:

1 → Buggy

0 → Clean

Built using scikit-learn, pandas, and joblib

Interactive input for real-time predictions


Project Files

buggy_code_classifier/
│
├── prepare_dataset.py  
├── train_model.py        
├── predict.py            
├── dataset.csv          
├── model.pkl             
├── vectorizer.pkl         
└── README.md            


How It Works
prepare_dataset.py: 
      Generates labeled code snippets (buggy or clean)
      Saves them to dataset.csv

train_model.py:
      Vectorizes code snippets using TF-IDF
      Trains a Logistic Regression classifier
      Saves the trained model and vectorizer

predict.py:
      Accepts user input (Python code)
      Vectorizes it using the saved vectorizer
      Uses the model to predict if the code is buggy or clean



How to Run

1. Install dependencies:
pip install pandas scikit-learn joblib
2. Prepare the dataset:
python prepare_dataset.py
3. Train the model:
python train_model.py
4. Predict a code snippet:
python predict.py


Sample Input & Output
Input (Buggy Code):
for i in range(5)
    print(i)
Output:
The code is predicted to be BUGGY.


Created by
Arpita Singh

Project: Code Quality Classification

