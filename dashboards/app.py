import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt
import base64
import os

# Cargar datos y modelo
df = pd.read_csv('data/dataset.csv')
model = joblib.load('models/model.pkl')
X = df.drop('failure', axis=1)
y = df['failure']

# Predicción para último registro
last_input = X.iloc[[-1]]
pred = model.predict(last_input)[0]
proba = model.predict_proba(last_input)[0][1]

# SHAP
explainer = shap.Explainer(model, X)
shap_values = explainer(X)

# Guardar gráfico SHAP
shap.summary_plot(shap_values, X, show=False)
plt.tight_layout()
shap_path = 'dashboards/shap_summary.png'
plt.savefig(shap_path, bbox_inches='tight')
plt.close()

# Convertir imagen SHAP a base64 para mostrar en dashboard
with open(shap_path, 'rb') as f:
    encoded_image = base64.b64encode(f.read()).decode()

# App Dash
app = dash.Dash(__name__)
app.title = 'Predictive Maintenance Dashboard'

app.layout = html.Div([
    html.H1('🔧 Predictive Maintenance Dashboard', style={'textAlign': 'center'}),

    html.Div([
        html.Div([
            html.H4('Predicción del último registro:'),
            html.P(f'¿Fallará?: {"Sí" if pred == 1 else "No"}'),
            html.P(f'Probabilidad: {proba:.2%}')
        ], style={'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top'}),

        html.Div([
            html.Img(src='data:image/png;base64,{}'.format(encoded_image), style={'width': '100%'})
        ], style={'width': '65%', 'display': 'inline-block', 'paddingLeft': '5%'})
    ]),

    html.Hr(),

    html.H3('📊 Visualización de datos de sensores'),
    dcc.Graph(figure=px.scatter_matrix(df, dimensions=df.columns[:-1], color='failure')),

    html.H3('📄 Tabla de datos'),
    dcc.Graph(figure=px.imshow(df.head(10), text_auto=True))
])

if __name__ == '__main__':
    app.run_server(debug=True)
