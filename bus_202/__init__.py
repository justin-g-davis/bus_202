import pandas as pd
from pathlib import Path
from .functions.trim import trim
from .functions.boxplot import boxplot
from .functions.histogram import histogram

# Get the directory containing the data
DATA_DIR = Path(__file__).parent / 'data'

# Load the data when the package is imported
gapfinder = pd.read_excel(DATA_DIR / 'gapfinder.xlsx')
financials = pd.read_excel(DATA_DIR / 'financials.xlsx')
exec_comp = pd.read_excel(DATA_DIR / 'exec_comp.xlsx')
a1_df = pd.read_excel(DATA_DIR / 'a1_df.xlsx')
