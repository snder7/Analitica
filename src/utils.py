# src/utils.py
def calculate_mean(data, variable):
    return data[variable].mean()

def calculate_median(data, variable):
    return data[variable].median()

def calculate_mode(data, variable):
    return data[variable].mode()

def calculate_variance(data, variable):
    return data[variable].var()

def calculate_std_dev(data, variable):
    return data[variable].std()
