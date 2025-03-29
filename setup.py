import os
import subprocess

# Crear carpetas necesarias
os.makedirs("data", exist_ok=True)
os.makedirs("models", exist_ok=True)

print("🔧 Generando dataset...")
subprocess.run(["python", "src/generate_data.py"], check=True)

print("📊 Entrenando modelo...")
subprocess.run(["python", "src/train_model.py"], check=True)

print("🚀 Ejecutando dashboard con Dash...")
subprocess.run(["python", "dashboards/app.py"])
