# src/main.py
import sys
import os
from jinja2 import Template
import matplotlib.pyplot as plt

# Añadir el directorio raíz del proyecto al path de búsqueda de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#-------Cargue de librías propas-------
from data_loader import DataLoader
from analysis.data_exploration import DataExplorer
from analysis.descriptive_analysis import DescriptiveAnalysis
from visual.visualization import Visualization
from analysis.data_exploration import DataExplorer
from etl.transform import DataFormatter
from diagnostics.anomaly_detection import AnomalyDetection
from diagnostics.tendencia import TrendAnalysis
#---------------FIN---------------------


# Ruta al archivo de datos
file_path = 'C:/Users/Extreme002/Documents/Xanalitics/data/raw/sensores.csv'


# Cargar los datos
data_loader = DataLoader(file_path)
data = data_loader.load_data()
# ----------------------------------------------
import pandas as pd

#--------------Tratamiento de datos------------
data = DataFormatter(data).transform_date('datetime')

start_date = pd.to_datetime('2024-05-01').date()
day_data = data[data['fecha'] == start_date]



df_pivot = day_data.groupby(["hora", "DESCRIPTION"])["VALUE"].mean().unstack()

filtro = df_pivot.columns[df_pivot.columns.str.contains('Corredor|Bomba 3', case=False)]
df_filtrado = df_pivot[filtro]



caudal_column = 'Caudal salid corredor turistico en  [l/s]'
presion_column = 'Presion bomba 3 en  [PSI]'

# Asegúrate de que las columnas sean del tipo numérico
df_filtrado[caudal_column] = pd.to_numeric(df_filtrado[caudal_column], errors='coerce')
df_filtrado[presion_column] = pd.to_numeric(df_filtrado[presion_column], errors='coerce')

# Eliminar filas con valores NaN en las columnas relevantes
df_filtered = df_filtrado.dropna(subset=[caudal_column, presion_column])

print(df_filtered)

# Crear la gráfica de dispersión (scatter plot)
plt.figure(figsize=(10, 6))
plt.scatter(df_filtered[caudal_column], df_filtered[presion_column], alpha=0.5)

# Configurar etiquetas y título
plt.xlabel('Caudal (l/s)')
plt.ylabel('Presión (PSI)')
plt.title('Caudal vs Presión')
plt.grid(True)

# Mostrar la gráfica
plt.show()

import seaborn as sns

# Calcular la matriz de correlación
corr_matrix = df_filtered.corr()

# Crear un mapa de calor para visualizar la matriz de correlación
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlación')
plt.show()




# Graficar las variables a lo largo del tiempo
plt.figure(figsize=(14, 7))
df_filtered['Caudal salid corredor turistico en  [l/s]'].plot(label='Caudal (l/s)')
df_filtered['Presion bomba 3 en  [PSI]'].plot(label='Presión (PSI)')
plt.title('Caudal y Presión a lo Largo del Tiempo')
plt.xlabel('Fecha y Hora')
plt.ylabel('Valores')
plt.legend()
plt.show()


# Distribución de caudal
plt.figure(figsize=(12, 6))
sns.histplot(df_filtered['Caudal salid corredor turistico en  [l/s]'], bins=50, kde=True)
plt.title('Distribución del Caudal')
plt.xlabel('Caudal (l/s)')
plt.ylabel('Frecuencia')
plt.show()

# Distribución de presión
plt.figure(figsize=(12, 6))
sns.histplot(df_filtered['Presion bomba 3 en  [PSI]'], bins=50, kde=True)
plt.title('Distribución de la Presión')
plt.xlabel('Presión (PSI)')
plt.ylabel('Frecuencia')
plt.show()


from statsmodels.tsa.seasonal import seasonal_decompose

# Suponiendo que 'datetime' es el índice del DataFrame
result = seasonal_decompose(df_filtered['Caudal salid corredor turistico en  [l/s]'], model='additive', period=24)
result.plot()
plt.show()

result = seasonal_decompose(df_filtered['Presion bomba 3 en  [PSI]'], model='additive', period=24)
result.plot()
plt.show()

from scipy import stats

# Detección de outliers en caudal
z_scores = stats.zscore(df_filtered['Caudal salid corredor turistico en  [l/s]'])
outliers = df_filtered[z_scores > 3]

print("Outliers en Caudal:")
print(outliers)

# Detección de outliers en presión
z_scores = stats.zscore(df_filtered['Presion bomba 3 en  [PSI]'])
outliers = df_filtered[z_scores > 3]

print("Outliers en Presión:")
print(outliers)
