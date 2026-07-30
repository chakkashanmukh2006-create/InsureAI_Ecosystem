
'use client';
import Script from 'next/script';
import { useEffect } from 'react';

export default function Home() {
  return (
    <>
      {/* The original Vanilla JS logic */}
      <Script src="/app.js" strategy="lazyOnload" />
      
    <div id="app">
        {/* Main Content Area */}
        <main className="content-area">
            
            {/* VIEW 1: OVERVIEW LANDING HUB (No sidebar, Big 4 Cards Centered) */}
            <div id="overview-tab" className="tab-pane active" style={{"alignItems": "center", "justifyContent": "center", "width": "100%"}}>
                <header className="hub-header">
                    <i className="ph-fill ph-shield-check hub-logo"></i>
                    <h1>INSURE AI</h1>
                    <p className="subtitle">Enterprise Ecosystem Master Hub</p>
                    
                    <div className="search-container glass-panel" style={{"marginTop": "1.5rem", "width": "100%", "maxWidth": "550px", "position": "relative", "padding": "15px", "display": "flex", "flexDirection": "column", "gap": "10px", "border": "1px solid rgba(100, 181, 246, 0.3)", "background": "rgba(10, 15, 30, 0.6)", "boxShadow": "0 4px 15px rgba(0,0,0,0.2)"}}>
                        <div style={{"display": "flex", "alignItems": "center", "gap": "8px", "color": "var(--accent-predictive)", "fontWeight": "bold", "fontSize": "1.1rem"}}>
                            <i className="ph-fill ph-user-circle"></i> Customer 360 Engine
                        </div>
                        <div style={{"position": "relative", "width": "100%"}}>
                            <i className="ph ph-magnifying-glass" style={{"position": "absolute", "left": "15px", "top": "50%", "transform": "translateY(-50%)", "color": "var(--text-secondary)", "fontSize": "1.2rem"}}></i>
                            <input type="text" id="customer-360-search" placeholder="Enter Customer ID or Name to unlock 360 profile..." style={{"width": "100%", "padding": "12px 12px 12px 45px", "borderRadius": "6px", "background": "rgba(0,0,0,0.3)", "border": "1px solid rgba(255,255,255,0.1)", "color": "#fff", "fontSize": "1rem", "transition": "all 0.2s ease"}} />
                            <div id="search-results-dropdown" style={{"display": "none", "position": "absolute", "top": "100%", "left": "0", "width": "100%", "background": "#1a1c29", "border": "1px solid var(--accent-predictive)", "borderRadius": "6px", "marginTop": "5px", "zIndex": "100", "maxHeight": "250px", "overflowY": "auto", "boxShadow": "0 10px 25px rgba(0,0,0,0.5)"}}>
                                {/* Populated via JS */}
                            </div>
                        </div>
                    </div>
                </header>
                
                {/* System Health & Status Strip */}
                <div className="system-status-strip">
                    <div id="status-retention" className="status-badge offline">
                        <span className="status-dot" style={{"color": "var(--accent-retention)"}}></span>
                        <span>Retention [8000]</span>
                    </div>
                    <div id="status-anomaly" className="status-badge offline">
                        <span className="status-dot" style={{"color": "var(--accent-anomaly)"}}></span>
                        <span>Anomaly [8001]</span>
                    </div>
                    <div id="status-predictive" className="status-badge offline">
                        <span className="status-dot" style={{"color": "var(--accent-predictive)"}}></span>
                        <span>Predictive [8002]</span>
                    </div>
                    <div id="status-decision" className="status-badge offline">
                        <span className="status-dot" style={{"color": "var(--accent-decision)"}}></span>
                        <span>Decision [8003]</span>
                    </div>
                </div>

                {/* Big 4 Core Options Grid */}
                <div className="hub-grid">
                    {/* Option 1: Customer Retention */}
                    <div className="hub-card retention clickable-hub-card" data-target="retention-tab">
                        <span className="hub-card-port">Port 8000</span>
                        <div className="hub-card-icon"><i className="ph-fill ph-users-three"></i></div>
                        <h2>Customer Retention</h2>
                        <p>XGBoost ML classification predicting conversions and churn risks with SHAP values.</p>
                        <div className="hub-card-counts">
                            <div>Leads: <strong id="metric-retention-leads">--</strong></div>
                            <div>Customers: <strong id="metric-retention-cust">--</strong></div>
                        </div>
                    </div>

                    {/* Option 2: Anomaly Detection */}
                    <div className="hub-card anomaly clickable-hub-card" data-target="anomaly-tab">
                        <span className="hub-card-port">Port 8001</span>
                        <div className="hub-card-icon"><i className="ph-fill ph-shield-warning"></i></div>
                        <h2>Anomaly Detection</h2>
                        <p>Isolation Forest engine scanning records to identify fraud and outliers.</p>
                        <div className="hub-card-counts">
                            <div>Leads Analyzed: <strong id="metric-anomaly-leads">--</strong></div>
                            <div>Anomalies: <strong id="metric-anomaly-fraud">--</strong></div>
                        </div>
                    </div>

                    {/* Option 3: Predictive AI */}
                    <div className="hub-card predictive clickable-hub-card" data-target="predictive-tab">
                        <span className="hub-card-port">Port 8002</span>
                        <div className="hub-card-icon"><i className="ph-fill ph-chart-line-up"></i></div>
                        <h2>Predictive Intelligence</h2>
                        <p>Facebook Prophet time-series algorithm forecasting overall conversion trends.</p>
                        <div className="hub-card-counts" style={{"flexWrap": "wrap", "gap": "8px"}}>
                            <div>Call Logs: <strong id="metric-predictive-calls">--</strong></div>
                            <div>Leads: <strong id="metric-predictive-leads">--</strong></div>
                            <div>Customers: <strong id="metric-predictive-cust">--</strong></div>
                        </div>
                    </div>

                    {/* Option 4: Decision Engine */}
                    <div className="hub-card decision clickable-hub-card" data-target="decision-tab">
                        <span className="hub-card-port">Port 8003</span>
                        <div className="hub-card-icon"><i className="ph-fill ph-brain"></i></div>
                        <h2>Decision Engine</h2>
                        <p>Rule-based translation system compiling agent dialogue scripts based on risk.</p>
                        <div className="hub-card-counts">
                            <div>Decisions: <strong id="metric-decision-actions">--</strong></div>
                            <div>Recommended: <strong id="metric-decision-rec">--</strong></div>
                        </div>
                    </div>

                    {/* Option 5: Demand Forecasting */}
                    <div className="hub-card predictive clickable-hub-card" data-target="demand-forecast-tab">
                        <span className="hub-card-port">Port 8002</span>
                        <div className="hub-card-icon"><i className="ph-fill ph-trend-up"></i></div>
                        <h2>Demand Forecasting</h2>
                        <p>Customer-centric prediction of future insurance product demand using Prophet ML.</p>
                        <div className="hub-card-counts">
                            <div>Products: <strong style={{color: "var(--accent-predictive)"}}>4</strong></div>
                            <div>Forecast: <strong style={{color: "var(--accent-predictive)"}}>12 Mo</strong></div>
                        </div>
                    </div>

                    {/* Option 6: Retail Forecasting */}
                    <div className="hub-card predictive clickable-hub-card" data-target="retail-forecast-tab">
                        <span className="hub-card-port">Port 8002</span>
                        <div className="hub-card-icon"><i className="ph-fill ph-storefront"></i></div>
                        <h2>Retail Forecasting</h2>
                        <p>Cross-domain analysis of 5 different forecasting models on Kaggle retail datasets.</p>
                        <div className="hub-card-counts">
                            <div>Models: <strong style={{color: "var(--accent-predictive)"}}>5</strong></div>
                            <div>Horizon: <strong style={{color: "var(--accent-predictive)"}}>30 D</strong></div>
                        </div>
                    </div>
                </div>

                {/* Admin & Management Center Links */}
                <div className="admin-grid" style={{"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "1.5rem", "width": "100%", "maxWidth": "1000px", "marginTop": "2rem"}}>
                    <div className="hub-card retrain clickable-hub-card" data-target="retrain-tab" style={{"padding": "1.5rem", "flexDirection": "row", "gap": "1.2rem", "alignItems": "center"}}>
                        <div className="hub-card-icon" style={{"fontSize": "1.8rem", "width": "48px", "height": "48px"}}><i className="ph-fill ph-arrows-clockwise" style={{"color": "var(--accent-warning)"}}></i></div>
                        <div>
                            <h3 style={{"color": "var(--text-primary)", "fontSize": "1.05rem"}}>Ecosystem Retrain Console</h3>
                            <p style={{"fontSize": "0.85rem", "marginTop": "3px", "color": "var(--text-secondary)"}}>Train models and view execution log streams.</p>
                        </div>
                    </div>
                    
                    <div className="hub-card data clickable-hub-card" data-target="data-tab" style={{"padding": "1.5rem", "flexDirection": "row", "gap": "1.2rem", "alignItems": "center"}}>
                        <div className="hub-card-icon" style={{"fontSize": "1.8rem", "width": "48px", "height": "48px"}}><i className="ph-fill ph-database" style={{"color": "#fff"}}></i></div>
                        <div>
                            <h3 style={{"color": "var(--text-primary)", "fontSize": "1.05rem"}}>Ecosystem Data Center</h3>
                            <p style={{"fontSize": "0.85rem", "marginTop": "3px", "color": "var(--text-secondary)"}}>Upload leads/customers CSV files and view database records.</p>
                        </div>
                    </div>
                </div>
            </div>

            {/* PANEL 2: CUSTOMER RETENTION PANEL (Mirrors the original Insure AI project) */}
            <div id="retention-tab" className="tab-pane">
                <header className="panel-header">
                    <button className="btn btn-secondary back-home-btn"><i className="ph ph-arrow-left"></i> Back to Hub</button>
                    <h2>Customer Retention Dashboard</h2>
                    <span className="card-badge retention">Port 8000</span>
                </header>

                {/* Retention Stats Grid (Original Insure AI metrics style, clickable for directories) */}
                <div className="stats-grid" style={{"gridTemplateColumns": "repeat(3, 1fr)", "width": "100%", "maxWidth": "100%"}}>
                    <div className="stat-card glass-panel clickable" id="retention-card-leads" title="Open All Leads Directory" style={{"cursor": "pointer"}}>
                        <div className="stat-icon blue"><i className="ph-fill ph-users"></i></div>
                        <div className="stat-info">
                            <span className="stat-label">Total Leads</span>
                            <h3 className="stat-value" id="retention-stat-leads">--</h3>
                        </div>
                    </div>
                    <div className="stat-card glass-panel clickable" id="retention-card-cust" title="Open All Customers Directory" style={{"cursor": "pointer"}}>
                        <div className="stat-icon green"><i className="ph-fill ph-check-circle"></i></div>
                        <div className="stat-info">
                            <span className="stat-label">Total Customers</span>
                            <h3 className="stat-value" id="retention-stat-cust">--</h3>
                        </div>
                    </div>
                    <div className="stat-card glass-panel clickable" id="retention-card-last-trained" title="View Training History" style={{"cursor": "pointer"}}>
                        <div className="stat-icon yellow"><i className="ph-fill ph-clock-counter-clockwise"></i></div>
                        <div className="stat-info">
                            <span className="stat-label">Last Trained</span>
                            <h3 className="stat-value" id="retention-stat-last-trained">--</h3>
                        </div>
                    </div>
                </div>

                {/* Info & Management Grid (Original Insure AI Actions) */}
                <div className="upload-grid" style={{"marginTop": "1rem"}}>
                    {/* System Info */}
                    <div className="glass-panel" style={{"display": "flex", "flexDirection": "column", "gap": "12px"}}>
                        <div className="dashboard-card-header">
                            <h3>System Info</h3>
                        </div>
                        <p style={{"fontSize": "0.95rem"}}><strong>Lead Model Accuracy:</strong> <span id="retention-lead-acc" style={{"color": "var(--accent-retention)"}}>--</span></p>
                        <p style={{"fontSize": "0.95rem"}}><strong>Customer Model Accuracy:</strong> <span id="retention-cust-acc" style={{"color": "var(--accent-decision)"}}>--</span></p>
                        <button id="retention-train-btn" className="btn btn-primary" style={{"marginTop": "auto", "background": "var(--accent-warning)", "color": "var(--bg-dark)", "width": "100%"}}>
                            <i className="ph ph-arrows-clockwise"></i>
                            <span>Retrain Models</span>
                        </button>
                    </div>

                    {/* Data Management */}
                    <div className="glass-panel" style={{"display": "flex", "flexDirection": "column", "gap": "12px"}}>
                        <div className="dashboard-card-header">
                            <h3>Data Management</h3>
                        </div>
                        <p style={{"fontSize": "0.9rem", "color": "var(--text-secondary)"}}>Upload new CSV datasets or export existing data.</p>
                        <div style={{"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "10px", "marginTop": "auto"}}>
                            <label htmlFor="retention-upload-leads-input" className="btn btn-secondary" style={{"cursor": "pointer", "display": "flex", "gap": "8px", "justifyContent": "center", "alignItems": "center"}}>
                                <i className="ph ph-upload-simple"></i>
                                <span>Upload Leads</span>
                            </label>
                            <input type="file" id="retention-upload-leads-input" accept=".csv" style={{"display": "none"}} />
                            
                            <button id="retention-export-leads-btn" className="btn btn-secondary">
                                <i className="ph ph-download-simple"></i>
                                <span>Export Leads</span>
                            </button>
                            
                            <label htmlFor="retention-upload-cust-input" className="btn btn-secondary" style={{"cursor": "pointer", "display": "flex", "gap": "8px", "justifyContent": "center", "alignItems": "center"}}>
                                <i className="ph ph-upload-simple"></i>
                                <span>Upload Cust</span>
                            </label>
                            <input type="file" id="retention-upload-cust-input" accept=".csv" style={{"display": "none"}} />
                            
                            <button id="retention-export-cust-btn" className="btn btn-secondary">
                                <i className="ph ph-download-simple"></i>
                                <span>Export Cust</span>
                            </button>
                        </div>
                    </div>
                </div>

                {/* High Propensity Leads Table (Top 20) */}
                <div className="table-card glass-panel" style={{"marginTop": "1rem"}}>
                    <div className="dashboard-card-header">
                        <h3>High Propensity Leads</h3>
                        <p style={{"fontSize": "0.85rem", "color": "var(--text-secondary)"}}>Top 20 prospects ranked by AI conversion probability.</p>
                    </div>
                    <div className="table-wrapper">
                        <table>
                            <thead>
                                <tr>
                                    <th>Lead ID</th>
                                    <th>Target Score</th>
                                    <th>AI Recommendation Reason</th>
                                    <th>Source</th>
                                </tr>
                            </thead>
                            <tbody id="retention-top20-leads-tbody">
                                {/* Populated dynamically */}
                            </tbody>
                        </table>
                    </div>
                </div>

                {/* High Churn Risk Customers Table (Top 20) */}
                <div className="table-card glass-panel" style={{"marginTop": "1rem"}}>
                    <div className="dashboard-card-header">
                        <h3>High-Risk Customers</h3>
                        <p style={{"fontSize": "0.85rem", "color": "var(--text-secondary)"}}>Current policyholders at highest risk of churning.</p>
                    </div>
                    <div className="table-wrapper">
                        <table>
                            <thead>
                                <tr>
                                    <th>Customer ID</th>
                                    <th>Risk Level</th>
                                    <th>Primary Risk Factor</th>
                                    <th>Policy Type</th>
                                    <th>Contact</th>
                                </tr>
                            </thead>
                            <tbody id="retention-top20-cust-tbody">
                                {/* Populated dynamically */}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            {/* PANEL 3: ANOMALY DETECTION PANEL */}
            <div id="anomaly-tab" className="tab-pane">
                <header className="panel-header">
                    <button className="btn btn-secondary back-home-btn"><i className="ph ph-arrow-left"></i> Back to Hub</button>
                    <h2>Anomaly & Fraud Detection Dashboard</h2>
                    <span className="card-badge anomaly">Port 8001</span>
                </header>

                <div className="table-card glass-panel">
                    <div className="dashboard-card-header">
                        <h3>Lead Fraud Anomaly Scans</h3>
                    </div>
                    <div className="table-wrapper">
                        <table>
                            <thead>
                                <tr>
                                    <th>Lead Name</th>
                                    <th>Risk Status</th>
                                    <th>Anomaly Score</th>
                                    <th>Reason Flag</th>
                                    <th>Contact Info</th>
                                </tr>
                            </thead>
                            <tbody id="anomaly-leads-tbody">
                                {/* Populated dynamically */}
                            </tbody>
                        </table>
                    </div>
                    <div className="pagination">
                        <button id="prev-anomaly-leads" className="btn btn-outline" disabled>Previous</button>
                        <span id="anomaly-leads-page">Page 1</span>
                        <button id="next-anomaly-leads" className="btn btn-outline">Next</button>
                    </div>
                </div>

                <div className="table-card glass-panel">
                    <div className="dashboard-card-header">
                        <h3>Customer Account Scans</h3>
                    </div>
                    <div className="table-wrapper">
                        <table>
                            <thead>
                                <tr>
                                    <th>Customer ID / Name</th>
                                    <th>Risk Status</th>
                                    <th>Anomaly Score</th>
                                    <th>NLP Sentiment</th>
                                    <th>Contact Info</th>
                                </tr>
                            </thead>
                            <tbody id="anomaly-cust-tbody">
                                {/* Populated dynamically */}
                            </tbody>
                        </table>
                    </div>
                    <div className="pagination">
                        <button id="prev-anomaly-cust" className="btn btn-outline" disabled>Previous</button>
                        <span id="anomaly-cust-page">Page 1</span>
                        <button id="next-anomaly-cust" className="btn btn-outline">Next</button>
                    </div>
                </div>
            </div>

            {/* PANEL 4: PREDICTIVE AI PANEL */}
            <div id="predictive-tab" className="tab-pane">
                <header className="panel-header">
                    <button className="btn btn-secondary back-home-btn"><i className="ph ph-arrow-left"></i> Back to Hub</button>
                    <h2>Predictive Intelligence Dashboard</h2>
                    <span className="card-badge predictive">Port 8002</span>
                    <div style={{"marginLeft": "auto", "fontSize": "0.9rem", "color": "var(--text-secondary)", "display": "flex", "gap": "15px"}}>
                        <span>Leads: <strong id="predictive-stat-leads" style={{"color": "var(--accent-predictive)"}}>--</strong></span>
                        <span>Customers: <strong id="predictive-stat-cust" style={{"color": "#fff"}}>--</strong></span>
                    </div>
                </header>

                <div className="glass-panel" style={{"display": "flex", "flexDirection": "column", "gap": "1.2rem"}}>
                    <div className="dashboard-card-header">
                        <h3>Forecasted Conversion Trends (Prophet Engine)</h3>
                    </div>
                    <div style={{"height": "350px", "position": "relative"}}>
                        <canvas id="forecastChart"></canvas>
                    </div>
                </div>

                <div className="table-card glass-panel">
                    <div className="dashboard-card-header">
                        <h3>Agent Customer Interaction Logs</h3>
                    </div>
                    <div className="table-wrapper">
                        <table>
                            <thead>
                                <tr>
                                    <th>Agent ID</th>
                                    <th>Call Timestamp</th>
                                    <th>Duration</th>
                                    <th>Outcome</th>
                                </tr>
                            </thead>
                            <tbody id="predictive-logs-tbody">
                                {/* Populated dynamically */}
                            </tbody>
                        </table>
                    </div>
                    <div className="pagination">
                        <button id="prev-predictive-calls" className="btn btn-outline" disabled>Previous</button>
                        <span id="predictive-calls-page">Page 1</span>
                        <button id="next-predictive-calls" className="btn btn-outline">Next</button>
                    </div>
                </div>
            </div>

            {/* PANEL 5: DECISION ENGINE PANEL */}
            <div id="decision-tab" className="tab-pane">
                <header className="panel-header">
                    <button className="btn btn-secondary back-home-btn"><i className="ph ph-arrow-left"></i> Back to Hub</button>
                    <h2>Decision Engine Dashboard</h2>
                    <span className="card-badge decision">Port 8003</span>
                </header>

                <div className="table-card glass-panel">
                    <div className="dashboard-card-header">
                        <h3>Leads Translation Decisions</h3>
                    </div>
                    <div className="table-wrapper">
                        <table>
                            <thead>
                                <tr>
                                    <th>Lead Name</th>
                                    <th>Score Ratio</th>
                                    <th>Dialogue Script Advice</th>
                                    <th>Contact Info</th>
                                </tr>
                            </thead>
                            <tbody id="decision-leads-tbody">
                                {/* Populated dynamically */}
                            </tbody>
                        </table>
                    </div>
                    <div className="pagination">
                        <button id="prev-decision-leads" className="btn btn-outline" disabled>Previous</button>
                        <span id="decision-leads-page">Page 1</span>
                        <button id="next-decision-leads" className="btn btn-outline">Next</button>
                    </div>
                </div>

                <div className="table-card glass-panel">
                    <div className="dashboard-card-header">
                        <h3>Customer Retainment Actions</h3>
                    </div>
                    <div className="table-wrapper">
                        <table>
                            <thead>
                                <tr>
                                    <th>Customer ID / Name</th>
                                    <th>Score Ratio</th>
                                    <th>Retention Dialogue Action Advice</th>
                                    <th>Contact Info</th>
                                </tr>
                            </thead>
                            <tbody id="decision-cust-tbody">
                                {/* Populated dynamically */}
                            </tbody>
                        </table>
                    </div>
                    <div className="pagination">
                        <button id="prev-decision-cust" className="btn btn-outline" disabled>Previous</button>
                        <span id="decision-cust-page">Page 1</span>
                        <button id="next-decision-cust" className="btn btn-outline">Next</button>
                    </div>
                </div>
            </div>

            {/* PANEL 6: RETRAIN CONSOLE VIEW */}
            <div id="retrain-tab" className="tab-pane">
                <header className="panel-header">
                    <button className="btn btn-secondary back-home-btn"><i className="ph ph-arrow-left"></i> Back to Hub</button>
                    <h2>Ecosystem Retrain Console</h2>
                    <span className="card-badge" style={{"color": "var(--accent-warning)"}}>Console</span>
                </header>

                <div className="glass-panel" style={{"display": "flex", "flexDirection": "column", "gap": "1.5rem"}}>
                    <p style={{"fontSize": "0.95rem"}}>Select which subsystem model you wish to retrain. The server will execute the training scripts and compile metrics in real time.</p>
                    
                    <div className="retrain-selector-grid">
                        <button className="retrain-btn-selector active" data-port="8000">Retention [Port 8000]</button>
                        <button className="retrain-btn-selector" data-port="8001">Anomaly [Port 8001]</button>
                        <button className="retrain-btn-selector" data-port="8002">Predictive [Port 8002]</button>
                        <button className="retrain-btn-selector" data-port="8003">Decision [Port 8003]</button>
                    </div>

                    <div className="console-card">
                        <div className="console-terminal" id="console-output">
                            {/* Retraining outputs here */}
                        </div>
                    </div>

                    <div>
                        <button id="exec-train-btn" className="btn btn-primary" style={{"backgroundColor": "var(--accent-warning)", "color": "var(--bg-dark)"}}>
                            <i className="ph ph-arrows-clockwise"></i>
                            <span>Retrain Model</span>
                        </button>
                    </div>
                </div>
            </div>

            {/* PANEL 7: DATA CENTER VIEW */}
            <div id="data-tab" className="tab-pane">
                <header className="panel-header">
                    <button className="btn btn-secondary back-home-btn"><i className="ph ph-arrow-left"></i> Back to Hub</button>
                    <h2>Ecosystem Data Center</h2>
                    <span className="card-badge" style={{"color": "#fff"}}>Database</span>
                </header>

                <div className="upload-grid">
                    <div className="glass-panel" style={{"display": "flex", "flexDirection": "column", "gap": "1.5rem"}}>
                        <div className="dashboard-card-header">
                            <h3>Upload Datasets</h3>
                            <span className="card-badge" style={{"color": "var(--text-primary)"}}>Ingest CSV</span>
                        </div>
                        
                        <p style={{"fontSize": "0.9rem"}}>Select a target subsystem and upload a customer or lead dataset to clean, normalize, and save to the database.</p>
                        
                        <div style={{"display": "flex", "flexDirection": "column", "gap": "12px"}}>
                            <label style={{"fontSize": "0.8rem", "fontWeight": "600", "color": "var(--text-primary)"}}>Target Subsystem</label>
                            <select id="upload-service-select" style={{"background": "#131520", "border": "1px solid var(--border-color)", "color": "#fff", "padding": "10px", "borderRadius": "8px"}}>
                                <option value="retention">Customer Retention [Port 8000]</option>
                                <option value="anomaly">Anomaly Detection [Port 8001]</option>
                                <option value="predictive">Predictive Intelligence [Port 8002]</option>
                                <option value="decision">Decision Making [Port 8003]</option>
                            </select>

                            <label style={{"fontSize": "0.8rem", "fontWeight": "600", "color": "var(--text-primary)"}}>Dataset Type</label>
                            <select id="upload-dataset-select" style={{"background": "#131520", "border": "1px solid var(--border-color)", "color": "#fff", "padding": "10px", "borderRadius": "8px"}}>
                                <option value="leads">Leads CSV</option>
                                <option value="customers">Customers CSV</option>
                            </select>

                            <label style={{"fontSize": "0.8rem", "fontWeight": "600", "color": "var(--text-primary)", "marginTop": "8px"}}>Select File</label>
                            <input type="file" id="dataset-file-input" accept=".csv" style={{"background": "#131520", "border": "1px solid var(--border-color)", "color": "#fff", "padding": "10px", "borderRadius": "8px"}} />
                        </div>

                        <button id="upload-submit-btn" className="btn btn-primary" style={{"marginTop": "8px"}}>
                            <i className="ph ph-upload-simple"></i>
                            <span>Upload Dataset</span>
                        </button>
                    </div>

                    <div className="glass-panel" style={{"display": "flex", "flexDirection": "column", "gap": "1.5rem"}}>
                        <div className="dashboard-card-header">
                            <h3>Export Subsystem Data</h3>
                            <span className="card-badge" style={{"color": "var(--text-primary)"}}>Download CSV</span>
                        </div>
                        
                        <p style={{"fontSize": "0.9rem"}}>Fetch and download the processed datasets directly from the SQL database records of the selected subsystem.</p>
                        
                        <div style={{"display": "flex", "flexDirection": "column", "gap": "12px"}}>
                            <label style={{"fontSize": "0.8rem", "fontWeight": "600", "color": "var(--text-primary)"}}>Target Subsystem</label>
                            <select id="export-service-select" style={{"background": "#131520", "border": "1px solid var(--border-color)", "color": "#fff", "padding": "10px", "borderRadius": "8px"}}>
                                <option value="retention">Customer Retention [Port 8000]</option>
                                <option value="anomaly">Anomaly Detection [Port 8001]</option>
                                <option value="predictive">Predictive Intelligence [Port 8002]</option>
                                <option value="decision">Decision Making [Port 8003]</option>
                            </select>

                            <label style={{"fontSize": "0.8rem", "fontWeight": "600", "color": "var(--text-primary)"}}>Dataset Type</label>
                            <select id="export-dataset-select" style={{"background": "#131520", "border": "1px solid var(--border-color)", "color": "#fff", "padding": "10px", "borderRadius": "8px"}}>
                                <option value="leads">Leads Export</option>
                                <option value="customers">Customers Export</option>
                            </select>
                        </div>

                        <button id="export-submit-btn" className="btn btn-secondary" style={{"marginTop": "auto"}}>
                            <i className="ph ph-download-simple"></i>
                            <span>Export Dataset</span>
                        </button>
                    </div>

                    {/* RECENTLY INGESTED DATA TABLE */}
                    <div className="glass-panel" style={{"gridColumn": "span 2", "marginTop": "1rem"}}>
                        <div className="dashboard-card-header">
                            <h3>Recently Ingested Database Entries (Double-Check Uploads)</h3>
                            <span className="card-badge" style={{"color": "var(--accent-retention)"}}>Database Log</span>
                        </div>
                        <p style={{"fontSize": "0.85rem", "marginBottom": "1rem"}}>Review the actual rows loaded into the database from the last CSV upload. Updates instantly.</p>
                        
                        <div className="retrain-selector-grid" style={{"gridTemplateColumns": "repeat(4, 1fr)", "marginBottom": "1.5rem"}}>
                            <button className="recent-selector-btn active" data-service="retention">Retention [8000]</button>
                            <button className="recent-selector-btn" data-service="anomaly">Anomaly [8001]</button>
                            <button className="recent-selector-btn" data-service="predictive">Predictive [8002]</button>
                            <button className="recent-selector-btn" data-service="decision">Decision [8003]</button>
                        </div>

                        <div className="table-wrapper">
                            <table>
                                <thead>
                                    <tr>
                                        <th>Entry ID</th>
                                        <th>Primary Reference</th>
                                        <th>Secondary Details</th>
                                        <th>Database Schema Mapping Info</th>
                                    </tr>
                                </thead>
                                <tbody id="recently-ingested-tbody">
                                    {/* Populated dynamically */}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>

    {/* PANEL 8: DEMAND FORECASTING (New feature) */}
    <div id="demand-forecast-tab" className="tab-pane">
        <header className="panel-header">
            <button className="btn btn-secondary back-home-btn"><i className="ph ph-arrow-left"></i> Back to Hub</button>
            <h2>Customer-Centric Demand Forecasting</h2>
            <span className="card-badge predictive">Port 8002</span>
        </header>
        <div className="stats-grid" style={{gridTemplateColumns: "repeat(4, 1fr)"}}>
            <div className="stat-card glass-panel">
                <div className="stat-icon blue"><i className="ph-fill ph-heart"></i></div>
                <div className="stat-info">
                    <span className="stat-label">Life Peak Demand</span>
                    <h3 className="stat-value" id="demand-peak-life">--</h3>
                </div>
            </div>
            <div className="stat-card glass-panel">
                <div className="stat-icon purple"><i className="ph-fill ph-car"></i></div>
                <div className="stat-info">
                    <span className="stat-label">Auto Peak Demand</span>
                    <h3 className="stat-value" id="demand-peak-auto">--</h3>
                </div>
            </div>
            <div className="stat-card glass-panel">
                <div className="stat-icon orange"><i className="ph-fill ph-house"></i></div>
                <div className="stat-info">
                    <span className="stat-label">Home Peak Demand</span>
                    <h3 className="stat-value" id="demand-peak-home">--</h3>
                </div>
            </div>
            <div className="stat-card glass-panel">
                <div className="stat-icon green"><i className="ph-fill ph-first-aid"></i></div>
                <div className="stat-info">
                    <span className="stat-label">Health Peak Demand</span>
                    <h3 className="stat-value" id="demand-peak-health">--</h3>
                </div>
            </div>
        </div>
        <div className="glass-panel" style={{padding: "20px", marginTop: "20px"}}>
            <h3>12-Month Product Demand Projection</h3>
            <p style={{color: "var(--text-secondary)", marginBottom: "15px"}}>Powered by Facebook Prophet Multivariate Time Series Engine.</p>
            <div className="chart-container" style={{height: "400px", width: "100%"}}>
                <canvas id="demandForecastChart"></canvas>
            </div>
        </div>
    </div>

    {/* PANEL 9: RETAIL FORECASTING (Cross-Domain) */}
    <div id="retail-forecast-tab" className="tab-pane">
        <header className="panel-header">
            <button className="btn btn-secondary back-home-btn"><i className="ph ph-arrow-left"></i> Back to Hub</button>
            <h2>Cross-Domain Demand Forecasting (Retail)</h2>
            <span className="card-badge predictive">Port 8002</span>
        </header>
        
        <div className="stats-grid" style={{gridTemplateColumns: "repeat(3, 1fr)"}}>
            <div className="stat-card glass-panel">
                <div className="stat-icon blue"><i className="ph-fill ph-database"></i></div>
                <div className="stat-info">
                    <span className="stat-label">Dataset Size</span>
                    <h3 className="stat-value">1,096 Days</h3>
                </div>
            </div>
            <div className="stat-card glass-panel">
                <div className="stat-icon purple"><i className="ph-fill ph-trend-up"></i></div>
                <div className="stat-info">
                    <span className="stat-label">Forecast Horizon</span>
                    <h3 className="stat-value">30 Days</h3>
                </div>
            </div>
            <div className="stat-card glass-panel">
                <div className="stat-icon orange"><i className="ph-fill ph-code"></i></div>
                <div className="stat-info">
                    <span className="stat-label">Algorithm Stack</span>
                    <h3 className="stat-value">5 Models</h3>
                </div>
            </div>
        </div>

        <div className="glass-panel" style={{padding: "20px", marginTop: "20px"}}>
            <div style={{display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "15px"}}>
                <div>
                    <h3>Forecast Comparison Analysis</h3>
                    <p style={{color: "var(--text-secondary)"}}>Analyzing retail sales using 5 independent statistical and machine learning models (Prophet, XGBoost, SARIMA, Holt-Winters, SMA).</p>
                </div>
                <div style={{display: "flex", gap: "10px", alignItems: "center"}}>
                    <select id="retail-level-select" className="search-input" style={{width: "200px", padding: "8px"}}>
                        <option value="store">Total Store (Aggregate)</option>
                        <option value="category">By Product Category</option>
                        <option value="product">By Individual Product</option>
                    </select>
                    <select id="retail-item-select" className="search-input" style={{width: "250px", padding: "8px", display: "none"}}>
                        {/* Options populated dynamically */}
                    </select>
                </div>
            </div>
            <div className="chart-container" style={{height: "400px", width: "100%", position: "relative"}}>
                <canvas id="retailForecastChart"></canvas>
                <div id="retail-loading-overlay" style={{ position: "absolute", inset: "0", background: "rgba(10,10,12,0.8)", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", zIndex: 10 }}>
                    <div className="spinner" style={{ width: "40px", height: "40px", border: "4px solid rgba(255,255,255,0.1)", borderTop: "4px solid var(--accent-predictive)", borderRadius: "50%", animation: "spin 1s linear infinite" }}></div>
                    <p style={{ marginTop: "1rem", color: "var(--text-secondary)" }}>Training 5 Models & Generating Forecasts...</p>
                </div>
            </div>
        </div>

        <div className="glass-panel" style={{padding: "20px", marginTop: "20px"}}>
            <h3>Cross-Domain Applications of Demand Forecasting</h3>
            <p style={{color: "var(--text-secondary)", lineHeight: "1.6", marginBottom: "15px"}}>
                The same mathematical principles and machine learning algorithms used to predict insurance product demand can be seamlessly translated to virtually any industry. By swapping the underlying time-series data, these models adapt to different seasonal patterns and trends.
            </p>
            
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1.5rem" }}>
                <div style={{ background: "rgba(255,255,255,0.02)", padding: "1.5rem", borderRadius: "8px", border: "1px solid rgba(255,255,255,0.05)" }}>
                    <h3 style={{ color: "var(--accent-predictive)", marginBottom: "0.5rem", display: "flex", alignItems: "center", gap: "0.5rem" }}><i className="ph-fill ph-shopping-cart"></i> Retail & E-Commerce</h3>
                    <p style={{ color: "var(--text-secondary)", fontSize: "0.9rem", lineHeight: "1.5" }}>Models like SARIMA and XGBoost accurately capture weekend sales spikes and holiday seasonality (e.g., Black Friday), optimizing inventory levels and preventing stockouts.</p>
                </div>
                <div style={{ background: "rgba(255,255,255,0.02)", padding: "1.5rem", borderRadius: "8px", border: "1px solid rgba(255,255,255,0.05)" }}>
                    <h3 style={{ color: "var(--accent-retention)", marginBottom: "0.5rem", display: "flex", alignItems: "center", gap: "0.5rem" }}><i className="ph-fill ph-truck"></i> Supply Chain & Logistics</h3>
                    <p style={{ color: "var(--text-secondary)", fontSize: "0.9rem", lineHeight: "1.5" }}>Forecasting shipping volume and warehouse utilization allows logistics companies to dynamically allocate fleets and negotiate better supplier contracts.</p>
                </div>
                <div style={{ background: "rgba(255,255,255,0.02)", padding: "1.5rem", borderRadius: "8px", border: "1px solid rgba(255,255,255,0.05)" }}>
                    <h3 style={{ color: "var(--accent-decision)", marginBottom: "0.5rem", display: "flex", alignItems: "center", gap: "0.5rem" }}><i className="ph-fill ph-lightning"></i> Energy Grid Management</h3>
                    <p style={{ color: "var(--text-secondary)", fontSize: "0.9rem", lineHeight: "1.5" }}>Prophet is highly effective at predicting daily and seasonal power consumption spikes, ensuring the grid can supply enough electricity without burning excess coal.</p>
                </div>
                <div style={{ background: "rgba(255,255,255,0.02)", padding: "1.5rem", borderRadius: "8px", border: "1px solid rgba(255,255,255,0.05)" }}>
                    <h3 style={{ color: "var(--accent-anomaly)", marginBottom: "0.5rem", display: "flex", alignItems: "center", gap: "0.5rem" }}><i className="ph-fill ph-heartbeat"></i> Healthcare</h3>
                    <p style={{ color: "var(--text-secondary)", fontSize: "0.9rem", lineHeight: "1.5" }}>Predicting patient admission rates and disease outbreak seasonality allows hospitals to adequately staff ICU units and stock critical medical supplies.</p>
                </div>
            </div>
        </div>
    </div>

        </main>
    </div>

    {/* OVERLAY MODALS FROM PREVIOUS RETENTION PROJECT */}
    
    {/* All Leads Directory Modal */}
    <div id="modal-all-leads" className="modal-overlay">
        <div className="modal-content glass-panel" style={{"maxWidth": "850px", "width": "90%"}}>
            <div className="modal-header" style={{"display": "flex", "justifyContent": "space-between", "alignItems": "center", "borderBottom": "1px solid var(--border-color)", "paddingBottom": "12px", "marginBottom": "16px"}}>
                <h2 style={{"color": "#fff", "fontSize": "1.4rem"}}><i className="ph ph-users" style={{"marginRight": "8px", "color": "var(--accent-retention)"}}></i>All Leads Directory</h2>
                <button id="close-modal-leads" style={{"padding": "6px 12px", "fontSize": "0.85rem", "background": "rgba(255,255,255,0.1)", "border": "1px solid rgba(255,255,255,0.2)", "color": "white", "borderRadius": "6px", "cursor": "pointer"}}><i className="ph ph-x"></i> Close</button>
            </div>
            <div className="table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th>Lead ID</th>
                            <th>Name</th>
                            <th>AI Score</th>
                            <th>Primary Reason</th>
                            <th>Source</th>
                        </tr>
                    </thead>
                    <tbody id="all-leads-tbody">
                        {/* Populated via JS */}
                    </tbody>
                </table>
            </div>
            <div className="pagination" style={{"marginTop": "15px"}}>
                <button id="prev-modal-leads" className="btn btn-outline" disabled>Previous</button>
                <span id="modal-leads-page-indicator">Page 1</span>
                <button id="next-modal-leads" className="btn btn-outline">Next</button>
            </div>
        </div>
    </div>

    {/* All Customers Directory Modal */}
    <div id="modal-all-customers" className="modal-overlay">
        <div className="modal-content glass-panel" style={{"maxWidth": "950px", "width": "90%"}}>
            <div className="modal-header" style={{"display": "flex", "justifyContent": "space-between", "alignItems": "center", "borderBottom": "1px solid var(--border-color)", "paddingBottom": "12px", "marginBottom": "16px"}}>
                <h2 style={{"color": "#fff", "fontSize": "1.4rem"}}><i className="ph ph-check-circle" style={{"marginRight": "8px", "color": "var(--accent-decision)"}}></i>All Customers Directory</h2>
                <button id="close-modal-customers" style={{"padding": "6px 12px", "fontSize": "0.85rem", "background": "rgba(255,255,255,0.1)", "border": "1px solid rgba(255,255,255,0.2)", "color": "white", "borderRadius": "6px", "cursor": "pointer"}}><i className="ph ph-x"></i> Close</button>
            </div>
            <div className="table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th>Customer ID</th>
                            <th>Name</th>
                            <th>Risk Level</th>
                            <th>Primary Risk Factor</th>
                            <th>Sentiment</th>
                            <th>Contact</th>
                        </tr>
                    </thead>
                    <tbody id="all-customers-tbody">
                        {/* Populated via JS */}
                    </tbody>
                </table>
            </div>
            <div className="pagination" style={{"marginTop": "15px"}}>
                <button id="prev-modal-customers" className="btn btn-outline" disabled>Previous</button>
                <span id="modal-customers-page-indicator">Page 1</span>
                <button id="next-modal-customers" className="btn btn-outline">Next</button>
            </div>
        </div>
    </div>

    {/* Training History Modal */}
    <div id="modal-training-history" className="modal-overlay">
        <div className="modal-content glass-panel" style={{"maxWidth": "850px", "width": "90%"}}>
            <div className="modal-header" style={{"display": "flex", "justifyContent": "space-between", "alignItems": "center", "borderBottom": "1px solid var(--border-color)", "paddingBottom": "12px", "marginBottom": "16px"}}>
                <h2 style={{"color": "#fff", "fontSize": "1.4rem"}}><i className="ph ph-clock-counter-clockwise" style={{"marginRight": "8px", "color": "var(--accent-warning)"}}></i>AI Training & Model History</h2>
                <button id="close-modal-training" style={{"padding": "6px 12px", "fontSize": "0.85rem", "background": "rgba(255,255,255,0.1)", "border": "1px solid rgba(255,255,255,0.2)", "color": "white", "borderRadius": "6px", "cursor": "pointer"}}><i className="ph ph-x"></i> Close</button>
            </div>
            <div className="table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th>Date / Time</th>
                            <th>Model Type</th>
                            <th>Version ID</th>
                            <th>Accuracy</th>
                            <th>Algorithm Used</th>
                        </tr>
                    </thead>
                    <tbody id="training-history-tbody">
                        {/* Populated via JS */}
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    {/* Retrain Progress Log Modal Overlay */}
    <div id="modal-training-progress" className="modal-overlay">
        <div className="modal-content glass-panel" style={{"maxWidth": "600px", "width": "90%"}}>
            <div className="modal-header" style={{"display": "flex", "justifyContent": "space-between", "alignItems": "center", "borderBottom": "1px solid var(--border-color)", "paddingBottom": "12px", "marginBottom": "16px"}}>
                <h2 style={{"color": "#fff", "fontSize": "1.3rem"}}><i className="ph ph-spinner ph-spin" style={{"marginRight": "8px", "color": "var(--accent-warning)"}}></i>AI Training in Progress</h2>
            </div>
            <div style={{"background": "#040508", "color": "#00ff66", "fontFamily": "monospace", "padding": "15px", "borderRadius": "8px", "height": "320px", "overflowY": "auto", "fontSize": "13px", "lineHeight": "1.5", "boxShadow": "inset 0 0 10px rgba(0,0,0,0.5)"}} id="modal-training-logs">
                Initializing training pipelines...
            </div>
        </div>
    </div>

    {/* Customer 360 Modal */}
    <div id="modal-customer-360" className="modal-overlay">
        <div className="modal-content glass-panel" style={{"maxWidth": "1100px", "width": "95%", "maxHeight": "90vh", "overflowY": "auto"}}>
            <div className="modal-header" style={{"display": "flex", "justifyContent": "space-between", "alignItems": "center", "borderBottom": "1px solid var(--border-color)", "paddingBottom": "12px", "marginBottom": "20px"}}>
                <h2 style={{"color": "#fff", "fontSize": "1.6rem", "display": "flex", "alignItems": "center", "gap": "10px"}}>
                    <i className="ph-fill ph-user-circle" style={{"color": "var(--accent-predictive)"}}></i> 
                    Customer 360 Profile: <span id="c360-title-name" style={{"color": "var(--accent-warning)", "marginLeft": "5px"}}>--</span>
                </h2>
                <button id="close-modal-c360" style={{"padding": "6px 12px", "fontSize": "0.85rem", "background": "rgba(255,255,255,0.1)", "border": "1px solid rgba(255,255,255,0.2)", "color": "white", "borderRadius": "6px", "cursor": "pointer"}}><i className="ph ph-x"></i> Close</button>
            </div>
            
            <div style={{"display": "grid", "gridTemplateColumns": "2fr 1fr", "gap": "20px"}}>
                {/* Left Column: Transactional Summary */}
                <div style={{"display": "flex", "flexDirection": "column", "gap": "20px"}}>
                    <div className="glass-panel" style={{"padding": "20px"}}>
                        <h3 style={{"marginBottom": "15px", "borderBottom": "1px solid rgba(255,255,255,0.1)", "paddingBottom": "10px"}}>
                            <i className="ph ph-clock-counter-clockwise"></i> Lifetime Transactional Summary
                        </h3>
                        <div className="table-wrapper" style={{"maxHeight": "300px", "overflowY": "auto"}}>
                            <table>
                                <thead>
                                    <tr>
                                        <th>Policy Type</th>
                                        <th>Status</th>
                                        <th>Term</th>
                                        <th>Premium</th>
                                        <th>Claims</th>
                                    </tr>
                                </thead>
                                <tbody id="c360-policies-tbody">
                                </tbody>
                                <tfoot>
                                    <tr style={{"background": "rgba(255,255,255,0.05)", "fontWeight": "bold"}}>
                                        <td colSpan={3} style={{"textAlign": "right", "paddingRight": "15px", "color": "var(--text-secondary)"}}>Lifetime Grand Total Spent:</td>
                                        <td colSpan={2} id="c360-total-spent" style={{"color": "#00ff66", "fontSize": "1.1rem"}}>$0.00</td>
                                    </tr>
                                </tfoot>
                            </table>
                        </div>
                    </div>
                    
                    <div className="glass-panel" style={{"padding": "20px"}}>
                        <h3 style={{"marginBottom": "15px", "borderBottom": "1px solid rgba(255,255,255,0.1)", "paddingBottom": "10px"}}>
                            <i className="ph ph-chat-text"></i> NLP Sentiment & Feedback
                        </h3>
                        <p style={{"fontStyle": "italic", "color": "var(--text-secondary)", "marginBottom": "15px"}} id="c360-feedback-notes">No notes available.</p>
                        <div style={{"display": "flex", "gap": "10px", "flexWrap": "wrap"}} id="c360-keywords-container">
                            {/* Keyword tags here */}
                        </div>
                    </div>
                </div>
                
                {/* Right Column: Predictive & Prescriptive */}
                <div style={{"display": "flex", "flexDirection": "column", "gap": "20px"}}>
                    {/* Predictive */}
                    <div className="glass-panel" style={{"padding": "20px"}}>
                        <h3 style={{"marginBottom": "15px", "borderBottom": "1px solid rgba(255,255,255,0.1)", "paddingBottom": "10px"}}>
                            <i className="ph ph-chart-polar"></i> Predictive Summary
                        </h3>
                        <div style={{"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "15px"}}>
                            <div style={{"background": "rgba(255,255,255,0.05)", "padding": "15px", "borderRadius": "8px", "textAlign": "center"}}>
                                <div style={{"fontSize": "0.8rem", "color": "var(--text-secondary)", "textTransform": "uppercase"}}>BoW Sentiment Score</div>
                                <div style={{"fontSize": "1.8rem", "fontWeight": "700", "marginTop": "5px"}} id="c360-score-sentiment">--</div>
                            </div>
                            <div style={{"background": "rgba(255,255,255,0.05)", "padding": "15px", "borderRadius": "8px", "textAlign": "center"}}>
                                <div style={{"fontSize": "0.8rem", "color": "var(--text-secondary)", "textTransform": "uppercase"}}>Behavioral Index</div>
                                <div style={{"fontSize": "1.8rem", "fontWeight": "700", "marginTop": "5px"}} id="c360-score-behavior">--</div>
                            </div>
                            <div style={{"background": "rgba(255,255,255,0.05)", "padding": "15px", "borderRadius": "8px", "textAlign": "center"}}>
                                <div style={{"fontSize": "0.8rem", "color": "var(--text-secondary)", "textTransform": "uppercase"}}>Churn Risk</div>
                                <div style={{"fontSize": "1.8rem", "fontWeight": "700", "marginTop": "5px", "color": "var(--accent-decision)"}} id="c360-score-churn">--</div>
                            </div>
                            <div style={{"background": "rgba(255,255,255,0.05)", "padding": "15px", "borderRadius": "8px", "textAlign": "center"}}>
                                <div style={{"fontSize": "0.8rem", "color": "var(--text-secondary)", "textTransform": "uppercase"}}>Propensity Score</div>
                                <div style={{"fontSize": "1.8rem", "fontWeight": "700", "marginTop": "5px", "color": "var(--accent-retention)"}} id="c360-score-propensity">--</div>
                            </div>
                        </div>
                    </div>
                    
                    {/* Prescriptive */}
                    <div className="glass-panel" style={{"padding": "20px", "background": "rgba(33, 150, 243, 0.05)", "border": "1px solid rgba(33, 150, 243, 0.2)"}}>
                        <h3 style={{"marginBottom": "15px", "borderBottom": "1px solid rgba(33, 150, 243, 0.2)", "paddingBottom": "10px", "color": "#64b5f6"}}>
                            <i className="ph-fill ph-brain"></i> Prescriptive Strategy Engine
                        </h3>
                        <div style={{"marginBottom": "10px", "fontWeight": "600"}}>Objective: <span id="c360-strategy-objective" style={{"color": "#fff"}}>--</span></div>
                        <ul style={{"listStyle": "none", "padding": "0", "margin": "0", "display": "flex", "flexDirection": "column", "gap": "10px"}} id="c360-strategy-steps">
                            {/* Populated via JS */}
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>

    {/* Toast Alerts Container */}
    <div id="toast-container" className="toast-container"></div>

    {/* Controller Scripts */}
    

    </>
  );
}
