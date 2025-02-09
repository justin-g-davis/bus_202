import matplotlib.pyplot as plt

def boxplot(series, title='Title', label=None):
    """
    Create a boxplot using matplotlib's axes interface.
    """
    # Create figure and axis
    fig, ax = plt.subplots()
    
    if not label:
        label = series.name
    
    # Convert to list, handle NaN, and wrap in list
    clean_data = [[x for x in series.dropna()]]
    
    # Create boxplot on the axis
    ax.boxplot(clean_data,
               patch_artist=True,
               boxprops=dict(facecolor='skyblue', color='black'),
               medianprops=dict(color='black'),
               flierprops=dict(marker='o', markerfacecolor='gray'),
               whiskerprops=dict(color='black'),
               capprops=dict(color='black'))
    
    # Add labels and styling
    ax.set_title(title)
    ax.set_ylabel(label)
    ax.ticklabel_format(style='plain', axis='y')
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Set y-axis limits based on data
    data_min = min(series.dropna())
    data_max = max(series.dropna())
    margin = (data_max - data_min) * 0.1  # 10% margin
    ax.set_ylim(data_min - margin, data_max + margin)
    
    plt.show(block=False)
