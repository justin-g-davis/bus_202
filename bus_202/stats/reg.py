def reg(df, dv, ivs, logistic=False):
    import statsmodels.api as sm
    import pandas as pd
    
    # Convert ivs to list if it's a single string
    if isinstance(ivs, str):
        ivs = [ivs]
    
    # Create X and y, adding constant
    X = sm.add_constant(df[ivs])
    y = df[dv]
    
    # Run appropriate regression
    if logistic:
        # Logistic regression
        model = sm.Logit(y, X)
    else:
        # OLS regression
        model = sm.OLS(y, X)
    
    # Fit model and return results
    try:
        results = model.fit()
        print(results.summary())
    except Exception as e:
        print(f"Error fitting model: {e}")
