import pandas as pd
import numpy as np

def generate_sensor_data(num_samples=1000):
    np.random.seed(42)
    data = {
        'temperature': np.random.normal(75, 10, num_samples),
        'vibration': np.random.normal(0.5, 0.1, num_samples),
        'pressure': np.random.normal(30, 5, num_samples),
        'operating_hours': np.random.randint(100, 10000, num_samples),
        'failure': np.random.choice([0, 1], size=num_samples, p=[0.9, 0.1])
    }
    return pd.DataFrame(data)

if __name__ == '__main__':
    df = generate_sensor_data()
    df.to_csv('data/dataset.csv', index=False)
