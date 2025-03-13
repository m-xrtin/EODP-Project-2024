import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold

df = pd.read_csv("communities.csv")
crime_df = pd.read_excel("Table03.xlsx")

def heatmap_petty_crimes():
    df["Schools"] = df["Primary Schools"] + df["Secondary Schools"] + df["P12 Schools"] + df["Other Schools"]
    suburbs = df[df["Community Name"].str.contains("Suburb")].copy()
    suburbs["Community Name"] = suburbs["Community Name"].str.replace(r'\s+\(.*\)', '', regex = True)

    crimes_2014 = crime_df[crime_df["Year"] == 2014].copy()
    petty_crimes = crimes_2014[crimes_2014["Offence Subdivision"].isin([
        "A20 Assault and related offences", 
        "B40 Theft", 
        "B20 Property damage", 
        "B30 Burglary/Break and enter"
        ])].copy()
    grouped_crimes = petty_crimes.groupby("Suburb/Town Name")['Offence Count'].sum()
    merged_df = pd.merge(suburbs, grouped_crimes, left_on='Community Name', right_on='Suburb/Town Name', how='left')
    relevant_columns = [
    '2012 ERP, total', 'Poor English proficiency, %', 'Number of Households', 'Unemployed, %', 
    'Equivalent household income <$600/week, %', 'Schools', 
    'Personal income <$400/week, %', 'Did not complete year 12, %', 
    'Holds degree or higher, %', 'Offence Count'
    ]
    filtered_df = merged_df[relevant_columns]
    
    # Set up Heatmap
    correlation_matrix = filtered_df.corr()
    plt.figure(figsize=(20, 15))
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title('Correlation Heatmap of Selected Features', fontsize=16)
    plt.tight_layout()
    plt.savefig("heatmap_petty_crimes.png")
    return

