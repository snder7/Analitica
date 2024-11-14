from sqlalchemy import create_engine
import pandas as pd

def load_data(df):
    engine = create_engine('postgresql://usuario:contraseña@host:puerto/base_de_datos_destino')
    df.to_sql('tabla_transformada', engine, if_exists='replace')
