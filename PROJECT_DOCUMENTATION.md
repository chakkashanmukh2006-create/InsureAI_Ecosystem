# Insure AI Enterprise Ecosystem - Technical Project Documentation

This document contains four structured technical notes detailing the architecture, ML algorithms, database configurations, python dependencies, and data flows of each subsystem in the Insure AI Ecosystem.

---

## 📝 Note 1: Customer Retention Subsystem (Port 8000)

### 1. Structural Design & Goal
The Customer Retention module is designed to predict **Lead Conversion Propensities** (which leads are likely to purchase an insurance policy) and **Customer Churn Risks** (which existing clients are at risk of leaving). It provides agents with actionable propensity percentages and feature importance insights.

### 2. Machine Learning Algorithm
*   **Core Classifier**: **XGBoost (Extreme Gradient Boosting)**. Chosen for its superior accuracy, speed, and capability to handle structured tabular demographic data.
*   **Explainability Model**: **SHAP (SHapley Additive exPlanations)**. Calculates feature contributions to explain why a customer was flagged as high-risk (e.g., how age or income impacted their score).

### 3. Core Python Libraries
*   `fastapi` & `uvicorn` (REST API layer)
*   `xgboost` (gradient booster model)
*   `shap` (game-theoretic model explainability)
*   `pandas` & `numpy` (data wrangling and array manipulation)
*   `scikit-learn` (pre-processing, data splitting, scaling)
*   `sqlalchemy` (SQL Object Relational Mapping)
*   `psycopg2-binary` (native PostgreSQL driver)

### 4. Database Schema (PostgreSQL)
*   **`leads`**: Stores client attributes (age, income, visits, conversion target).
*   **`customers`**: Stores profile attributes (policy type, premium amount, complaints, churn target).
*   **`lead_predictions` / `customer_predictions`**: Stores computed churn risk and propensity scores.
*   **`training_history`**: Logs active model versions and training parameters.

### 5. Ingestion & Execution Flow
1.  **Ingestion**: CSV datasets are uploaded via POST `/upload/leads` or `/upload/customers`. The backend normalizes headers and writes records.
2.  **Retraining**: Executing POST `/train` loads active database rows, pre-processes features, trains XGBoost, saves serialized models (`.joblib`), and updates the local model registry.
3.  **Result Retrieval**: `/leads/predicted/all` serves scored propensity lists.

---

## 📝 Note 2: Anomaly Detection Subsystem (Port 8001)

### 1. Structural Design & Goal
The Anomaly Detection module serves to safeguard the insurance portfolio by automatically auditing leads and customer accounts to flag potential fraud, claims exaggeration, or statistical outliers.

### 2. Machine Learning Algorithm
*   **Core Classifier**: **Isolation Forest**. An unsupervised learning algorithm that isolates anomalies by randomly partitioning features. Outliers are isolated much faster (closer to the root of the tree) than normal data points.
*   **Scoring**: Generates an anomaly index score from `0.0` (normal) to `1.0` (highly anomalous).

### 3. Core Python Libraries
*   `fastapi` & `uvicorn` (REST API layer)
*   `scikit-learn` (specifically `sklearn.ensemble.IsolationForest`)
*   `pandas` & `numpy` (data parsing)
*   `sqlalchemy` (database orchestration)

### 4. Database Schema (SQLite: `anomaly.db`)
*   **`leads` / `customers`**: Stores demographic attributes.
*   **`lead_predictions` / `customer_predictions`**: Holds computed anomaly scores and specific reasons for the outlier designation (e.g., abnormal income-to-premium ratio).

### 5. Ingestion & Execution Flow
1.  **Ingestion**: Claims or transaction data are uploaded.
2.  **Retraining**: Isolation Forest is trained on current database rows, calculating contamination factors and isolating outliers.
3.  **Result Retrieval**: Scored outputs are sorted by anomaly scores descending, making the highest-risk claims visible at the top.

---

## 📝 Note 3: Predictive Intelligence Subsystem (Port 8002)

### 1. Structural Design & Goal
This subsystem is dedicated to forecasting long-term operational metrics, specifically projecting the total volume of customer conversions over the next 30 days based on historical call center performance.

### 2. Machine Learning Algorithm
*   **Forecasting Engine**: **Facebook Prophet**. An additive regression model designed for time-series forecasting. It handles seasonality (daily, weekly, yearly) and holiday shifts natively.
*   **Fallback Classifier**: **Linear Regression** (from `scikit-learn`) is used if Prophet is missing.

### 3. Core Python Libraries
*   `fastapi` & `uvicorn` (REST API layer)
*   `prophet` (time-series forecasting engine)
*   `scikit-learn` (mathematical fallbacks)
*   `joblib` (saving/loading models)
*   `pandas` & `numpy` (aggregating logs by date)

### 4. Database Schema (SQLite: `predictive.db`)
*   **`call_logs`**: Stores agent call details: `agent_id`, `call_duration`, `outcome` (conversion/rejected), and `call_date`.
*   **`model_registry`**: Registers active time-series models.

### 5. Ingestion & Execution Flow
1.  **Ingestion**: Call center phone records are logged.
2.  **Retraining**: Prophet aggregates raw call logs by date to compute daily conversion counts. It fits a trend curve and projects conversion counts for the next 30 days.
3.  **Result Retrieval**: `/predictions/forecast?days=30` returns a coordinate list of historical and projected timelines rendered on a line chart.

---

## 📝 Note 4: Decision Engine Subsystem (Port 8003)

### 1. Structural Design & Goal
The Decision Engine acts as the business rules compiler. It automatically translates risk assessments, propensity scores, and profile attributes into custom dialogue advice for customer support agents.

### 2. Decision Logic
*   **Core Compiler**: **Rule-Based Translation Engine**. Evaluates scoring indicators (e.g., churn probability > 70%) to compile script categories:
    *   *High Churn Risk* ➡️ *"CRITICAL: Call immediately and offer 10% discount"*
    *   *High Propensity* ➡️ *"Promotion: Recommend premium plan"*
    *   *Normal* ➡️ *"Standard check-in follow-up"*

### 3. Core Python Libraries
*   `fastapi` & `uvicorn` (API routers)
*   `pandas` & `numpy` (rules evaluation)
*   `sqlalchemy` (database interactions)

### 4. Database Schema (SQLite: `decision.db`)
*   **`leads` / `customers`**: Stores profile records.
*   **`lead_predictions` / `customer_predictions`**: Holds risk scoring flags and compiled dialog script advice.

### 5. Ingestion & Execution Flow
1.  **Ingestion**: Customer profiles are bulk-ingested.
2.  **Retraining**: Re-compiles classifications using decision matrices.
3.  **Result Retrieval**: The directories list dialogue advice alongside names, scores, and contact info, giving agents a direct action list.
