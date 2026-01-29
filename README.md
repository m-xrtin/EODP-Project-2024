# 🚀 EODP Project

## ❓ Research Question ❓
How can we combat income disparity in Victoria?

## 📄 Research Paper  
This project explores income inequality across Victorian suburbs using data science techniques,  
including statistical analysis and predictive modeling.

📥 [Download Full Research Paper (PDF)](Thesis.pdf)

## How to run a program 🏃‍♂️💨
To run an individual program: 
```py 
python main.py file_name
```

## What files did we use?
EGM.csv: Contains gambling data by local government areas (LGAs) in Victoria.

Table01.xlsx: Crime data sorted by LGA (We later limited to only the year 2014 for crime data)

Table03.xlsx: Contains additional data for use in certain analyses, such as types of offence, subcategories.

communities.csv: The main dataset for Victorian communities, containing socioeconomic data such as unemployment, education, and income levels, population, etc.

filtered.csv: Filtered dataset that includes merged data from multiple sources like crime and gambling data.

clean_data.csv: Preprocessed data after cleaning and transformations applied, and used for our model building.

predictions.txt: Contains predictions from the various regression models.

## What does each program do? 😈
degree_boxplot: creates a boxplot to show the proportions of people who hold a degree compared to the those who did not complete year 12 in suburbs.

education_and_income: creates a scatterplot to depict the proportion of low income earners (x-axis) vs. the proportion of people who did not complete year 12 (y-axis).

education_levels: dividing suburbs into categories of low, medium or highly educated. 
- low education level: has more than 75% of the population who did not complete year 12
- medium education level: in between low and highly
- high education level: has more than 75% of the population who holds a degree, or higher

gradient_boosting_model: Implements the gradient boosting regression model to predict the proportion of low-income earners across Victorian communities, 
includes cross-validation to test performance.

heatmap: creates a correlation map of 13 potentially relevant factors:
- Poor English proficiency, %
- 2012 ERP, total
- Number of Households
- Unemployed, %
- Equivalent household income <$600/week, %
- Schools
- Personal income <$400/week, %
- Did not complete year 12, %
- Holds degree or higher, %
- Location_numeric
- Offence count 
- Rate Per 100 000 population
- Gambling losses (2014)

heatmap_small: creates a correlation map with only the 7 selected factors used in regression models:
- Poor English proficiency, %
- Unemployed, % 
- Holds degree or higher, %
- Schools
- Personal income <$400/week, % 
- Did not complete year 12, %
- 2014 (Gambling losses in 2014)

heatmap_petty_crimes: Re-analysis of correlations with crime, by only including crimes that relate to theft, burglary, and personal attacks.

income_and_gambling: creates a scatterplot depicting the proportion of low income earners (x-axis) vs. the gambling losses in 2011 (y-axis).

income_vs_crime: This script analyzes the relationship between low-income earners and crime rates in Victorian suburbs. It merges crime data from 2014 with community income data and calculates crime rates per 1,000 residents. 
The script generates a scatter plot to visualize the correlation between the proportion of low-income earners and crime rates, and calculates the Pearson correlation coefficient between the two.

linear_r_1: Implements the Linear regression model to predict the proportion of low-income earners across Victorian communities, 
includes cross-validation to test performance.

make_csv: creates a training set, a test set to be used for linear regression and a "filtered" set to be cleaned and later used during cross-validation.

poly_regression: Implements the polynomial regression model, specifically to degree 2, to predict potential parabola relationship, and 
predict proportion of low-income earners across Victorian communities, includes cross-validation to test performance.

## Steps to Run the Project 😎

1. Preprocessing, Visualizations, and Correlation Analysis:

Several scripts focus on preprocessing and visualizing correlations between different socioeconomic factors. These include:
- education_and_income.py
- education_levels.py
- heatmap.py
- heatmap_small.py
- heatmap_petty_crimes.py
- income_and_gambling.py
Feel free to run any of these scripts to explore the visualizations and analyses of the relationship between specific variables.

2. Modeling and Predictions:
We have provided a preprocessed dataset, clean_data.csv. You can directly run the following modeling scripts for cross-validation analysis:

- linear_r_1.py
- gradient_boosting_model.py
- poly_regression.py

If you want to make specific predictions using the models, you can modify the features (currently commented out in the code). Uncomment and adjust these features as needed to generate custom predictions.

3. Visualization of Training and Testing Sets:

Visualizations related to training and testing data sets are also available within the scripts. To view these, simply uncomment the relevant lines in the code.

