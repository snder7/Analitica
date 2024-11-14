import pandas as pd
import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import matplotlib.pyplot as plt
import seaborn as sns
from apscheduler.schedulers.blocking import BlockingScheduler

#import pyodbc
#print(pyodbc.drivers())

# Configuración de la conexión
server = 'xreportsdb.ctydtimai6ew.us-east-2.rds.amazonaws.com'  # Nombre del servidor
database = 'xreports'  # Nombre de la base de datos
username = 'scantillo'  # Tu nombre de usuario
password = 'Extreme2024**'  # Tu contraseña




import pyodbc

# Construcción de la cadena de conexión
connection_string = (
    'DRIVER={ODBC Driver 18 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
    'TrustServerCertificate=yes;'
)

# Prueba la conexión directa con pyodbc
try:
    # Conectar a la base de datos
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    
    # Ejecutar la consulta
    query = "SELECT  fechareal, senal, variable , valor, tvalor, rvalor, unidad  FROM vwDatos vd WHERE vd.idestacion = 190117 and  CAST(vd.fechareal AS DATE) = CAST(GETDATE() AS DATE);"
    query_mes  = """
    SELECT
        d.datetime,
        CONCAT(s.descripcion, ' en ', ' [', v.unidad, ']') AS DESCRIPTION,
        d.value AS VALUE,
        v.unidad AS UNIT,
        xe.descripcion AS STATION
    FROM 
        xtdatos d
    LEFT OUTER JOIN 
        xtFallas f ON (f.idsenal = d.idsenal 
                        AND f.restringirdatos = 'SI'
                        AND d.datetime BETWEEN f.fechadesde AND f.fechahasta 
                        AND f.idsenal IS NULL)
    INNER JOIN 
        xtsenales s ON (d.idsenal = s.idsenal)
    INNER JOIN 
        xtEstaciones xe ON (xe.idestacion = s.idestacion)
    INNER JOIN 
        xtvariables v ON (s.idvariable = v.idvariable)
    WHERE 
        MONTH(d.datetime) = MONTH(DATEADD(MONTH, -1, GETDATE()))
        AND YEAR(d.datetime) = YEAR(DATEADD(MONTH, -1, GETDATE()))
        AND d.value NOT IN (SELECT valor FROM xtParametros WHERE parametro = 'I' OR parametro = 'I2')
        AND xe.descripcion  ='EBAP GAIRA'
    ORDER BY 
        d.datetime;
"""
    cursor.execute(query_mes)
    
    # Obtener los datos y las columnas
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    
    # Convertir las filas a una lista de listas en lugar de lista de tuplas
    data = [list(row) for row in rows]
    
    # Crear el DataFrame con los datos y columnas
    df = pd.DataFrame(data, columns=columns)
    df.to_csv('C:/Users/Extreme002/Documents/Xanalitics/data/raw/sensores.csv', index=False)

    # Imprimir las primeras filas del DataFrame
    print(df.head())
    
    # Cerrar la conexión
    conn.close()
except Exception as e:
    print("Error durante la conexión:", e)