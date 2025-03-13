import pandas as pd
import matplotlib.pyplot as plt

def education_levels():
    communities = pd.read_csv('communities.csv')
    communities.dropna(inplace=True)
    suburbs = communities[communities['Community Name'].str.contains('Suburb')]

    suburbs.loc["Did not complete year 12, %"] = pd.to_numeric(suburbs["Did not complete year 12, %"], errors= "coerce")
    print(suburbs.head())

    poor = len(suburbs[suburbs["Did not complete year 12, %"] > 51.04])
    medium = len(suburbs[(suburbs["Did not complete year 12, %"] < 51.04) & (suburbs["Holds degree or higher, %"] < 58.98)])
    high = len(suburbs[suburbs["Holds degree or higher, %"] > 58.98])

    education_levels = ['Poor', 'Medium', 'High']
    education_df = [poor, medium, high]

    plt.figure(figsize=(10, 6))
    plt.bar(education_levels, education_df)
    plt.title('Number of suburbs in each education level', fontweight='bold')
    plt.xlabel('Level of education', fontweight='bold')
    plt.ylabel('Number of suburbs', fontweight='bold')
    plt.xticks(rotation=45, ha='right')

    # Save the bar chart as a PNG file
    plt.savefig('education_levels_bar', bbox_inches='tight')

    return

