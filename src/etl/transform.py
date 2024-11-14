import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataLoader:
    def __init__(self, file_name, headers):
        self.df = pd.read_csv(file_name, names=headers)

    def show_head(self, n=5):
        return self.df.head(n)

    def get_data(self):
        return self.df


class MissingValueHandler:
    def __init__(self, df, columns_with_mean, column_with_mode, columns_to_dropna):
        self.df = df
        self.columns_with_mean = columns_with_mean
        self.column_with_mode = column_with_mode
        self.columns_to_dropna = columns_to_dropna

    def handle_missing_values(self):
        # Reemplazar "?" por NaN
        self.df.replace("?", np.nan, inplace=True)

        # Reemplazar valores faltantes con la media
        for column in self.columns_with_mean:
            avg = self.df[column].astype("float").mean(axis=0)
            self.df[column] = self.df[column].replace(np.nan, avg)
        
        # Reemplazar valores faltantes con el modo
        if self.column_with_mode:
            most_frequent = self.df[self.column_with_mode].value_counts().idxmax()
            self.df[self.column_with_mode] = self.df[self.column_with_mode].replace(np.nan, most_frequent)

        # Eliminar filas con NaN en las columnas especificadas y resetear el índice
        self.df.dropna(subset=self.columns_to_dropna, axis=0, inplace=True)
        self.df.reset_index(drop=True, inplace=True)

        return self.df


class DataFormatter:
    def __init__(self, df):
        self.df = df

    def correct_data_format(self, columns_types):
        for columns, dtype in columns_types.items():
            for column in columns:
                self.df[column] = self.df[column].astype(dtype)
        return self.df

    def data_standardization(self, mpg_columns):
        for col in mpg_columns:
            new_col = col.replace("mpg", "L/100km")
            self.df[new_col] = 235 / self.df[col]
        return self.df

    def data_normalization(self, column):
        # Verificar que la columna existe en el DataFrame
        if column in self.df.columns:
            self.df[column] = self.df[column] / self.df[column].max()
        else:
            print(f"La columna '{column}' no existe en el DataFrame")
        return self.df
    
    def transform_date(self, column_name):
        
        self.df['datetime'] = pd.to_datetime(self.df['datetime'])

        self.df['date'] = pd.to_datetime(self.df['datetime'])
        self.df['fecha'] = self.df['datetime'].dt.date
        self.df['hora'] = self.df['datetime'].dt.time
        self.df = self.df.drop(column_name, axis=1)
        return self.df
    
    def set_index(self, column_name):
        self.df.set_index(column_name, inplace=True)
        return self.df


class DataBinning:
    def __init__(self, df):
        self.df = df

    def binning(self, column, bins, group_names):
        self.df[column] = self.df[column].astype(int, copy=True)
        self.df[column + '-binned'] = pd.cut(self.df[column], bins, labels=group_names, include_lowest=True)
        return self.df

    def plot_histogram(self, column, bins):
        plt.hist(self.df[column], bins=bins)
        plt.xlabel(column)
        plt.ylabel("count")
        plt.title(f"{column} bins")
        plt.show()


class IndicatorVariableCreator:
    def __init__(self, df):
        self.df = df

    def create_indicator_variables(self, columns):
        for column in columns:
            dummies = pd.get_dummies(self.df[column], prefix=column)
            self.df = pd.concat([self.df, dummies], axis=1)
            self.df.drop(column, axis=1, inplace=True)
        return self.df


