import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("communities.csv")
gambling_df = pd.read_csv("EGM.csv")

def income_and_gambling():
    # We are going to group by LGA, so that we can compre between LGAs with the EGM file
    df['LGA'] = df['LGA'].str.lower()
    df['LGA'] = df['LGA'].str.replace(r'\s+\(.*\)', '', regex=True).str.lower()

    gambling_df['LGA'] = gambling_df['LGA Name'].str.lower()  # Convert to lowercase
    gambling_df['LGA'] = gambling_df['LGA'].str.replace(r'city of\s+|shire of\s+|rural city of\s+', '', regex=True)

    grouped_lga = df.groupby('LGA').agg({
    'Personal income <$400/week, %': 'mean',
    'Did not complete year 12, %': 'mean',
    'Holds degree or higher, %': 'mean',
    'Equivalent household income <$600/week, %': 'mean'
    }).reset_index()

    merged_df = pd.merge(grouped_lga, gambling_df, on='LGA', how='inner')
    
    # Our graph can see a negative linear relationship between higher education holder vs low income
    plt.scatter(x=merged_df['Personal income <$400/week, %'], y=merged_df['2011'], alpha=0.5)
    plt.title('Low income vs losses in gambling')
    plt.xlabel('Percentage of income <400 a week')
    plt.ylabel('Gambling Losses (Dollar)')
    plt.grid(True)
    plt.savefig("income_vs_gambling_tendency.png")

    Degree_and_low_income = ['Holds degree or higher, %', 'Personal income <$400/week, %']
    print(grouped_lga[Degree_and_low_income].corr(method='pearson'))
    Low_education_and_low_income = ['Did not complete year 12, %', 'Personal income <$400/week, %']
    print(grouped_lga[Low_education_and_low_income].corr(method='pearson'))
    
    
    return
