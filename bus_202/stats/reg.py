def reg(df, y, x, fe=None, logistic=False):
    import statsmodels.api as sm
    import pandas as pd
    
    # Convert ivs to list if it's a single string
    if isinstance(x, str):
        x = [x]
    
    # Create copy of dataframe to avoid modifying original
    df_reg = df.copy()
    
    # Convert main variables to numeric
    numeric_cols = [y] + x
    for col in numeric_cols:
        df_reg[col] = pd.to_numeric(df_reg[col], errors='coerce')
    
    # Handle fixed effects if specified
    if fe is not None:
        # Convert fe to list if it's a single string
        if isinstance(fe, str):
            fe = [fe]
        
        # Create dummies for each fixed effect variable
        for fe_var in fe:
            # Create dummies, drop first category to avoid multicollinearity
            dummies = pd.get_dummies(df_reg[fe_var], prefix=fe_var, drop_first=True, dtype=float)
            
            # Add dummies to dataframe
            df_reg = pd.concat([df_reg, dummies], axis=1)
            
            # Add dummy column names to x list
            x.extend(dummies.columns)
    
    # Drop rows with NaN values
    df_reg = df_reg.dropna(subset=[y] + x)
    
    # Create X and y, adding constant
    X = sm.add_constant(df_reg[x].astype(float))
    y_data = df_reg[y].astype(float)
    
    # Run appropriate regression
    if logistic:
        model = sm.Logit(y_data, X)
    else:
        model = sm.OLS(y_data, X)
    
    # Fit model and return results
    try:
        results = model.fit()
        print(results.summary())
        return results
    except Exception as e:
        print(f"Error fitting model: {e}")
