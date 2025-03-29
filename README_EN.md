# Predictive Maintenance AI

This project implements a predictive maintenance system using artificial intelligence models, simulated industrial sensor data, and interactive visualization.

## 🧠 Description

This application was developed as part of the thesis **Reverse Engineering in Artificial Intelligence Models for Predictive Maintenance in Industry 4.0**. It simulates industrial sensor data, trains a classification model, and provides interactive dashboards for failure analysis.

## ⚙️ Technologies Used

- Python 3.11
- Scikit-learn
- Pandas / NumPy
- SHAP
- Plotly Dash
- Matplotlib / Seaborn
- Joblib

## 🗂 Project Structure

```
predictive_maintenance_ai/
├── data/                # Simulated sensor data
├── models/              # Trained models
├── dashboards/          # Visualization app (Dash)
├── src/                 # Source code: data generation, training, SHAP
├── anexos/              # Exported charts for documentation
├── setup.py             # Script to run the full project
└── README.md            # This file
```

## 🚀 How to Run

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/predictive-maintenance-ai.git
cd predictive-maintenance-ai
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Run the full pipeline:
```bash
python setup.py
```

This will generate the data, train the model, and launch the interactive dashboard.

## 📊 System Features

- Simulation of industrial sensor conditions
- Failure prediction using Random Forest
- 3D data visualization
- Explainability with SHAP
- Real-time dashboards using Plotly Dash

## 🧩 Context and References

This project was developed as part of a postgraduate research project in Intelligent Manufacturing Engineering, covering topics in Industry 4.0, predictive maintenance, and explainable AI models.
