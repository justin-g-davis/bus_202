import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent

def financials():
    return pd.read_excel(DATA_DIR / 'financials.xlsx')

def exec_comp():
    return pd.read_excel(DATA_DIR / 'exec_comp.xlsx')

def a1_df():
    return pd.read_excel(DATA_DIR / 'a1_df.xlsx')

def midterm():
    return pd.read_excel(DATA_DIR / 'midterm.xlsx')
