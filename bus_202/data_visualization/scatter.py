def scatter(df, y, x, ols=False):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Calculate correlation coefficient
    corr = df[x].corr(df[y])
    
    # Set style (using seaborn's default style)
    sns.set_style("whitegrid")
    
    # Create figure
    fig, ax = plt.subplots()
    
    # Create scatter plot
    if ols:
        # Use seaborn's regplot for scatter + OLS line
        sns.regplot(data=df, 
                   x=x, 
                   y=y,
                   scatter_kws={'alpha':0.5},
                   line_kws={'color': 'red'},
                   ci=None)
    else:
        # Use seaborn's scatterplot
        sns.scatterplot(data=df,
                       x=x,
                       y=y,
                       alpha=0.5)
    
    # Customize plot
    plt.title(f'{y} and {x}\nCorrelation: {corr:.3f}', pad=15)
    plt.xlabel(x)
    plt.ylabel(y)
    
    # Adjust layout
    plt.tight_layout()
    
    # Show plot without blocking
    plt.show(block=False)
