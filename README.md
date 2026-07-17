# Insure AI Enterprise Ecosystem Dashboard

A premium, unified single-page application (SPA) managing four distinct AI and rule-based subsystems for insurance analysis, predictive forecasting, anomaly detection, and automated decision orchestration.

---

## 📊 Architecture & Subsystems

The ecosystem runs on a **FastAPI backend grid** serving four modules on local loopback ports, connected to a glassmorphic **Main Hub SPA** frontend:

### 1. Customer Retention (Port 8000)
*   **Database**: PostgreSQL
*   **Engine**: XGBoost Machine Learning Classifier
*   **Features**: Propensity scoring, customer churn predictions, SHAP feature importance overlays, paginated directories (All Leads, All Customers), and real-time training progress logs.

### 2. Anomaly Detection (Port 8001)
*   **Database**: SQLite (`anomaly.db`)
*   **Engine**: Isolation Forest Classifier
*   **Features**: Automatically scores and flags anomalies, highlights claims outliers, and identifies potentially fraudulent profiles.

### 3. Predictive Intelligence (Port 8002)
*   **Database**: SQLite (`predictive.db`)
*   **Engine**: FB Prophet Time-Series Regression
*   **Features**: Analyzes historical agent-customer interaction call logs to forecast future daily conversions over a 30-day horizon, visualizing trends on an interactive line chart.

### 4. Decision Engine (Port 8003)
*   **Database**: SQLite (`decision.db`)
*   **Engine**: Rule-Based Action Compiler
*   **Features**: Synthesizes customer risks and metrics to generate automated contact recommendations and custom script dialogue advice for insurance agents.

---

## 🚀 Getting Started

### Prerequisites
*   Python 3.10+
*   PostgreSQL running locally (for Customer Retention)

### 1. Start the Subsystem Backends
For each of the four subsystem folders (`1_Customer_Retention`, `2_Anomaly_Detection`, `3_Predictive_Intelligence`, `4_Decision_Making`):
1.  Navigate into the folder.
2.  Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
3.  Start the FastAPI server on its designated port:
    *   **Retention**: `uvicorn app.main:app --port 8000 --reload`
    *   **Anomaly**: `uvicorn app.main:app --port 8001 --reload`
    *   **Predictive**: `uvicorn app.main:app --port 8002 --reload`
    *   **Decision**: `uvicorn app.main:app --port 8003 --reload`

### 2. Launch the Frontend
Navigate to the `Main_Hub` directory:
```bash
cd Main_Hub
python3 -m http.server 8080
```
Open **[http://127.0.0.1:8080/index.html](http://127.0.0.1:8080/index.html)** in Google Chrome.

---

## 🧪 Testing with Kaggle Datasets

The repository includes pre-downloaded, cleaned Kaggle datasets in the root directory for immediate bulk testing:

*   **`kaggle_telco_churn.csv`** (7,045 records): Perfect for testing **Customer Retention [Port 8000]**.
*   **`churn_modelling.csv`** (10,000 records): Perfect for testing **Anomaly Detection [Port 8001]**.
*   **`bank_churn.csv`** (11,162 records): Perfect for testing **Predictive Intelligence [Port 8002]** or **Decision Engine [Port 8003]**.

### Recommended Testing Loop:
1.  Go to **Ecosystem Data Center** tab.
2.  Choose your target subsystem, upload one of the corresponding CSV files, and click **Upload Dataset**.
3.  Go back to the Hub landing page—the counts on the cards will update **instantly**.
4.  Open the **Ecosystem Retrain Console**, select the target port, and click **Retrain Model**.
5.  Open the subsystem's tab to review the updated predictions, charts, and dialogues.
