import pandas as pd
from pathlib import Path

# Get the directory containing the data
DATA_DIR = Path(__file__).parent / 'data'

# Load the data when the package is imported
gapfinder = pd.read_excel(DATA_DIR / 'gapfinder.xlsx')
