import pandas as pd
import openpyxl
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

def education_and_income():
    communities = pd.read_csv('communities.csv')
    communities.dropna(subset=['Did not complete year 12, %', 'Personal income <$400/week, %'], inplace=True)
    print("CSV files loaded successfully.")
    

    # creating a dataframe with just suburbs
    # Getting rid of the (suburb) specifier for each entry
    suburbs = communities[communities['Community Name'].str.contains('Suburb')].copy()

    # Plot the scatter plot
    plt.figure(figsize=(12, 7))
    plt.scatter(communities['Did not complete year 12, %'], communities['Personal income <$400/week, %'])

    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title('Proportion of people who did not complete year 12 vs. Proportion of low income earners', fontweight='bold')
    plt.xlabel('Proportion of low income earners, %', fontweight='bold')
    plt.ylabel('Proportion of people who did not complete year 12, %', fontweight='bold')
    plt.grid(True)

    # save the plot as a PNG file
    plt.savefig('income_vs_edu_scatter')

    # Calculate the Pearson correlation coefficient
    pearson_corr, p_value = pearsonr(communities['Did not complete year 12, %'], communities['Personal income <$400/week, %'])

    print(f"Pearson's correlation: {pearson_corr}" )

    return

