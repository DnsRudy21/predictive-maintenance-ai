# Predictive Maintenance AI

Este proyecto implementa un sistema de mantenimiento predictivo utilizando modelos de inteligencia artificial, simulación de datos industriales y visualización interactiva.

## 🧠 Descripción

Aplicación desarrollada para la tesis **Ingeniería Inversa en Modelos de Inteligencia Artificial para el Mantenimiento Predictivo en la Industria 4.0**, la cual simula datos de sensores industriales, entrena un modelo de clasificación y presenta dashboards interactivos para análisis de fallas.

## ⚙️ Tecnologías utilizadas

- Python 3.11
- Scikit-learn
- Pandas / NumPy
- SHAP
- Plotly Dash
- Matplotlib / Seaborn
- Joblib

## 🗂 Estructura del proyecto

```
predictive_maintenance_ai/
├── data/                # Datos simulados
├── models/              # Modelos entrenados
├── dashboards/          # App de visualización (Dash)
├── src/                 # Código fuente: generación, entrenamiento, SHAP
├── anexos/              # Gráficas exportadas para documentación
├── setup.py             # Script para ejecutar el proyecto completo
└── README.md            # Este archivo
```

## 🚀 Instrucciones de ejecución

1. Clona este repositorio:
```bash
git clone https://github.com/TU_USUARIO/predictive-maintenance-ai.git
cd predictive-maintenance-ai
```

2. Instala dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta el proyecto:
```bash
python setup.py
```

Esto generará los datos, entrenará el modelo y lanzará el dashboard interactivo.

## 📊 Funcionalidades del sistema

- Simulación de condiciones de sensores industriales
- Predicción de fallas mediante Random Forest
- Visualización 3D de datos
- Explicabilidad con SHAP
- Dashboards en tiempo real con Plotly Dash

## 🧩 Referencias y contexto

Este proyecto fue desarrollado como parte de un trabajo de investigación para una maestría en Ingeniería para la Manufactura Inteligente, abordando temas de Industria 4.0, mantenimiento predictivo y modelos explicables.
