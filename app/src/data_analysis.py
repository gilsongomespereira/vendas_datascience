
import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(data):
    # Análise de dados
    summary = data.describe()
    data['sales'].plot(kind='hist')
    plt.savefig('/app/static/sales_histogram.png')
    return summary
