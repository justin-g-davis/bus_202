import matplotlib.pyplot as plt
import numpy as np
from trim import trim

def boxplot(series, title=None, percentile_keep=100):
    # Create figure and axis
    fig, ax = plt.subplots()
    
    if not title:
        title = series.name
        
    # Apply trimming if percentile_keep < 100
    if percentile_keep < 100:
        series = trim(series, percentile_keep)
        title = f"{title} (outliers removed at {percentile_keep}% level)"
    
    # Convert to numpy array and ensure 1D
    data = np.array(series.dropna()).flatten()
    
    # Create boxplot on the axis
    ax.boxplot(data,
        patch_artist=True,
        boxprops=dict(facecolor='skyblue', color='black'),
        medianprops=dict(color='black'),
        flierprops=dict(marker='o', markerfacecolor='gray'),
        whiskerprops=dict(color='black'),
        capprops=dict(color='black'))
    
    # Add labels and styling
    ax.set_title(title)
    ax.ticklabel_format(style='plain', axis='y')
    ax.grid(True, linestyle='--', alpha=0.7)
    
    plt.show(block=False)
