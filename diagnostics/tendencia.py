import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing, Holt
from statsmodels.tsa.stattools import adfuller
from sklearn.linear_model import LinearRegression, Ridge, Lasso

class TrendAnalysis:
    def __init__(self, data):
        self.data = data
        self.variables = data.columns

    def adf_test(self):
        results = {}
        for variable in self.variables:
            adf_result = adfuller(self.data[variable])
            results[variable] = adf_result[1]
            print(f"Test ADF para estacionalidad de {variable}: p-value = {adf_result[1]}")
        return results

    def exponential_smoothing(self, alpha=0.5, steps=10):
        forecasts = {}
        for variable in self.variables:
            model = ExponentialSmoothing(self.data[variable], trend="additive", seasonal="additive", seasonal_periods=12).fit(smoothing_level=alpha)
            forecast = model.forecast(steps=steps)
            forecasts[variable] = forecast
            print(f"Pronóstico de {variable} con Exponential Smoothing (alpha={alpha}):")
            print(forecast)
        return forecasts

    def holt_winters(self, seasonal_periods=7, steps=10):
        forecasts = {}
        for variable in self.variables:
            model = Holt(self.data[variable], trend="additive", damped_trend=True).fit()
            forecast = model.forecast(steps=steps)
            forecasts[variable] = forecast
            print(f"Pronóstico de {variable} con Holt-Winters (seasonal_periods={seasonal_periods}):")
            print(forecast)
        return forecasts

    def linear_regression(self):
        results = {}
        for variable in self.variables:
            X = self.data.drop(variable, axis=1)  # Variables independientes
            y = self.data[variable]  # Variable dependiente
            model = LinearRegression()
            model.fit(X, y)
            score = model.score(X, y)
            intercept = model.intercept_
            coefficients = dict(zip(X.columns, model.coef_))
            results[variable] = {
                "R^2": score,
                "Intercept": intercept,
                "Coefficients": coefficients
            }
            print(f"Modelo de regresión lineal para {variable}:")
            print(f"Coeficiente de determinación (R^2): {score}")
            print(f"Intercepto: {intercept}")
            print("Coeficientes de regresión:")
            for feature, coef in coefficients.items():
                print(f"  - {feature}: {coef}")
        return results

    def ridge_regression(self, alpha=1.0):
        results = {}
        for variable in self.variables:
            X = self.data.drop(variable, axis=1)  # Variables independientes
            y = self.data[variable]  # Variable dependiente
            model = Ridge(alpha=alpha)
            model.fit(X, y)
            score = model.score(X, y)
            coefficients = dict(zip(X.columns, model.coef_))
            results[variable] = {
                "R^2": score,
                "Coefficients": coefficients
            }
            print(f"Modelo de regresión Ridge para {variable}:")
            print(f"Coeficiente de determinación (R^2): {score}")
            print("Coeficientes de regresión:")
            for feature, coef in coefficients.items():
                print(f"  - {feature}: {coef}")
        return results

    def lasso_regression(self, alpha=1.0):
        results = {}
        for variable in self.variables:
            X = self.data.drop(variable, axis=1)  # Variables independientes
            y = self.data[variable]  # Variable dependiente
            model = Lasso(alpha=alpha)
            model.fit(X, y)
            score = model.score(X, y)
            coefficients = dict(zip(X.columns, model.coef_))
            results[variable] = {
                "R^2": score,
                "Coefficients": coefficients
            }
            print(f"Modelo de regresión Lasso para {variable}:")
            print(f"Coeficiente de determinación (R^2): {score}")
            print("Coeficientes de regresión:")
            for feature, coef in coefficients.items():
                print(f"  - {feature}: {coef}")
        return results
