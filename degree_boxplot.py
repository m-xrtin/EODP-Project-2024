import pandas as pd 
import matplotlib.pyplot as plt

def degree_boxplot():
    communities = pd.read_csv('communities.csv')
    communities.dropna(inplace=True)

    suburb = communities[communities['Community Name'].str.contains('Suburb')]
    suburb_degree = suburb['Holds degree or higher, %']
    suburb_year12 = suburb['Did not complete year 12, %']

    suburb_degree_Q3 = suburb_degree.quantile(0.75)
    suburb_year12_Q3 = suburb_year12.quantile(0.75)
    print(f"The upper quarter of those who hold a degree is : {suburb_degree_Q3:.2f}%")
    print(f"The upper quarter of those who haven't completed year 12 is : {suburb_year12_Q3:.2f}%")

    plt.figure(figsize=(15, 8))
    plt.boxplot([suburb_degree, suburb_year12], labels=['Holds a degree or higher', 'Did not complete year 12'], vert=False)

    plt.title('Education attainment in different suburbs', fontweight='bold')
    plt.xlabel('Percentage, %', fontweight='bold')
    plt.ylabel('Category', fontweight='bold')

    # Save the boxplot as a PNG file
    plt.savefig('degree_boxplot', bbox_inches='tight')

    # Display the plot
    plt.show()  
    return

