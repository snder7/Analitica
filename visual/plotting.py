# visualization/plotting.py
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, stats

def plot_histogram(data, variable, bins=10, title='Histogram'):
    plt.figure(figsize=(10, 6))
    data[variable].hist(bins=bins)
    plt.title(title)
    plt.xlabel(variable)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def plot_boxplot(data, variable, title='Boxplot'):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data[variable])
    plt.title(title)
    plt.xlabel(variable)
    plt.grid(True)
    plt.show()

def plot_scatter(data, x_variable, y_variable, title='Scatter Plot'):
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_variable], data[y_variable])
    plt.title(title)
    plt.xlabel(x_variable)
    plt.ylabel(y_variable)
    plt.grid(True)
    plt.show()

def plot_correlation_heatmap(self, exclude_columns=None):
        """
        Plots a heatmap of the correlations between numerical variables in the data.

        Parameters:
        - exclude_columns (list of str): List of column names to exclude from the correlation matrix.
        """
        if exclude_columns is None:
            exclude_columns = []

        # Drop the specified columns
        data_for_corr = self.data.drop(columns=exclude_columns)

        # Calculate the correlation matrix
        corr_matrix = data_for_corr.corr()

        # Plot the heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, square=True, cmap='coolwarm', fmt='.2f')
        plt.title('Pearson Correlation Heatmap')
        plt.show()

def plot_distribution(self, variable, log_transform=False):
    data = np.log1p(self.data[variable]) if log_transform else self.data[variable]
    (mu, sigma) = norm.fit(data)

    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(19, 5))

    ax1 = sns.histplot(data, kde=True, ax=ax1, stat="density", fit=norm)
    ax1.legend([f'Normal distribution ($\mu=$ {mu:.3f} and $\sigma=$ {sigma:.3f})'], loc='best')
    ax1.set_ylabel('Frequency')
    title = f'Log(1+{variable}) Distribution' if log_transform else f'{variable} Distribution'
    ax1.set_title(title)

    stats.probplot(data, dist="norm", plot=ax2)
    ax2.set_title(f'Probability Plot ({title})')

    plt.show()

def plot_pie_chart(self, variable):
    data_counts = self.data[variable].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(data_counts, labels=data_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(f'Pie Chart of {variable}')
    plt.axis('equal')
    plt.show()

def plot_heatmap(self, pivot_table_data, x_variable, y_variable, value_variable):
    pivot_table = pivot_table_data.pivot(index=y_variable, columns=x_variable, values=value_variable)
    plt.figure(figsize=(10, 8))
    sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap='viridis')
    plt.title(f'Heatmap of {value_variable} by {x_variable} and {y_variable}')
    plt.show()