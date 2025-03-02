import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent

class DataFrames:
    _midterm = None
    _financials = None
    _exec_comp = None
    _a1_df = None
    _gapfinder = None
    
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
    
    @property
    def financials(self):
        if self._financials is None:
            self._financials = pd.read_excel(DATA_DIR / 'financials.xlsx')
        return self._financials
    
    @property
    def exec_comp(self):
        if self._exec_comp is None:
            self._exec_comp = pd.read_excel(DATA_DIR / 'exec_comp.xlsx')
        return self._exec_comp
    
    @property
    def a1_df(self):
        if self._a1_df is None:
            self._a1_df = pd.read_excel(DATA_DIR / 'a1_df.xlsx')
        return self._a1_df

# Just export the class instance
df = DataFrames()
