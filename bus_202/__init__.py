import pandas as pd
from pathlib import Path
from .functions.trim import trim
from .functions.boxplot import boxplot
from .functions.histogram import histogram

# Get the directory containing the data
DATA_DIR = Path(__file__).parent / 'data'
