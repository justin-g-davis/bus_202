import matplotlib.pyplot as plt
import numpy as np

def histogram(series, title=None, bins=30):
    # Create figure and axis
    fig, ax = plt.subplots()
    
    if not label:
        title = series.name
    
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
    
    plt.show()
