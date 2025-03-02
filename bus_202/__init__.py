import pandas as pd
from pathlib import Path
from .functions.trim import trim
from .functions.boxplot import boxplot
from .functions.histogram import histogram
from .data import df

# Create properties at the package level
@property
def gapfinder():
    return df.gapfinder

@property
def financials():
    return df.financials

@property
def exec_comp():
    return df.exec_comp

@property
def a1_df():
    return df.a1_df

@property
def midterm():
    return df.midterm
