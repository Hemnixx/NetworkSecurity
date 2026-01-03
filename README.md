🔐 Network Security – Phishing Website Detection (End-to-End MLOps)

An end-to-end MLOps-based Network Security project focused on detecting phishing / malicious websites using machine learning, automation pipelines, and deployment-ready architecture.

This project covers the complete lifecycle of an ML system — from data ingestion to model training, validation, transformation, prediction, and API-based deployment.

🚀 Project Overview

Phishing websites pose a serious threat to users by stealing sensitive information such as login credentials and financial data.
This project aims to automatically classify websites as phishing or legitimate using network-level and URL-based features.

The system is designed using MLOps principles, ensuring:

Reproducibility

Automation

Scalability

Production readiness

🧠 Key Features

✅ End-to-End MLOps Pipeline

✅ Automated Data Ingestion from MongoDB

✅ Data Validation & Drift Detection

✅ Feature Transformation & Preprocessing

✅ Model Training & Evaluation

✅ REST API for Real-time Predictions

✅ CI/CD-ready architecture

✅ Modular, scalable, and production-grade codebase

NetworkSecurity/
│
├── networksecurity/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   └── training_pipeline.py
│   │
│   ├── entity/
│   │   ├── config_entity.py
│   │   └── artifact_entity.py
│   │
│   ├── constant/
│   │   └── training_pipeline.py
│   │
│   ├── utils/
│   │   └── main_utils/
│   │
│   └── exception/
│
├── app.py              # FastAPI application
├── main.py             # Pipeline trigger
├── templates/          # HTML templates
├── data_schema/
│   └── schema.yaml
├── artifact/           # Generated artifacts
├── final_model/        # Saved models
├── requirements.txt
└── README.md


🔄 ML Pipeline Stages
1️⃣ Data Ingestion

Data is fetched from MongoDB Atlas

Stored in a feature store

Split into training & testing datasets

2️⃣ Data Validation

Schema validation using schema.yaml

Column consistency checks

Data drift detection using KS-test

Drift reports stored as YAML

3️⃣ Data Transformation

Missing value handling using KNN Imputer

Feature-target separation

Transformed datasets saved as NumPy arrays

4️⃣ Model Training

Machine learning model trained on transformed data

Performance validation against expected threshold

Trained model saved as an artifact

🌐 Deployment & API

The project uses FastAPI to expose endpoints:

🔹 Train the Model
GET /train


Triggers the full training pipeline.

🔹 Predict Phishing Websites
POST /predict


Upload a CSV file containing website features

Returns predictions (phishing / legitimate)

Output displayed in tabular format

📊 Input Features

The model uses network and URL-based features such as:

URL length

Presence of IP address

SSL certificate status

Domain age

Redirection behavior

DNS records

Web traffic

Page rank

and more…

📈 Output

Prediction:

1 → Legitimate Website

-1 → Phishing Website

Output is saved as:

prediction_output/output.csv

🛠️ Tech Stack

Programming: Python

ML & Data: Scikit-learn, NumPy, Pandas

Database: MongoDB Atlas

Backend: FastAPI

MLOps: Modular pipelines, artifact tracking

Version Control: Git & GitHub

Deployment Ready: CI/CD compatible architecture

📌 How to Run Locally
1️⃣ Clone Repository
git clone https://github.com/Hemnixx/NetworkSecurity.git
cd NetworkSecurity

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Training Pipeline
python main.py

5️⃣ Start FastAPI Server
python app.py


Visit:

http://localhost:8000/docs

🎯 Use Case

Detect phishing websites

Cybersecurity research

Network traffic analysis

Educational MLOps project

Resume-ready industry project

📚 Future Enhancements

Model monitoring & alerting

Cloud deployment (AWS / GCP)

Real-time streaming predictions

UI dashboard

Advanced ensemble models

👤 Author

Neeraj Kumar Gupta
B.Tech – Electronics & Communication Engineering
NIT Kurukshetra

🔗 GitHub: https://github.com/Hemnixx

🔗 LinkedIn: https://linkedin.com/in/neeraj-gupta-554b33291

⭐ Final Note

This project demonstrates practical MLOps skills, real-world network security application, and production-ready ML system design — making it suitable for IT, ML, and Data roles.
