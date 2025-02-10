import matplotlib.pyplot as plt
import numpy as np
from .trim import trim

def histogram(series, title=None, bins=30, trim=100):
    # Create figure and axis
    fig, ax = plt.subplots()
    
    # Get base title
    if not title:
        title = series.name
        
    # Apply trimming if trim < 100
    if trim < 100:
        series = trim(series, trim)
        title = f"{title} (outliers removed at {trim}% level)"
    
    # Convert to numpy array and handle NaN
    data = np.array(series.dropna()).flatten()
    
    # Create histogram
    ax.hist(data, 
            bins=bins,
            edgecolor='black',
            color='skyblue',
            alpha=0.7)
    
    # Add labels and styling
    ax.set_title(title)
    ax.set_ylabel('Count')
    ax.ticklabel_format(style='plain', axis='x')
    ax.grid(True, linestyle='--', alpha=0.7)
    
    plt.show(block=False)
