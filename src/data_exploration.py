# src/data_exploration.py
import pandas as pd
import io

class DataExploration:
    def __init__(self, data):
        self.data = data
        self.info_data = None
        self.describe_data = None
        self.head_data = None

    def explore_data(self):
        # Captura la salida de data.info() en un StringIO buffer
        buffer = io.StringIO()
        self.data.info(buf=buffer)
        self.info_data = buffer.getvalue()
        buffer.close()

        # Captura la salida de data.describe() y data.head()
        self.describe_data = self.data.describe().round(2).transpose().to_dict()
        self.head_data = self.data.head().to_dict(orient='records')

  
