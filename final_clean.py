import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def final_clean():
    filtered = pd.read_csv('filtered.csv')
    
    # fill null rows with mean
    filtered.fillna(filtered.mean(), inplace=True)

    filtered = remove_outliers(filtered)

    filtered.to_csv('clean_data.csv', index=False)

    # testing if outliers are removed
    plt.figure(figsize=(15, 8))
    plt.boxplot(filtered['2012 ERP, total'], vert=False)
    plt.savefig('boxplot.png', bbox_inches='tight')

    return 


def remove_outliers(df):
    for col in df.columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - (1.5 * IQR)
        upper_bound = Q3 + (1.5 * IQR)

        mean = df[col].mean()
        df[col] = df[col].apply(lambda x: mean if x < lower_bound or x > upper_bound else x)
    return df
