import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("communities.csv")
crime_data = pd.read_excel("Table01.xlsx")
gambling_df = pd.read_csv("EGM.csv")

def make_csv():
    # Clean the LGA names in the communities dataframe
    df['LGA'] = df['LGA'].str.lower()
    df['LGA'] = df['LGA'].str.replace(r'\s+\(.*\)', '', regex=True).str.lower()

    df["Schools"] = df["Primary Schools"] + df["Secondary Schools"] + df["P12 Schools"] + df["Other Schools"]
    df['Location_numeric'] = df['Location'].str.extract(r'(\d+\.?\d*)').astype(float)

    # Group by LGA and calculate mean values for the specified columns
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
        'Equivalent household income <$600/week, %': 'mean',
        'Location_numeric': 'mean'
    }).reset_index()   
    # Clean crime data: strip spaces and replace MERRI-BEK with MORELAND
    crime_data["LGA"] = crime_data["Local Government Area"].str.strip().str.lower()
    crime_data["LGA"] = crime_data["LGA"].replace("MERRI-BEK", "MORELAND")
    
    gambling_df['LGA'] = gambling_df['LGA Name'].str.lower()  # Convert to lowercase
    gambling_df['LGA'] = gambling_df['LGA'].str.replace(r'city of\s+|shire of\s+|rural city of\s+', '', regex=True)

    # Merge on 'LGA' column
    merged_df = pd.merge(grouped_lga, crime_data[crime_data["Year"] == 2014], on='LGA', how='inner')
    merged_again_df = pd.merge(merged_df, gambling_df, on ='LGA', how = 'inner')

    # Select only the columns you're interested in (the ones from grouped LGA and crime data)
    relevant_columns = [
        '2012 ERP, total', 'Poor English proficiency, %', 'Number of Households', 'Unemployed, %', 
        'Equivalent household income <$600/week, %', 'Schools', 
        'Personal income <$400/week, %', 'Did not complete year 12, %', 
        'Holds degree or higher, %', 'Location_numeric', 'Offence Count', 'Rate per 100,000 population', '2014'
    ]
    
    # Filter the dataframe to keep only relevant columns
    filtered_df = merged_again_df[relevant_columns]
    
    train_df = filtered_df.iloc[:50]  
    test_df = filtered_df.iloc[50:]   

    train_df.to_csv('train_data.csv', index=False)
    test_df.to_csv('test_data.csv', index=False)
    filtered_df.to_csv('filtered.csv', index=False)
    return

    
    
