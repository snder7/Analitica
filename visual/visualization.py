# visual/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class Visualization:
    def __init__(self, data):
        self.data = data

    def plot_histogram(self, column, save_path=None):
        plt.figure()
        sns.histplot(self.data[column])
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

    def plot_boxplot(self, column, save_path=None):
        plt.figure()
        sns.boxplot(x=self.data[column])
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

    def plot_violinplot(self, column, save_path=None):
        plt.figure()
        sns.violinplot(x=self.data[column])
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

    def plot_scatter(self, column1, column2, save_path=None):
        plt.figure()
        sns.scatterplot(x=self.data[column1], y=self.data[column2])
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

    def plot_correlation_heatmap(self, exclude_columns=None, save_path=None):
        plt.figure()
        corr = self.data.drop(columns=exclude_columns).corr()
        sns.heatmap(corr, annot=True, fmt=".2f")
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

    def plot_distribution(self, column, log_transform=False, save_path=None):
        plt.figure()
        if log_transform:
            sns.histplot(np.log1p(self.data[column]))
        else:
            sns.histplot(self.data[column])
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

    def plot_pie_chart(self, column, save_path=None):
        plt.figure()
        self.data[column].value_counts().plot.pie(autopct='%1.1f%%')
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()
