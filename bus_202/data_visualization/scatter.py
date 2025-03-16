def scatter(df, y, x, ols=False):
    """
    Create a nice scatter plot with optional OLS line and correlation coefficient
    
    Parameters:
    df (pandas DataFrame): Input data
    y (str): Column name for y-axis variable
    x (str): Column name for x-axis variable
    ols (bool): If True, adds OLS line with confidence interval
    
    Returns:
    matplotlib figure
    """
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Calculate correlation coefficient
    corr = df[x].corr(df[y])
    
    # Set style
    plt.style.use('seaborn')
    
    # Create figure (let matplotlib handle default sizing)
    fig, ax = plt.subplots()
    
    # Create scatter plot
    if ols:
        # Use seaborn's regplot for scatter + OLS line
        sns.regplot(data=df, 
                   x=x, 
                   y=y,
                   scatter_kws={'alpha':0.5},
                   line_kws={'color': 'red'},
                   ci=95)
    else:
        # Use seaborn's scatterplot
        sns.scatterplot(data=df,
                       x=x,
                       y=y,
                       alpha=0.5)
    
    # Customize plot
    plt.title(f'{y} vs {x}\nCorrelation: {corr:.3f}', pad=15)
    plt.xlabel(x)
    plt.ylabel(y)
    
    # Add grid
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Adjust layout
    plt.tight_layout()
    
    return fig
