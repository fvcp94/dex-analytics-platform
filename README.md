# DEX Intelligence Platform  
**Digital Employee Experience (DEX) Analytics | Streamlit + GenAI (OpenRouter)**

An **end‑to‑end Digital Employee Experience (DEX) analytics platform** that demonstrates how modern Digital Workplace and IT Service Governance teams can **measure, analyze, and improve employee productivity and system reliability** using analytics, machine learning, and GenAI.

This project is built as a **portfolio‑grade, enterprise‑style internal product**, inspired by real‑world DEX platforms used by large organizations.

> ⚠️ **Data disclaimer:** All data is **synthetic** and generated at runtime for demonstration purposes only. No real employee, endpoint, or enterprise data is used.

---

## 🚀 What This Platform Does

### 📊 Executive DEX Scoreboard
- Computes a **DEX Score (0–100)** per day from:
  - Application latency  
  - Login performance  
  - Crash rate  
  - Device health  
- Tracks ticket volume, MTTR, and impacted users
- Filters by **region** and **persona** (enterprise-ready views)

### 🔍 Digital Workplace Health Analytics
- Trend monitoring for:
  - App latency
  - Login time
  - Crash rate
  - Device health
- Designed for IT Operations & Service Governance teams

### 🚨 Anomaly Detection
- Rolling **z‑score anomaly detection** on curated KPIs
- Identifies experience regressions after:
  - Patches
  - Upgrades
  - Configuration changes
- Enables **proactive incident prevention**

### 🎫 Ticket Intelligence (ITSM‑style)
- Synthetic ServiceNow‑like incident data
- Ticket volume, priority mix, and MTTR analysis
- Identification of top recurring friction points

### 🤖 AI Insights (GenAI via OpenRouter)
- LLM‑assisted explanations for detected anomalies
- Evidence‑based summaries using:
  - Aggregated KPI windows
  - Nearby change events
- Guardrails applied:
  - No raw endpoint‑level data
  - No autonomous remediation
  - Human‑in‑the‑loop recommendations only

---

## 🧠 Architecture Overview

```
Synthetic Data Generation
        ↓
Curated Metrics & DEX Scoring
        ↓
Statistical Analysis & Anomaly Detection
        ↓
Streamlit Dashboards
        ↓
GenAI Explanation Layer (OpenRouter)
```

**Design Principles**
- Deterministic analytics first (metrics & statistics)
- GenAI used strictly for **explainability and summarization**
- Privacy‑by‑design (cohort‑level insights, no PII)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI & deployment)
- **Pandas / NumPy**
- **Plotly**
- **scikit‑learn**
- **OpenRouter (LLMs)**
- **Parquet** (columnar storage)

---

## 📂 Project Structure

```
dex-analytics-platform/
│
├── streamlit_app/
│   ├── app.py                  # Executive dashboard
│   └── pages/
│       ├── 3_Anomaly_Detection.py
│       ├── 4_Ticket_Intelligence.py
│       └── 5_AI_Insights.py
│
├── src/
│   ├── data_gen.py             # Synthetic DEX + ITSM data generator
│   ├── bootstrap_data.py       # Auto‑generate data on first run
│   ├── metrics.py              # DEX KPI calculations
│   ├── anomaly.py              # Anomaly detection logic
│   ├── llm_openrouter.py       # OpenRouter GenAI client
│   └── io.py                   # Data I/O helpers
│
├── data/
│   └── processed/              # Auto‑generated demo data
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Run Locally

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run streamlit_app/app.py
```

The app automatically generates synthetic demo data on first run.

---

## ☁️ Deploy on Streamlit Community Cloud

Use the following settings:

- **Repository:** `fvcp94/dex-analytics-platform`
- **Branch:** `main`
- **Main file path:** `streamlit_app/app.py`

No database or manual setup required.

---

## 🔐 Enable GenAI (Optional)

### Local
Create `.streamlit/secrets.toml`:
```toml
[openrouter]
api_key = "YOUR_OPENROUTER_API_KEY"
model = "openai/gpt-4o-mini"
```

### Streamlit Cloud
App → **Settings → Secrets**
```toml
[openrouter]
api_key = "YOUR_OPENROUTER_API_KEY"
model = "openai/gpt-4o-mini"
```

Save and reboot the app.

---

## 🎯 Use Cases Demonstrated
- Digital Workplace analytics
- DEX service governance
- Proactive IT operations
- Incident trend analysis
- Change impact detection
- GenAI‑assisted IT decision support

---

## 📌 Future Enhancements
- NLP‑based ticket clustering
- Incident forecasting & capacity planning
- Runbook‑driven remediation recommendations
- Role‑based access control
- ServiceNow / Splunk connectors
- GenAI tool‑calling (Copilot‑style)

---

## 👤 Author

**Febin Varghese**  
Senior Data Scientist | Digital Workplace Analytics | AI / ML
