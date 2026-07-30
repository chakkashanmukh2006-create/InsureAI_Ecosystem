#!/bin/bash

echo "Starting Insure AI Ecosystem Backend Services..."

# Start Port 8000 (Customer Retention & Sentiment)
cd /app/1_Customer_Retention
uvicorn app.main:app --host 0.0.0.0 --port 8000 &
PID1=$!

# Start Port 8001 (Anomaly Detection)
cd /app/2_Anomaly_Detection
uvicorn app.main:app --host 0.0.0.0 --port 8001 &
PID2=$!

# Start Port 8002 (Predictive Intelligence)
cd /app/3_Predictive_Intelligence
uvicorn app.main:app --host 0.0.0.0 --port 8002 &
PID3=$!

# Start Port 8003 (Decision Making)
cd /app/4_Decision_Making
uvicorn app.main:app --host 0.0.0.0 --port 8003 &
PID4=$!

echo "All services successfully initialized."
echo "Listening on ports: 8000, 8001, 8002, 8003"

# Wait for all background processes to keep container alive
wait $PID1 $PID2 $PID3 $PID4
