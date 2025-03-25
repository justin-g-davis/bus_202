def reg(df, y, x, fe=None, logistic=False):
    import statsmodels.api as sm
    import pandas as pd
    
    # Convert ivs to list if it's a single string
    if isinstance(x, str):
        x = [x]
    
    # Create copy of dataframe to avoid modifying original
    df_reg = df.copy()
    
    # Handle fixed effects if specified
    if fe is not None:
        # Convert fe to list if it's a single string
        if isinstance(fe, str):
            fe = [fe]
        
        # Create dummies for each fixed effect variable
        for fe_var in fe:
            # Create dummies, drop first category to avoid multicollinearity
            dummies = pd.get_dummies(df_reg[fe_var], prefix=fe_var, drop_first=True)
            
            # Add dummies to dataframe
            df_reg = pd.concat([df_reg, dummies], axis=1)
            
            # Add dummy column names to x list
            x.extend(dummies.columns)
    
    # Create X and y, adding constant
    X = sm.add_constant(df_reg[x])
    y = df_reg[y]
    
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
