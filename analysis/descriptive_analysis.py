# analysis/descriptive_analysis.py
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

class DescriptiveAnalysis:
    def __init__(self, data):
        self.data = data

    def calculate_central_tendency(self, variable):
        mean = self.data[variable].mean()
        median = self.data[variable].median()
        mode = self.data[variable].mode()
        return mean, median, mode

    def calculate_dispersion(self, variable):
        range_value = self.data[variable].max() - self.data[variable].min()
        variance = self.data[variable].var()
        std_dev = self.data[variable].std()
        return range_value, variance, std_dev

    def calculate_skewness(self, variable):
        return stats.skew(self.data[variable])

    def calculate_kurtosis(self, variable):
        return stats.kurtosis(self.data[variable])

    def analyze_distribution(self, variable):
        mean = self.data[variable].mean()
        std_dev = self.data[variable].std()
        skewness = stats.skew(self.data[variable])
        kurtosis = stats.kurtosis(self.data[variable])

        if skewness > 0:
            distribution = "Distribución asimétrica a la derecha"
        elif skewness < 0:
            distribution = "Distribución asimétrica a la izquierda"
        else:
            distribution = "Distribución simétrica"

        return mean, std_dev, skewness, kurtosis, distribution

    def calculate_interquartile_range(self, variable):
        q1 = self.data[variable].quantile(0.25)
        q3 = self.data[variable].quantile(0.75)
        iqr = q3 - q1
        return iqr

    def calculate_correlation(self, variable1, variable2):
        correlation = stats.pearsonr(self.data[variable1], self.data[variable2])[0]
        return correlation

    def analyze_relationships(self, variable1, variable2):
        if self.data[variable1].dtype.kind in 'bifc' and self.data[variable2].dtype.kind in 'bifc':
            correlation = stats.pearsonr(self.data[variable1], self.data[variable2])
            print(f"Correlación entre {variable1} y {variable2}: {correlation}")

        elif self.data[variable1].dtype.kind in 'O' and self.data[variable2].dtype.kind in 'O':
            contingency_table = pd.crosstab(self.data[variable1], self.data[variable2])
            print(contingency_table)

            chi2, p_value, _, _ = stats.chi2_contingency(contingency_table)
            if p_value < 0.05:
                print("Existe una dependencia estadísticamente significativa entre las variables.")
            else:
                print("No existe una dependencia estadísticamente significativa entre las variables.")

        plt.scatter(self.data[variable1], self.data[variable2])
        plt.title(f"Relación entre {variable1} y {variable2}")
        plt.xlabel(variable1)
        plt.ylabel(variable2)
        plt.show()
