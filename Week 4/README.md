# Week 4 — End-to-End Project & Model Deployment

**Project Title:** End-to-End Data Science Project Development & Model Deployment

##  Overview
The final week brought everything together: a complete end-to-end ML project — the
**Spinal Kyphosis Detector** — built as a full-stack web application, with the
trained model deployed as a live API.

##  Tasks

| Task | Focus |
|------|-------|
| [Task 12](./Task-12) | End-to-End ML Project on Real-World Dataset — Spinal Kyphosis Detector |

### Task 12 — End-to-End ML Project: Spinal Kyphosis Detector
- Built a full-stack web app predicting **Kyphosis** (a spinal condition) from
  medical inputs, using a **FastAPI** backend and a 3-page HTML/CSS/JavaScript
  frontend with an X-ray-inspired dark theme
- Trained a **Decision Tree** and **Random Forest** classifier on a 3,000-row
  synthetic dataset (modeled on real clinical patterns), using three surgical
  parameters: `Age`, `Number` of vertebrae, and `Start` level
- Achieved **~82% (Decision Tree)** and **~82–84% (Random Forest)** accuracy on an
  80/20 stratified train-test split
- Built three frontend pages: an educational **Home** page, an interactive
  **Predict** page (live prediction + confidence score), and an **About** page
  showing live model metrics
- Deployed the trained model as a REST API with FastAPI:
  - `GET /health` — server health check
  - `POST /predict` — returns prediction + confidence score
  - `GET /metrics` — returns live accuracy/precision/recall/F1 scores
  - Interactive API docs auto-generated at `/docs`

##  Tools & Libraries
Python, FastAPI, Scikit-learn, Pandas, joblib, HTML5, CSS3, Vanilla JavaScript,
Git/GitHub

##  Internship Summary & Key Learnings
1. Gained hands-on experience in data cleaning, EDA, and visualization across
   multiple datasets
2. Learned and applied supervised and unsupervised ML algorithms using Scikit-learn
3. Built interactive Power BI dashboards and performed web scraping using Python
4. Successfully developed and deployed a full-stack, end-to-end ML project (FastAPI
   backend + HTML/CSS/JS frontend)

##  References
1. FastAPI Documentation (fastapi.tiangolo.com)
2. Scikit-learn & Pandas Documentation
3. Classic Kyphosis Dataset — basis for the synthetic dataset used in Task 12
4. Google Colab, Jupyter Notebook

---
⚠️ **Medical Disclaimer:** The Task 12 application is for educational and
demonstration purposes only. It should never be used for actual medical diagnosis or
treatment decisions.
