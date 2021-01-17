import pandas as pd 
import numpy as np

gpu_names = []

def create_table():
    df = pd.read_csv("gpu_data.csv")
    df['Under $500 and In Stock?'] = np.where((df['Price'] <= 500) & (df['Availability'] == True),'Yes!', 'Check back later :/')
    return df

def check_available(input_df):
    if input_df['Under $500 and In Stock?'].str.contains('Yes!').any():
        found = input_df.loc[input_df['Under $500 and In Stock?'] == 'Yes!', 'Product Name']

        # Add GPU's that meet criteria to list 
        for index in found:
            gpu_names.append(index)
        
        return True
    else:
        return False

check_available(create_table())
print(gpu_names)