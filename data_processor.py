import pandas as pd

def process_data(df):
    # Convert specific columns to object type
    cols = ['Occupation', 'Marital_Status', 'Product_Category']
    df[cols] = df[cols].astype('object')
    
    # Group by User_ID and Gender, and sum the Purchase amount
    amt_df = df.groupby(['User_ID', 'Gender'])[['Purchase']].sum().reset_index()
    
    return amt_df