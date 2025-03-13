import pandas as pd
import openpyxl
from scipy.stats import pearsonr
import matplotlib.pyplot as plt


def income_vs_crime():
    communities = pd.read_csv('communities.csv')
    print("CSV files loaded successfully.")

    # Load a specific sheet into a DataFrame
    df_table01 = pd.read_excel("Table01.xlsx", engine='openpyxl')
    df_table03 = pd.read_excel("Table03.xlsx", engine='openpyxl')
    df_tab = df_table03[df_table03["Year"] == 2014].copy()
    df_tab_1 = df_tab[df_tab["Offence Division"].isin(["A Crimes against the person", "B Property and deception offences", "C Drug offences","D Public order and security offences"])]

    # drop rows with NaN 
    communities.dropna(inplace=True)

    # creating a dataframe with just suburbs
    # Getting rid of the (suburb) specifier for each entry
    suburbs = communities[communities['Community Name'].str.contains('Suburb')].copy()
    suburbs["Community Name"] = suburbs["Community Name"].str.replace(r'\s+\(.*\)', '', regex = True)

    # Group by 'suburb_name' and sum the 'Offence Count'
    suburb_crime_tally = df_tab_1.groupby('Suburb/Town Name')['Offence Count'].sum().reset_index()

    # Renamed for easier merging process
    suburb_crime_tally = suburb_crime_tally.rename(columns={'Suburb/Town Name': 'suburb_name'})
    merged_df = pd.merge(suburbs, suburb_crime_tally, left_on='Community Name', right_on='suburb_name', how='left')
    
    merged_df["Personal income <$400/week, %"] = pd.to_numeric(merged_df["Personal income <$400/week, %"], errors='coerce')
    merged_df["Offence Count"] = pd.to_numeric(merged_df["Offence Count"], errors='coerce')
    merged_df["Crime Rate"] = (merged_df["Offence Count"] / merged_df["2012 ERP, total"]) * 1000
    # Create bins based on quantiles
   
    merged_df["Crime Category"] = pd.qcut(merged_df["Crime Rate"], q=[0, 0.25, 0.75, 1], labels=[1, 2, 3])

    print(merged_df)

    plt.figure(figsize=(10, 5))
    plt.scatter(merged_df['Personal income <$400/week, %'], merged_df['Crime Rate'])
    plt.title('Proportion of low income earners vs. Crime Rate', fontweight='bold')
    plt.xlabel('Proportion of low income earners', fontweight='bold')
    plt.ylabel('Crime Rate', fontweight='bold')
    plt.grid(True)
    plt.savefig('income_vs_crime_scatter.png')

    # Drop rows with missing data for the Pearson calculation
    valid_data = merged_df[['Personal income <$400/week, %', 'Crime Rate']].dropna()

    # Calculate the Pearson correlation coefficient
    pearson_corr, p_value = pearsonr(valid_data['Personal income <$400/week, %'], valid_data['Crime Rate'])
    
    return
