import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("clean_data.csv")

def poly_regression(degree = 2):
    relevant_columns = [
        'Poor English proficiency, %',
        'Unemployed, %', 'Holds degree or higher, %', 'Schools',
        'Personal income <$400/week, %', 'Did not complete year 12, %', '2014'
    ]
    model_df = df[relevant_columns]
    X = model_df.drop(columns=['Personal income <$400/week, %'])
    Y = model_df['Personal income <$400/week, %']

    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)
    model = LinearRegression()
    
    # 10 Fold Cross Validation
    mse_scores = - cross_val_score(model, X_poly, Y, cv=5, scoring='neg_mean_squared_error')
    mean_mse = mse_scores.mean()
    print(f"MSE Scores: {mse_scores}")
    print(f"Mean MSE: {mean_mse}")

    # R2 validation
    r2_scores = cross_val_score(model, X_poly, Y, cv=5, scoring='r2')
    mean_r2 = r2_scores.mean()
    print(f"R2 Scores: {r2_scores}")
    print(f"Mean R2: {mean_r2}")

    return
