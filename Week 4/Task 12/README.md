# Spinal Kyphosis Detector Using Machine Learning

A full-stack web application that predicts whether a patient has Kyphosis (a spinal condition) based on medical inputs, using machine learning. Built with a FastAPI backend and a 3-page HTML/CSS/JavaScript frontend styled with an X-ray-inspired dark theme.

> ⚠️ **Medical Disclaimer:** This application is for educational and demonstration purposes only. It should never be used for actual medical diagnosis or treatment decisions. Always consult a qualified healthcare professional for medical advice.

---

## Overview

This project uses a Decision Tree / Random Forest classifier trained on a 3,000-row synthetic dataset (modeled on real clinical patterns) to predict the presence or absence of kyphosis based on three surgical parameters:

| Feature | Description | Typical Range |
|---|---|---|
| **Age** | Patient age in months | 1 – 210 |
| **Number** | Number of vertebrae involved in surgery | 2 – 10 |
| **Start** | Topmost vertebra level operated on | 1 – 18 |

The frontend has three pages: an educational **Home** page, an interactive **Predict** page, and an **About** page showing live model performance metrics.

---

## Project Structure

```
kyphosis-app/
├── data/
│   └── kyphosis_synthetic_3000.csv   # Training dataset (3,000 records)
├── backend/
│   ├── train_model.py                 # Model training script
│   ├── model.pkl                       # Trained model (generated)
│   ├── metrics.json                     # Saved model metrics (generated)
│   ├── main.py                           # FastAPI server
│   └── requirements.txt                   # Python dependencies
├── frontend/
│   ├── index.html                          # Home / educational page
│   ├── predict.html                         # Prediction tool page
│   ├── about.html                            # About / model metrics page
│   ├── style.css                              # Shared dark/X-ray themed styling
│   ├── script.js                               # Shared frontend logic
│   └── assets/                                  # Diagrams & X-ray images
└── README.md
```

---

## Quick Start

### Prerequisites
- Python 3.8+
- pip
- A modern web browser

### 1. Clone the repository
```bash
git clone <repository-url>
cd kyphosis-app
```
cd D:\projects\spinal-kyphosis-detector-using-machine-learningcd D:\projects\spinal-kyphosis-detector-using-machine-learning
### 2. Install backend dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 3. Train the model
```bash
python train_model.py
```
This generates `model.pkl` and `metrics.json` in the `backend/` folder.

### 4. Start the backend server
```bash
uvicorn main:app --reload --port 8000
```
- API base: `http://localhost:8000`
- Interactive docs: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

### 5. Open the frontend
```bash
cd frontend
python -m http.server 3000
```
Then visit `http://localhost:3000/index.html`.

---

## Using the App

1. **Home** — Learn what kyphosis is, how it happens, who it affects, and see spine/X-ray comparison diagrams.
2. **Predict** — Enter Age, Number of vertebrae, and Start level → get a prediction (Present/Absent) with a confidence score.
3. **About** — See how the project works, the tech stack used, and live model accuracy/precision/recall/F1 metrics.

### Example Inputs

| Age (months) | Number | Start |
|---|---|---|
| 71 | 3 | 5 |
| 158 | 3 | 14 |
| 128 | 4 | 5 |
| 42 | 6 | 11 |

---

## API Reference

| Endpoint | Method | Description |
|---|---|---|
| `/health` | GET | Server health check |
| `/predict` | POST | Returns `{ "prediction": "present"/"absent", "confidence": float }` |
| `/metrics` | GET | Returns saved model accuracy/precision/recall/F1 scores |

**Example request:**
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"age": 71, "number": 3, "start": 5}'
```

---

## Tech Stack

**Backend:** Python · FastAPI · scikit-learn · pandas · joblib
**Frontend:** HTML5 · CSS3 · Vanilla JavaScript
**Model:** Decision Tree Classifier & Random Forest Classifier

---

## Model Performance

Trained on the 3,000-row synthetic dataset with an 80/20 stratified train-test split. Exact figures are available live via the `/metrics` endpoint and on the app's About page.

| Model | Accuracy |
|---|---|
| Decision Tree | ~82% |
| Random Forest | ~82–84% |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| "Model not found" | Run `python train_model.py` before starting the server |
| "Cannot connect to server" | Confirm the backend is running on `localhost:8000` and check CORS settings |
| Metrics not loading on About page | Ensure `metrics.json` was generated and the backend is running |
| Module import errors | Run `pip install -r requirements.txt`; confirm Python 3.8+ |

---

## License

This project is for educational purposes. The dataset is derived from the classic Kyphosis dataset used in machine learning education.

---

**Built for machine learning education — not for clinical use.**