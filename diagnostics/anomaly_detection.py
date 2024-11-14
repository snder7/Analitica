import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

class AnomalyDetection:
    def __init__(self, data, variables):
        self.data = data
        self.variables = variables

    def calculate_statistics(self):
        self.mean_std = {}
        for variable in self.variables:
            mean_value = self.data[variable].mean()
            std_dev = self.data[variable].std()
            self.mean_std[variable] = {'mean': mean_value, 'std': std_dev}

    def detect_anomalies_zscore(self, threshold=3):
        self.zscore_anomalies = {}
        for variable in self.variables:
            mean_value = self.mean_std[variable]['mean']
            std_dev = self.mean_std[variable]['std']
            zscores = (self.data[variable] - mean_value) / std_dev
            anomalies_zscore = [i for i, z in enumerate(zscores) if abs(z) > threshold]
            self.zscore_anomalies[variable] = anomalies_zscore
            print(f"Anomalías Z-score para {variable}: {anomalies_zscore}")

    def detect_anomalies_iqr(self):
        self.iqr_anomalies = {}
        for variable in self.variables:
            q1 = self.data[variable].quantile(0.25)
            q3 = self.data[variable].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            anomalies_IQR = [i for i, value in enumerate(self.data[variable]) if value < lower_bound or value > upper_bound]
            self.iqr_anomalies[variable] = anomalies_IQR
            print(f"Anomalías IQR para {variable}: {anomalies_IQR}")

    def detect_anomalies_isolation_forest(self):
        isof = IsolationForest(random_state=42)
        isof.fit(self.data[self.variables].values)
        anomalies_isof = isof.predict(self.data[self.variables].values)
        self.isof_anomalies = np.where(anomalies_isof == -1)[0]
        print(f"Anomalías Isolation Forest: {self.isof_anomalies}")




#ad = AnomalyDetection(data, variables)
#ad.calculate_statistics()
#ad.detect_anomalies_zscore()
#ad.detect_anomalies_iqr()
#ad.detect_anomalies_isolation_forest()
