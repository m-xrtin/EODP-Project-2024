import os
import sys
    
def verify_heatmap():
    try:
        from heatmap import heatmap
    except ImportError:
        print("'heatmap' function not found.")
        return
    print("Verifying heatmap...")
    heatmap()
def verify_heatmap_small():
    try:
        from heatmap_small import heatmap_small
    except ImportError:
        print("'heatmap_small' function not found.")
        return
    print("Verifying heatmap_small...")
    heatmap_small()
def verify_education_and_income():
    try:
        from education_and_income import education_and_income
    except ImportError:
        print("'education_and_income' function not found.")
        return
    print("Verifying education_and_income...")
    education_and_income()

def verify_make_csv():
    try:
        from make_csv import make_csv
    except ImportError:
        print("'make_csv' function not found.")
        return
    print("Verifying make_csv...")
    make_csv()

def verify_linear_regress():
    try:
        from linear_regress import linear_regress
    except ImportError:
        print("'linear_regress' function not found.")
        return
    print("Verifying linear_regress...")
    linear_regress()

def verify_test():
    try:
        from test import test
    except ImportError:
        print("'test' function not found.")
        return
    print("Verifying test...")
    test()

def verify_poly_regression():
    try:
        from poly_regression import poly_regression
    except ImportError:
        print("'test' function not found.")
        return
    print("Verifying test...")
    poly_regression()

def verify_gradient_boosting_model():
    try:
        from gradient_boosting_model import gradient_boosting_model
    except ImportError:
        print("'test' function not found.")
        return
    print("Verifying test...")
    gradient_boosting_model()  

def verify_test_linear_with_cv():
    try:
        from test_linear_with_cv import test_linear_with_cv
    except ImportError:
        print("'test' function not found.")
        return
    print("Verifying test...")
    test_linear_with_cv() 

def verify_final_clean():
    try:
        from final_clean import final_clean
    except ImportError:
        print("'clean' function not found.")
        return
    print("Verifying final_clean...")
    final_clean()   

def verify_linear_r_1():
    try:
        from linear_r_1 import linear_r_1
    except ImportError:
        print("'linear_r_1' function not found.")
        return
    print("Verifying linear_r_1...")
    linear_r_1() 

def verify_gradient_boosting_model():
    try:
        from gradient_boosting_model import gradient_boosting_model
    except ImportError:
        print("'gradient_boosting_model' function not found.")
        return
    print("Verifying gradient_boosting_model...")
    gradient_boosting_model()

def verify_degree_boxplot():
    try:
        from degree_boxplot import degree_boxplot
    except ImportError:
        print("'degree_boxplot' function not found.")
        return
    print("Verifying degree_boxplot...")
    degree_boxplot()
def verify_education_levels():
    try:
        from education_levels import education_levels
    except ImportError:
        print("'education_levels' function not found.")
        return
    print("Verifying education_levels...")
    education_levels()
def verify_income_and_gambling():
    try:
        from income_and_gambling import income_and_gambling
    except ImportError:
        print("'income_and_gambling' function not found.")
        return
    print("Verifying income_and_gambling...")
    income_and_gambling()
def verify_income_vs_crime():
    try:
        from income_vs_crime import income_vs_crime
    except ImportError:
        print("'income_vs_crime' function not found.")
        return
    print("Verifying income_vs_crime...")
    income_vs_crime()
def verify_edu_vs_crime():
    try:
        from edu_vs_crime import edu_vs_crime
    except ImportError:
        print("'edu_vs_crime' function not found.")
        return
    print("Verifying edu_vs_crime...")
    edu_vs_crime()
def verify_heatmap_petty_crimes():
    try:
        from heatmap_petty_crimes import heatmap_petty_crimes
    except ImportError:
        print("'heatmap_petty_crimes' function not found.")
        return
    print("Verifying heatmap_petty_crimes...")
    heatmap_petty_crimes()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "linear_regress":
            verify_linear_regress()
        elif sys.argv[1] == "heatmap":
            verify_heatmap()
        elif sys.argv[1] == "education_and_income":
            verify_education_and_income()
        elif sys.argv[1] == "heatmap_small":
            verify_heatmap_small()
        elif sys.argv[1] == "make_csv":
            verify_make_csv()
        elif sys.argv[1] == "test":
            verify_test()
        elif sys.argv[1] == "poly_regression":
            verify_poly_regression()
        elif sys.argv[1] == "gradient_boosting":
            verify_graident_boosting()
        elif sys.argv[1] == "test_linear_with_cv":
            verify_test_linear_with_cv()
        elif sys.argv[1] == "final_clean":
            verify_final_clean()
        elif sys.argv[1] == "linear_r_1":
            verify_linear_r_1()
        elif sys.argv[1] == "gradient_boosting_model":
            verify_gradient_boosting_model()
        elif sys.argv[1] == "degree_boxplot":
            verify_degree_boxplot()
        elif sys.argv[1] == "education_levels":
            verify_education_levels()
        elif sys.argv[1] == "income_and_gambling":
            verify_income_and_gambling()
        elif sys.argv[1] == "income_vs_crime":
            verify_income_vs_crime()
        elif sys.argv[1] == "income_vs_edu":
            verify_income_vs_edu()
        elif sys.argv[1] == "edu_vs_crime":   
            verify_edu_vs_crime()
        elif sys.argv[1] == "heatmap_petty_crimes":
            verify_heatmap_petty_crimes()
        else:
            print("Invalid argument.")
    else:
        print("Usage: python main.py")
