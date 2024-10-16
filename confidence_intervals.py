import numpy as np
import pandas as pd

def calculate_confidence_intervals(df):
    results = {}
    
    for gender in ['M', 'F']:
        gender_df = df[df['Gender'] == gender]
        mean = gender_df['Purchase'].mean()
        std = gender_df['Purchase'].std()
        n = len(gender_df)
        
        margin_of_error = 1.96 * (std / np.sqrt(n))  # 95% confidence interval
        
        lower = mean - margin_of_error
        upper = mean + margin_of_error
        
        results[gender] = {
            'mean': mean,
            'lower': lower,
            'upper': upper
        }
    
    return results