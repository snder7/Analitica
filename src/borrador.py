# src/main.py
import sys
import os
from jinja2 import Template
import matplotlib.pyplot as plt

# Añadir el directorio raíz del proyecto al path de búsqueda de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_loader import DataLoader
from analysis.data_exploration import DataExplorer
from analysis.descriptive_analysis import DescriptiveAnalysis
from visual.visualization import Visualization
from analysis.data_exploration import DataExplorer
from etl.transform import DataFormatter
from diagnostics.anomaly_detection import AnomalyDetection
from diagnostics.tendencia import TrendAnalysis

# Ruta al archivo de datos
file_path = 'C:/Users/Extreme002/Documents/Xanalitics/data/raw/sensores.csv'


# Cargar los datos
data_loader = DataLoader(file_path)
data = data_loader.load_data()
# Categorizar las variables totales





# Categorizar las variables totales

#Transformar el formato de fecha
data = DataFormatter(data).transform_date('fechareal')

#data = DataFormatter(data).set_index("hora")

df_pivot = data.groupby(["hora", "senal"])["valor"].mean().unstack()

print (df_pivot.columns)
# Mostrar el dataset pivotado
#df_pivot = df_pivot.rename(columns={'FLUJO EN L/S': 'flujo1', 'FLUJO PROMEDIO EN L/S':'flujo_p', 'METROS CÚBICOS TOTALIZADOS':'totalizado', 'PRESIÓN 01':'presion1', 'PRESIÓN 02':'presion2'})

#print("Columnas del DataFrame:", df_pivot.columns)

# Filtrar columnas que contienen las palabras clave 'CAUDAL', 'PRESION' y 'VOLUMEN'
filtro = df_pivot.columns[df_pivot.columns.str.contains('CAUDAL|PRESION|VOLUMEN', case=False)]
df_filtrado = df_pivot[filtro]

print (df_filtrado.columns)


df_pivot = DataFormatter(df_filtrado).data_normalization('VOLUMEN NARANJO')
df_pivot = DataFormatter(df_filtrado).data_normalization('VOLUMEN SENA')
df_pivot = DataFormatter(df_filtrado).data_normalization('VOLUMEN MI CASITA')
df_pivot = DataFormatter(df_filtrado).data_normalization('VOLUMEN SALIDA SALGUERO')
df_pivot = DataFormatter(df_filtrado).data_normalization('VOLUMENLINEA12')
df_filtrado.plot(kind="line", figsize=(10,4), subplots=False)


plt.legend()
plt.show()


#Filtrar columnas
#datos_filtrados = data.loc[data["senal"] == "FLUJO EN L/S"].copy()



explorer = DataExplorer(data)


# Graficar la línea de tiempo
#datos_filtrados.plot(kind="line", y="valor", figsize=(10,4))
plt.show()
#df_filtrado.plot(kind="box", column="CAUDAL MI CASITA", vert=False, patch_artist=True, showfliers=True, figsize=(10,6))

# Mostrar la gráfica



#Analisis de detección de anomalias 



""""
# ---------------------------------------------

for variable in df_filtrado.columns:
    print(f"\nEstadísticas descriptivas para {variable}:")
    print(df_filtrado[variable].describe())


for variable in df_filtrado.columns:
    plt.figure(figsize=(10, 6))
    plt.hist(df_filtrado[variable], bins=20, edgecolor="black", alpha=0.7)
    plt.title(f"Distribución de frecuencia de {variable}")
    plt.xlabel(variable)
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.show()

import seaborn as sns

for variable in df_filtrado.columns:
    sns.kdeplot(df_filtrado[variable], fill=True, alpha=0.7)
    plt.title(f"Densidad de probabilidad de {variable}")
    plt.xlabel(variable)
    plt.ylabel("Densidad")
    plt.grid(True)
    plt.show()
"""

viz = Visualization(df_filtrado)

"""
# Diagnostico___________Anomalia
ad = AnomalyDetection(df_filtrado, df_filtrado.columns)
ad.calculate_statistics()
ad.detect_anomalies_zscore()
ad.detect_anomalies_iqr()
ad.detect_anomalies_isolation_forest()
#-------------FIM----------------------
"""



""""
 # Análisis de tendencias
trend_analysis = TrendAnalysis(df_filtrado)
trend_analysis.adf_test()
trend_analysis.exponential_smoothing()
trend_analysis.holt_winters()
trend_analysis.linear_regression()
trend_analysis.ridge_regression()
trend_analysis.lasso_regression()
"""
# Visualize distribution for each variable (caudal, presion, volumen)

""""
for variable in df_filtrado.columns:
    # Option 1: Histogram (consider log transformation if necessary)
    viz.plot_histogram(variable, save_path=f"{variable}_histogram.png")  # Optional: Save to file

    # Option 2: Kernel Density Estimation (KDE)
    viz.plot_distribution(variable, log_transform=False, save_path=f"{variable}_kde.png")  # Optional: Save to file

# Scatter plots for all variable pairs
for i, variable1 in enumerate(df_filtrado.columns):
    for j, variable2 in enumerate(df_filtrado.columns):
        if i != j:  # Avoid self-comparisons
            viz.plot_scatter(variable1, variable2, save_path=f"{variable1}_vs_{variable2}_scatter.png")  # Optional: Save to file

# Correlation heatmap (excluding optional columns)
exclude_columns = []  # List any columns you want to exclude (e.g., timestamps)
viz.plot_correlation_heatmap(exclude_columns=exclude_columns, save_path="correlation_heatmap.png")  # Optional: Save to file

    
"""




#visualization.plot_histogram('variable', save_path=histogram_path)
#_______ Analisis estadisticos ____________________

# Calcular la matriz de correlación
#print(explorer.correlation_matrix(['valor', 'rvalor']))

# Plot de regresión para 'engine-size' y 'price'
#explorer.plot_regression(x='valor', y='rvalor')


""" senales= data['senal'].unique()

print (senales)


datos_filtrados = data.loc[data["senal"] == "FLUJO EN L/S"].copy()



df = datos_filtrados


# Análisis descriptivo
analysis = DescriptiveAnalysis(datos_filtrados)



mean, median, mode = analysis.calculate_central_tendency('valor')
range_value, variance, std_dev = analysis.calculate_dispersion('valor')
skewness = analysis.calculate_skewness('valor')
kurtosis = analysis.calculate_kurtosis('valor')
mean, std_dev, skewness, kurtosis, distribution = analysis.analyze_distribution('valor')
iqr = analysis.calculate_interquartile_range('valor')
#correlation = analysis.calculate_correlation('valor', 'rvalor')

# Descripción del DataFrame

# Uso del módulo

# Cargar datos


# Crear una instancia de DataExplorer
explorer = DataExplorer(df)




#_______ Analisis estadisticos ____________________

# Calcular la matriz de correlación
#print(explorer.correlation_matrix(['valor', 'rvalor']))

# Plot de regresión para 'engine-size' y 'price'
#explorer.plot_regression(x='valor', y='rvalor')

# Mostrar la correlación entre 'engine-size' y 'price'
#print(explorer.correlation_matrix(['valor', 'rvalor']))

# Box plot para 'body-style' y 'price'
#explorer.plot_box(x='valor', y='rvalor')



# Conteo de valores de 'drive-wheels'
#print(explorer.value_counts('valor'))

# Agrupar datos por 'drive-wheels' y calcular la media del precio
#grouped_data = explorer.group_by(by='senal', columns=['valor'])
#print(grouped_data)

# Crear tabla dinámica
#pivot_table = explorer.create_pivot_table(index='senal', columns='valor', values='rvalor')
#print(pivot_table)

# Plot del heatmap de la tabla dinámica
#explorer.plot_heatmap(pivot_table)

# Calcular y mostrar la correlación de Pearson entre 'wheel-base' y 'price'
#explorer.plot_pearson_correlation('valor', 'rvalor')
#_________________________________________Analisis__________




print(explorer.info)

# Crear visualizaciones y guardar como imágenes
visualization = Visualization(data)
histogram_path = 'histogram.png'
boxplot_path = 'boxplot.png'
violinplot_path = 'violinplot.png'
scatter_path = 'scatter.png'
heatmap_path = 'heatmap.png'
dist_path = 'dist.png'
log_dist_path = 'log_dist.png'
pie_chart_path = 'pie_chart.png'

visualization.plot_histogram('variable', save_path=histogram_path)
visualization.plot_boxplot('valor', save_path=boxplot_path)
visualization.plot_violinplot('valor', save_path=violinplot_path)
visualization.plot_scatter('valor', 'rvalor', save_path=scatter_path)
#visualization.plot_correlation_heatmap(exclude_columns=['revenue', 'City Group', 'Type'], save_path=heatmap_path)
visualization.plot_distribution('rvalor', log_transform=False, save_path=dist_path)
visualization.plot_distribution('rvalor', log_transform=True, save_path=log_dist_path)
visualization.plot_pie_chart('variable', save_path=pie_chart_path)

# Generar el informe HTML
with open('template.html', 'r') as file:
    template = Template(file.read())

html_content = template.render(
    title="Data Analysis Report",
    mean=mean,
    median=median,
    mode=mode,
    range_value=range_value,
    variance=variance,
    std_dev=std_dev,
    skewness=skewness,
    kurtosis=kurtosis,
    iqr=iqr,
    #correlation=correlation,
    #info_data=explorer.info,
    describe_data=explorer.describe_data(),
    head_data=explorer.show_head(),
    histogram=histogram_path,
    boxplot=boxplot_path,
    violinplot=violinplot_path,
    scatter=scatter_path,
    heatmap=heatmap_path,
    dist=dist_path,
    log_dist=log_dist_path,
    pie_chart=pie_chart_path
)

with open('report.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("Report generated: report.html")"""



## visualizar 

# Definir el rango de fechas para el mes de mayo de 2024
start_date = pd.to_datetime('2024-05-01').date()
end_date = pd.to_datetime('2024-05-31').date()

# Filtrar las descripciones específicas
keywords = ['VOLUMEN']

# Iterar sobre cada día del mes
for single_date in pd.date_range(start=start_date, end=end_date):
    # Filtrar los datos para el día actual
    day_data = data[data['fecha'] == single_date.date()]
    
    if day_data.empty:
        continue  # Saltar los días sin datos
    
    # Transponer el dataset
    df_pivot = day_data.groupby(["hora", "DESCRIPTION"])["VALUE"].mean().unstack()
    print ("aqui")
    # Aplicar el filtro de columnas
    filtro = df_pivot.columns[df_pivot.columns.str.contains('|'.join(keywords), case=False)]
    df_bomba2 = df_pivot[filtro]

    # Plotear los datos
    #print(df_bomba2)
    #df_bomba2.plot(kind="line", figsize=(10, 4), subplots=False, title=f"Data for {single_date.date()}")
   

#plt.show()




# Gráfica de volumen por día 


keywords = ['VOLUMEN']
df_filtrado = data[data['DESCRIPTION'].str.contains('volumen', case=False)]

# Filtrar las columnas de volumen
volumen_columns = ['DESCRIPTION', 'VALUE', 'fecha', 'hora']

# Filtrar el dataframe para solo tener las columnas necesarias
df_filtrado = df_filtrado[volumen_columns]


# Agrupar por día y descripción para calcular la diferencia acumulada diaria
daily_volumes = df_filtrado.groupby(['fecha', 'DESCRIPTION']).agg(
    start_value=('VALUE', 'first'),
    end_value=('VALUE', 'last')
).reset_index()

# Calcular el volumen diario
daily_volumes['daily_volume'] = daily_volumes['end_value'] - daily_volumes['start_value']

# Solo seleccionar las columnas relevantes
daily_volumes = daily_volumes[['fecha', 'DESCRIPTION', 'daily_volume']]

# Pivotar los datos para que cada descripción sea una columna
df_pivot = daily_volumes.pivot(index='fecha', columns='DESCRIPTION', values='daily_volume')

# Crear un gráfico de barras para cada descripción


# Plotear los datos
df_pivot.plot(kind='bar')



# Mostrar el g
plt.show()