import shap
import pandas as pd
import joblib

model = joblib.load('models/model.pkl')
data = pd.read_csv('data/dataset.csv').drop('failure', axis=1)
explainer = shap.Explainer(model, data)
shap_values = explainer(data)
shap.plots.beeswarm(shap_values)
