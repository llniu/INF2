import pandas as pd
import numpy as np

def assign_normal(df: pd.DataFrame) -> pd.DataFrame:
    """
    Assigns True/False to a new column 'normal' in the dataframe 
    based on CAP, AST, ALT, and sex criteria.
    
    - No biopsy (df['biopsy'] == False)
    - CAP < 300 dB/m
    - Women: ALT < 45 U/L and AST < 35 U/L
    - Men:   ALT < 70 U/L and AST < 45 U/L
    
    Returns:
        DataFrame with a new column.
    """
    
    # start with no score
    df['normal'] = False
    
    # condition for "no biopsy"
    #no_biopsy = df['biopsy'] == False
    
    # conditions for women
    women_condition = (
        #(df['te']<6) &
        (df['gender'] == 0) &
        (df['cap'] < 300) &
        (df['alt'] < 45) &
        (df['ast'] < 35)
    )
    
    # conditions for men
    men_condition = (
        #(df['te']<6) &
        (df['gender'] == 1) &
        (df['cap'] < 300) &
        (df['alt'] < 70) &
        (df['ast'] < 45)
    )
    
    # apply score = 0 for eligible participants without biopsy
    df.loc[(women_condition | men_condition), 'normal'] = True
    
    return df

def assign_supernormal(df: pd.DataFrame) -> pd.DataFrame:
    """
    Assigns True/False to a new column 'supernormal' in the dataframe 
    based on CAP, AST, ALT, and sex criteria.

    Criteria:
      - CAP < 248 dB/m2
      - AST <= 20 U/L
      - ALT <= 20 U/L for women, ALT <= 30 U/L for men

    Returns:
        DataFrame with a new column.
    """
    
    # start with no score
    df['supernormal'] = False
    
    # condition for "no biopsy"
    #no_biopsy = df['biopsy'] == False
    
    # conditions for women
    women_condition = (
        #(df['te']<6) &
        (df['gender'] == 0) &
        (df['cap'] < 248) &
        (df['alt'] <= 20) &
        (df['ast'] <= 20)
    )
    
    # conditions for men
    men_condition = (
        #(df['te']<6) &
        (df['gender'] == 1) &
        (df['cap'] < 248) &
        (df['alt'] <= 30) &
        (df['ast'] <= 20)
    )
    
    # apply score = 0 for eligible participants without biopsy
    df.loc[(women_condition | men_condition), 'supernormal'] = True
    
    return df

