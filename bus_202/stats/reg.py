def reg(df, dp, ivs, logistic=False):
    import statsmodels.api as sm
    import pandas as pd
    
    # Convert ivs to list if it's a single string
    if isinstance(ivs, str):
        ivs = [ivs]
    
    # Create X and y
    X = df[ivs]
    y = df[dp]
    
    # Run appropriate regression
    if logistic:
        # Logistic regression with constant
        model = sm.Logit(y, X, add_constant=True)
    else:
        # OLS regression with constant
        model = sm.OLS(y, X, add_constant=True)
    
    # Fit model and return results
    try:
        results = model.fit()
        return results
    except Exception as e:
        print(f"Error fitting model: {e}")
        return None
