import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("communities.csv")
crime_data = pd.read_excel("Table01.xlsx")
gambling_df = pd.read_csv("EGM.csv")

def heatmap_small():

    # Clean the LGA names in the communities dataframe
    df['LGA'] = df['LGA'].str.lower()
    df['LGA'] = df['LGA'].str.replace(r'\s+\(.*\)', '', regex=True).str.lower()

    df["Schools"] = df["Primary Schools"] + df["Secondary Schools"] + df["P12 Schools"] + df["Other Schools"]
    df['Location_numeric'] = df['Location'].str.extract(r'(\d+\.?\d*)').astype(float)

    # Group by LGA and calculate mean values for the specified features
    grouped_lga = df.groupby('LGA').agg({
        'Poor English proficiency, %': 'mean',
        '2012 ERP, total': 'mean',
        'Number of Households': 'mean',
        'Unemployed, %': 'mean',
        'Equivalent household income <$600/week, %': 'mean',
        'Schools': 'mean',
        'Personal income <$400/week, %': 'mean',
        'Did not complete year 12, %': 'mean',
        'Holds degree or higher, %': 'mean',
        'Location_numeric': 'mean'
    }).reset_index()

    # Clean crime data: strip spaces and replace MERRI-BEK with MORELAND
    crime_data["LGA"] = crime_data["Local Government Area"].str.strip().str.lower()
    crime_data["LGA"] = crime_data["LGA"].replace("MERRI-BEK", "MORELAND")
    
    gambling_df['LGA'] = gambling_df['LGA Name'].str.lower()  # Convert to lowercase
    gambling_df['LGA'] = gambling_df['LGA'].str.replace(r'city of\s+|shire of\s+|rural city of\s+', '', regex=True)

    # Merge on 'LGA' column for both crime and gambling
    merged_df = pd.merge(grouped_lga, crime_data[crime_data["Year"] == 2014], on='LGA', how='inner')
    merged_again_df = pd.merge(merged_df, gambling_df, on ='LGA', how = 'inner')

    # Select only the columns you're interested in (the ones from grouped LGA and crime data)
    relevant_columns = [
        'Poor English proficiency, %',
        'Unemployed, %', 'Holds degree or higher, %', 'Schools',
        'Personal income <$400/week, %', 'Did not complete year 12, %', '2014'
    ]
    
    # Filter the dataframe to keep only relevant features
    filtered_df = merged_again_df[relevant_columns]
    
    # Set up Heatmap
    correlation_matrix = filtered_df.corr()
    plt.figure(figsize=(20, 15))
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", annot_kws={"size": 20})
    plt.title('Correlation Heatmap of Selected Features', fontsize=25)
    plt.tight_layout()
    plt.savefig("heatmap_small.png")
    return
