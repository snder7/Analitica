import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

class DataExplorer:
    def __init__(self, df):
        self.df = df

    def show_head(self, n=5):
        return self.df.head(n)

    def show_data_types(self):
        return self.df.dtypes
    

   

    def correlation_matrix(self, columns):
        return self.df[columns].corr()

    def plot_regression(self, x, y):
        sns.regplot(x=x, y=y, data=self.df)
        plt.ylim(0,)
        plt.show()

    def plot_box(self, x, y):
        sns.boxplot(x=x, y=y, data=self.df)
        plt.show()

    def describe_data(self, include=None):
        return self.df.describe(include=include)

    
    def info(self, include=None):
        return self.df.info(include=include)

    def value_counts(self, column):
        return self.df[column].value_counts().to_frame()

    def group_by(self, by, columns, aggfunc='mean'):
        return self.df.groupby(by)[columns].agg(aggfunc).reset_index()

    def create_pivot_table(self, index, columns, values, aggfunc='mean', fill_value=0):
        pivot = self.df.pivot_table(index=index, columns=columns, values=values, aggfunc=aggfunc, fill_value=fill_value)
        return pivot

    def plot_heatmap(self, pivot, cmap='RdBu'):
        plt.pcolor(pivot, cmap=cmap)
        plt.colorbar()
        plt.show()

    def plot_pearson_correlation(self, column1, column2):
        pearson_coef, p_value = stats.pearsonr(self.df[column1], self.df[column2])
        print(f"The Pearson Correlation Coefficient between {column1} and {column2} is {pearson_coef} with a P-value of P = {p_value}")
        return pearson_coef, p_value
    




    def plot_correlation_matrix(self, annot=True, figsize=(10, 10)):
        # Calcular la matriz de correlación
        
        corr = self.df.values

        # Calcula la matriz de correlación
        corr = np.corrcoef(corr.T)

# Crear heatmap
        sns.heatmap(corr, xticklabels=self.df.columns, yticklabels=self.df.columns, cmap='coolwarm')


