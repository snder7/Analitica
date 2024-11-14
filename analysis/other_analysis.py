# analysis/other_analysis.py
import pandas as pd
from scipy import stats

class OtherAnalysis:
    def __init__(self, data):
        self.data = data

    def calculate_correlation(self, var1, var2):
        correlation = self.data[[var1, var2]].corr().iloc[0, 1]
        return correlation

    def perform_t_test(self, var1, var2):
        t_stat, p_value = stats.ttest_ind(self.data[var1], self.data[var2])
        return t_stat, p_value
