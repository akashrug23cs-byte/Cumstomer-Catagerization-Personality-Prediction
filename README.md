# CustomCategorized
Predict customer personality types using machine learning based on demographic and transaction data. Built with a full ML pipeline including clustering and classification.
# 🧠 Customer Personality Prediction

This data science project aims to build a machine learning system that predicts customer personality categories based on demographic and purchase behavior data. The system uses clustering and classification techniques to group customers and then classify new ones based on their attributes.

---

## 📌 Problem Statement

Businesses like malls, stores, and product-based companies often deal with diverse customers. Understanding customer segments helps in targeted marketing and improved customer service.

This project clusters customers based on their personal and transactional data and then builds a classification model to predict the cluster (personality category) of new customers.

---

## 📊 Dataset

- Contains features such as:
  - Demographic data (Age, Gender, Income, etc.)
  - Purchase behavior (Amount spent, Purchase frequency, etc.)

---

## ⚙️ Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn (for ML algorithms like KMeans & Random Forest)
- Matplotlib, Seaborn (for visualization)
- Pickle (for model serialization)

---

## 🔍 ML Pipeline

1. **Data Preprocessing**  
   Cleaning, encoding, and scaling features.

2. **Clustering (Unsupervised)**  
   KMeans is used to cluster customers into different personality segments.

3. **Classification (Supervised)**  
   Random Forest Classifier predicts the customer segment using labeled clusters.

4. **Model Saving & Deployment Ready**  
   Models are serialized using Pickle for future inference.

---

## 📈 Evaluation

- Clustering evaluated using Silhouette Score
- Classification evaluated using Accuracy, Confusion Matrix, and F1 Score

---


##flask ,html,css

