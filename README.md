# Phishing Website Detection using Machine Learning

## Project Overview

Phishing attacks are one of the most common cybersecurity threats where attackers create fake websites that imitate legitimate platforms to steal sensitive information such as passwords, credit card details, and personal data.

This project focuses on building a **machine learning model that can automatically detect phishing websites** based on various characteristics of URLs, domain information, and webpage behavior.

The model analyzes multiple features extracted from websites, such as URL structure, domain properties, security indicators, and webpage behavior, to determine whether a website is **legitimate or phishing**.

---

## Dataset Description

The dataset used in this project contains multiple features that describe different aspects of a website. These features include:

* URL-based features (URL length, presence of IP address, use of URL shortening services)
* Domain-based features (domain age, DNS records, domain registration length)
* Security features (SSL certificate status, HTTPS usage)
* Website behavior features (popups, iframes, redirection behavior)
* Website popularity indicators (web traffic, page rank, Google indexing)

Each record in the dataset represents a website and contains a **label indicating whether the website is legitimate or phishing**.

Most phishing datasets use values like:

1 → Legitimate
-1 → Phishing

And the Result column is the target label that tells whether the site is phishing.


---

# 🔬 Data Science Lifecycle

The machine learning workflow follows a modular pipeline architecture consisting of the following stages.

---

# 1️⃣ Data Ingestion

The pipeline begins with **data ingestion**, where data is fetched from **MongoDB**.

MongoDB is used as the primary data source because it allows flexible schema storage and efficient retrieval of large datasets.

Key steps:

- Connect to MongoDB database
- Retrieve dataset collections
- Convert documents into structured data format
- Export dataset into a DataFrame
- Store raw dataset in the artifact directory

This stage ensures that the pipeline always works with the **latest available dataset**.

---

# 2️⃣ Data Validation

The **data validation stage** ensures that the incoming dataset is reliable and suitable for training.

Validation checks include:

- Schema validation
- Missing value detection
- Data type verification
- Column consistency checks
- Dataset drift detection

A validation report is generated and stored in the artifacts folder.

This stage prevents **corrupted or inconsistent data from entering the training pipeline**.

---

# 3️⃣ Data Transformation

After validation, the dataset is processed in the **data transformation stage**.

This step prepares the data for machine learning by applying feature engineering techniques.

Transformation operations include:

- Handling missing values
- Feature encoding
- Feature scaling
- Feature selection
- Creating training and testing datasets

The processed dataset is then stored as an artifact and passed to the model training stage.

---

# 4️⃣ Model Training

In the **model training stage**, machine learning algorithms are trained using the transformed dataset.

This stage performs:

- Model selection
- Hyperparameter tuning
- Model training
- Model evaluation
- Model serialization

The trained model is saved as a serialized object (`.pkl`) in the artifacts directory.

---

# 📈 Experiment Tracking with DagsHub

To ensure reproducibility and experiment management, the project uses **DagsHub** for tracking machine learning experiments.

Experiment tracking includes:

- Model parameters
- Training metrics
- Dataset versions
- Model artifacts
- Experiment history

Each training run is logged to DagsHub, allowing comparison between different model versions.

Benefits of using DagsHub:

- Experiment reproducibility
- Centralized experiment tracking
- Integration with MLflow
- Version control for machine learning experiments

---

# 🧠 Machine Learning Pipeline Architecture

MongoDB Database
│
▼
Data Ingestion
│
▼
Data Validation
│
▼
Data Transformation
│
▼
Model Training
│
▼
Experiment Tracking (DagsHub)
│
▼
Artifacts Stored in Amazon S3

# 📊 Machine Learning Pipeline & Artifact Management

This project implements a complete **end-to-end machine learning pipeline** following the standard **Data Science Lifecycle**.  
The pipeline is designed to automate the process of data ingestion, validation, transformation, model training, and experiment tracking.

All artifacts generated during the pipeline execution are stored in **Amazon S3**, ensuring persistence, scalability, and accessibility across different environments.

---

# ☁️ Artifact Storage using Amazon S3

All intermediate and final outputs generated during the pipeline execution are stored in **Amazon S3**.

Artifacts stored include:

- Raw datasets
- Processed datasets
- Trained models
- Feature engineering outputs
- Validation reports
- Model evaluation metrics

Using **Amazon S3** provides the following advantages:

- Centralized artifact storage
- High durability and availability
- Easy integration with machine learning pipelines
- Version control for model artifacts

Example artifact structure stored in S3:
artifacts/
│
├── data_ingestion/
│ └── dataset.csv
│
├── data_validation/
│ └── validation_report.yaml
│
├── data_transformation/
│ └── transformed_data.csv
│
├── model_trainer/
│ └── trained_model.pkl


---

# 📦 Artifact Storage Flow
Pipeline Execution
│
▼
Generate Artifacts
│
▼
Upload to Amazon S3
│
▼
Artifacts Accessible for
Model Serving & Future Training

# 🚀 CI/CD Pipeline for Network Security ML API

This project implements a **fully automated CI/CD pipeline** that builds, packages, and deploys the machine learning API using containerization and cloud infrastructure.

The pipeline is implemented using **GitHub Actions**, containerized with **Docker**, stored in **Amazon Elastic Container Registry (ECR)**, and deployed on **Amazon EC2**.

The system ensures that **every code push automatically triggers build and deployment**, allowing continuous updates to the ML API without manual intervention.

---

# ⚙️ CI/CD Workflow Overview

The CI/CD pipeline is triggered whenever code is pushed to the `main` branch.

The workflow consists of three main stages:

1. Continuous Integration (CI)
2. Continuous Delivery (Build & Push Docker Image)
3. Continuous Deployment

---

# 🔹 Continuous Integration (CI)

The CI stage validates the code before deployment.

Steps performed:

- Checkout the repository
- Perform lint checks
- Execute unit tests

This stage ensures that only **verified and tested code** proceeds to the build stage.

---

# 🔹 Continuous Delivery (Build & Push Docker Image)

In this stage, the application is containerized and stored in a cloud container registry.

Steps performed:

1. Authenticate with AWS using GitHub Secrets.
2. Login to Amazon ECR.
3. Build a Docker image using the project’s Dockerfile.
4. Tag the image with the repository URI.
5. Push the image to Amazon ECR.

Example image format:
<aws-account-id>.dkr.ecr.<region>.amazonaws.com/networksecurityrepo:latest

This step ensures the application environment is **fully reproducible and version controlled**.

---

# 🔹 Continuous Deployment

The deployment stage automatically updates the running application on the EC2 server.

This job runs on a **self-hosted GitHub runner configured on the EC2 instance**.

Steps performed:

1. Authenticate with AWS.
2. Login to Amazon ECR.
3. Pull the latest Docker image.
4. Stop the currently running container.
5. Remove the old container.
6. Run a new container with the updated image.
7. Clean unused Docker resources.

The container exposes the API on port **8080**, making the service accessible via the EC2 public IP.

Example:
http://<EC2_PUBLIC_IP>:8080/docs

---

# 🏗️ CI/CD Architecture
Developer Push Code
│
▼
GitHub Repository
│
▼
GitHub Actions (CI Pipeline)
│
▼
Docker Image Build
│
▼
Push Image → Amazon ECR
│
▼
EC2 Self-Hosted Runner
│
▼
Pull Latest Docker Image
│
▼
Stop Old Container
│
▼
Run Updated Container
│
▼
FastAPI ML API Live

---

# 🔐 Required GitHub Secrets

The following secrets must be configured in the repository:

| Secret Name | Description |
|-------------|-------------|
| AWS_ACCESS_KEY_ID | AWS access key |
| AWS_SECRET_ACCESS_KEY | AWS secret key |
| AWS_REGION | AWS region |
| AWS_ECR_LOGIN_URI | ECR registry URI |
| ECR_REPOSITORY_NAME | ECR repository name |

These secrets allow GitHub Actions to securely authenticate with AWS services.

---

# 🐳 Docker Deployment

The application is packaged as a Docker container to ensure consistency across environments.

Key benefits:

- Environment reproducibility
- Simplified deployment
- Dependency isolation
- Scalable architecture

---

# 🌐 API Access

Once deployed, the FastAPI documentation can be accessed at:
http://<EC2_PUBLIC_IP>:8080/docs

This interface allows users to:

- Trigger model training
- Upload CSV files for prediction
- Download prediction results


---

# 🚀 Key Features

- End-to-end machine learning pipeline
- Modular pipeline architecture
- Artifact storage using Amazon S3
- Data ingestion using MongoDB
- Automated data validation and transformation
- Model training and evaluation
- Experiment tracking with DagsHub
- CI/CD enabled deployment pipeline

---

# 📌 Summary

This system integrates **cloud storage, automated pipelines, and experiment tracking** to create a robust and scalable machine learning workflow.

The architecture ensures:

- Reproducible experiments
- Scalable artifact storage
- Automated model training
- Seamless integration with CI/CD pipelines
