import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold

df = pd.read_csv("clean_data.csv")

def gradient_boosting_model():
    relevant_columns = [
        'Poor English proficiency, %',
        'Unemployed, %', 'Holds degree or higher, %', 'Schools',
        'Personal income <$400/week, %', 'Did not complete year 12, %', '2014'
    ]
    model_df = df[relevant_columns]
    X = model_df.drop(columns=['Personal income <$400/week, %'])
    Y = model_df['Personal income <$400/week, %']

    model = GradientBoostingRegressor()
    """
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=15)
    # Training and producing predictions
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)

    # Supervised learning by comparing with real values
    plt.scatter(Y_test, Y_pred, alpha=0.5)
    plt.plot([min(Y_test), max(Y_test)], [min(Y_test), max(Y_test)], color = 'black')
    plt.xlabel("Actual Personal income <$400/week, %")
    plt.ylabel("Predicted Personal income <$400/week, %")
    plt.title("Actual vs Predicted Values for Linear Regression")
    plt.grid(True)
    plt.savefig("erm.png")"""
    
    # 10 Fold Cross Validation
    mse_scores = - cross_val_score(model, X, Y, cv=5, scoring='neg_mean_squared_error')
    mean_mse = mse_scores.mean()
    print(f"MSE Scores: {mse_scores}")
    print(f"Mean MSE: {mean_mse}")

    # R2 validation
    r2_scores = cross_val_score(model, X, Y, cv=5, scoring='r2')
    mean_r2 = r2_scores.mean()
    print(f"R2 Scores: {r2_scores}")
    print(f"Mean R2: {mean_r2}")

    model.fit(X,Y)

    new_data = model_df.copy()
    #new_data['Poor English proficiency, %'] = new_data['Poor English proficiency, %'] * 0.8
    #new_data['Unemployed, %'] = new_data['Unemployed, %'] * 0.8
    #new_data['2014'] = new_data['2014'] * 0.8
    #new_data['Schools'] = new_data['Schools'] * 1.2
    new_data['Holds degree or higher, %'] = new_data['Holds degree or higher, %'] * 1.2
    new_data['Did not complete year 12, %'] = new_data['Did not complete year 12, %'] * 0.8
    X_new = new_data[relevant_columns]
    X_new = new_data.drop(columns=['Personal income <$400/week, %'])
    predictions = model.predict(X_new)
    print("Current mean low personal income across Victoria: {:.2f}".format(df["Personal income <$400/week, %"].mean()))
    print("This is the mean predicted low income percentage: {:.2f}".format(predictions.mean())) 

    return


