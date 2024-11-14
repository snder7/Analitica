import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from jinja2 import Template

# Paso 1: Generar datos y gráficos
datos = pd.DataFrame({
    'fechareal': pd.date_range(start='2024-01-01', periods=100, freq='D'),
    'pct': np.random.randn(100)  # Genera datos aleatorios para la columna 'pct'
})

datos['fechareal'] = pd.to_datetime(datos['fechareal'])
datos.set_index('fechareal', inplace=True)

plt.figure(figsize=(10, 6))
plt.plot(datos.index, datos['pct'], label='PCT')
plt.title('Gráfico de PCT')
plt.xlabel('Fecha')
plt.ylabel('PCT')
plt.legend()
plt.savefig('plot.png')
plt.close()

# Paso 2: Crear y leer la plantilla HTML
template_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Reporte de Análisis</title>
</head>
<body>
    <h1>Reporte de Análisis</h1>
    <h2>Tabla de Datos</h2>
    {{ table }}

    <h2>Gráfico de PCT</h2>
    <img src="plot.png" alt="Gráfico de PCT">

</body>
</html>
"""

template = Template(template_html)

# Convertir el DataFrame a HTML
table_html = datos.to_html()

# Rellenar la plantilla con la tabla y la imagen
reporte_html = template.render(table=table_html)

# Guardar el reporte como un archivo HTML
with open('reporte.html', 'w') as file:
    file.write(reporte_html)

print("Reporte generado: reporte.html")
