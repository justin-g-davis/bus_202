import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent

class DataFrames:
    _sp1500_cross-sectional = None
    _sp1500_panel = None
    
    @property
    def gapfinder(self):
        if self._gapfinder is None:
            self._gapfinder = pd.read_excel(DATA_DIR / 'gapfinder.xlsx')
        return self._gapfinder
    
    @property
    def midterm(self):
        if self._midterm is None:
            self._midterm = pd.read_excel(DATA_DIR / 'midterm.xlsx')
        return self._midterm

# Create a single instance
_data = DataFrames()

# Define module-level functions that return the data
def midterm():
    return _data.midterm

def financials():
    return _data.financials

def exec_comp():
    return _data.exec_comp

def a1_df():
    return _data.a1_df

def a3_df():
    return _data.a3_df

def gapfinder():
    return _data.gapfinder

def sweet_things():
    return _data.sweet_things

def sweet_things_simple():
    return _data.sweet_things_simple

def new_ceo():
    return _data.new_ceo

def restate():
    return _data.restate

def group_1_1():
    return _data.group_1_1

def group_1_2():
    return _data.group_1_2

def group_1_3():
    return _data.group_1_3

def group_1_4():
    return _data.group_1_4

def group_1_5():
    return _data.group_1_5

def group_1_6():
    return _data.group_1_6

def group_2_1():
    return _data.group_2_1

def group_2_2():
    return _data.group_2_2

def group_2_3():
    return _data.group_2_3

def group_2_4():
    return _data.group_2_4

def group_2_5():
    return _data.group_2_5

def group_2_6():
    return _data.group_2_6

def group_3_1():
    return _data.group_3_1

def group_3_2():
    return _data.group_3_2

def group_3_3():
    return _data.group_3_3

def group_3_4():
    return _data.group_3_4

def group_3_5():
    return _data.group_3_5

def group_3_6():
    return _data.group_3_6
