import pandas as pd
import ydata_profiling as profile

# Datos de prueba
data = {
    'Age': [25, 30, 22, 35, 40, 28, 33, 27, 29, 31],
    'Height': [175, 160, 180, 165, 170, 158, 172, 155, 168, 163],
    'Weight': [70, 55, 80, 65, 75, 52, 68, 54, 62, 60],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Income': [50000, 60000, 45000, 70000, 80000, 55000, 65000, 48000, 59000, 62000]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Guardar en un archivo CSV
df.to_csv('your_data_file.csv', index=False)

# cargar datos
df2 = pd.read_csv('sensores.csv')

profile = profile.ProfileReport(df2, title='Informe de perfilado de tips')

# Muestra el informe en la consola
#print(profile.to_string())

# Guarda el informe en un archivo HTML
profile.to_file('resume.html')